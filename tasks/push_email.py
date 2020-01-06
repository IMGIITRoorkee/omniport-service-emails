from omniport.celery import celery_app
from django.core.mail import send_mass_mail
from django.core.mail import EmailMessage


@celery_app.task(
    queue='celery',
    autoretry_for=(Exception,),
    retry_kwargs={'max_retries': 5}
)
def qpush(EmailMessage):
    EmailMessage.send()
