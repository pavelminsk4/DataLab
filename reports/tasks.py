from celery import shared_task
from email.message import EmailMessage
import smtplib
from reports.models import *
import os
import environ
from pathlib import Path
import mimetypes
from widgets.models import *
from reports.classes.project_pdf import Factory_PDF


BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))


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
            msg.add_attachment(ap.read(), maintype=mime_type,
                               subtype=mime_subtype, filename=reg_report.title + file)
    with smtplib.SMTP_SSL('smtp.gmail.com', int(env('EMAIL_PORT'))) as smtp:
        smtp.login(env('EMAIL_HOST_USER'), env('EMAIL_HOST_PASSWORD'))
        smtp.send_message(msg)


@shared_task
def regular_report_sender(report_id, crontab_type):
    reg_report = RegularReport.objects.get(id=report_id)
    template_path = reg_report.report_template.layout_file
    files = []
    for item in reg_report.items.all():
        files.append(Factory_PDF(item, template_path, reg_report.report_format).define().generate())
    send_email_with(files, reg_report, crontab_type)
