from celery import shared_task




@shared_task
def celery_send_emails(users):
    for i in range(20):

        print(f"send email to {i}")