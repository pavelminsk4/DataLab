from celery import shared_task
from email.message import EmailMessage
import smtplib
from reports.models import *
import os
import environ
from pathlib import Path
import mimetypes
from docx import Document
from widgets.models import *

from .chartjs.chartjs import prepare_widget_images_for_regular
from reports.views_filling.filling_for_report import filling_templates_for_instant_and_regular_reports
from reports.social_views_filling.filling_for_social_report import filling_templates_for_social_reports
from .services.pdf_handler import convert_docx_to_pdf

from .social_chartjs.social_chartjs import prepare_social_widget_images
from uuid import uuid4

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

# ====================================================================

def filling_template(template_path, docx_path, project_id):
  document = Document(template_path)
  document = filling_templates_for_instant_and_regular_reports(document, project_id)
  document.save(docx_path)

def filling_social_template(template_path, docx_path, item, screenshots_list):
  document = Document(template_path)
  document = filling_templates_for_social_reports(document, item, screenshots_list)
  document.save(docx_path)

def create_pdf_file(item, template_path, report_format):
  docx_path = 'tmp/temp_reg_report_' + str(uuid4()) + '.docx'
  report_path = 'tmp/temp_reg_report_' + str(uuid4()) + '.' + report_format
  if item.module_type == 'Project':
    prepare_widget_images_for_regular(item)
    filling_template(template_path, docx_path, item.module_project_id)
  else:
    screenshots_list = prepare_social_widget_images(item)
    filling_social_template(template_path, docx_path, item, screenshots_list)
  convert_docx_to_pdf(docx_path, report_path)
  return report_path

# =====================================================================

def send_email_with(files, reg_report, crontab_type):
  users = reg_report.user.all()
  recipient_list = list(users.values_list('email', flat=True))
  msg = EmailMessage()
  msg['Subject'] = f'''Your {crontab_type} regular '{reg_report.title}' report from the Datalab project is here.'''
  msg['From'] = 'Datalab'
  msg['To'] = recipient_list
  mime_type, _ = mimetypes.guess_type(files[0])
  mime_type, mime_subtype = mime_type.split('/', 1)

  for file in files:
    with open(file, 'rb') as ap:
      msg.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=reg_report.title + file)
  with smtplib.SMTP_SSL('smtp.gmail.com', int(env('EMAIL_PORT'))) as smtp:
    smtp.login(env('EMAIL_HOST_USER'), env('EMAIL_HOST_PASSWORD'))
    smtp.send_message(msg)

@shared_task
def regular_report_sender(report_id , crontab_type):
  reg_report = RegularReport.objects.get(id=report_id)
  template_path = reg_report.report_template.layout_file
  files = []
  for item in reg_report.items.all():
    files.append(create_pdf_file(item, template_path, reg_report.report_format))
  send_email_with(files, reg_report, crontab_type)
