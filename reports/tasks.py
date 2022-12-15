from celery import shared_task

@shared_task
def regular_report_sender():
  print('-------->REGULAR_REPORT_TRIGERED')
  return True
