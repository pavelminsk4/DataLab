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

from .chartjs.chartjs import prepare_widget_images
from reports.views_filling.filling_for_report import filling_templates_for_instant_and_regular_reports
from .services.pdf_handler import convert_docx_to_pdf

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

# ====================================================================

def filling_template(template_path, project_id):
  document = Document(template_path)
  document = filling_templates_for_instant_and_regular_reports(document, project_id)
  document.save('tmp/temp_reg_report.docx')

def create_pdf_file(reg_report, crontab_type):
  if crontab_type == 'hourly':
    template_path = str(reg_report.h_template.layout_file)
  if crontab_type == 'daily':
    template_path = str(reg_report.d_template.layout_file)
  if crontab_type == 'weekly':
    template_path = str(reg_report.w_template.layout_file)
  if crontab_type == 'monthly':
    template_path = str(reg_report.m_template.layout_file)
  docx_path='tmp/temp_reg_report.docx'
  report_path='tmp/temp_reg_report.' + 'pdf'
  if reg_report.module_type == 'Project':
    prepare_widget_images(reg_report.module_project_id)
    filling_template(template_path, reg_report.module_project_id)
  else:
    prepare_social_widget_images(reg_report.module_project_id)
    filling_social_template(template_path, reg_report.module_project_id)
  convert_docx_to_pdf(docx_path, report_path)
  return report_path

# =====================================================================

def send_email_with(file, reg_report, crontab_type):
  users = reg_report.user.all()
  recipient_list = list(users.values_list('email', flat=True))
  msg = EmailMessage()
  msg['Subject'] = f'''Your {crontab_type} regular '{reg_report.title}' report from the '{reg_report.project.title}' Datalab project is here.'''
  msg['From'] = 'Datalab'
  msg['To'] = recipient_list
  mime_type, _ = mimetypes.guess_type(file)
  mime_type, mime_subtype = mime_type.split('/', 1)
  with open(file, 'rb') as ap:
    msg.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename='report-regular')
  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(env('EMAIL_HOST_USER'), env('EMAIL_HOST_PASSWORD'))
    smtp.send_message(msg)

@shared_task
def regular_report_sender(report_id , crontab_type):
  reg_report = RegularReport.objects.get(id=report_id)
  file = create_pdf_file(reg_report, crontab_type)
  send_email_with(file, reg_report, crontab_type)
