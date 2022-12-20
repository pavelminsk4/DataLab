from celery import shared_task
from email.message import EmailMessage
import smtplib
from reports.models import *

import os
import environ
from pathlib import Path
import mimetypes
import aspose.words as aw

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

from .chartjs import prepare_widget_images

# ====================================================================

def prepare_widget_images():
  return True

def filling_template(template_path, pk):
  return True

def convert_docx_to_pdf(docx_path, report_path):
  doc = aw.Document(docx_path)
  doc.save(report_path)

def create_pdf_file(reg_report):
  template_path = str(reg_report.template.layout_file)
  docx_path='tmp/temp_reg_report.docx'
  report_path='tmp/temp_reg_report.' + 'pdf'

  prepare_widget_images(reg_report)
  filling_template(template_path, reg_report.project.pk)
  convert_docx_to_pdf(docx_path, report_path)

# =====================================================================

def send_email_with(file, recipient_list):
  msg = EmailMessage()
  msg['Subject'] = 'Subject: Regular Report from your Anova project.'
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
def regular_report_sender(report_id):
  print('-------->REGULAR_REPORT_TRIGERED')
  reg_report = RegularReport.objects.get(id=report_id)
  users = reg_report.user.all()
  recipient_list = list(users.values_list('email', flat=True))
  create_pdf_file(reg_report)
  file = './tmp/temp_reg_report.pdf'
  send_email_with(file, recipient_list)
