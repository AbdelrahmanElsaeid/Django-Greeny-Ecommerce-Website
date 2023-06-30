from celery import shared_task
import time



@shared_task
def celery_send_emails(users):
    time.sleep(10)
    for i in range(20):

        print(f"send email to :  {i}")