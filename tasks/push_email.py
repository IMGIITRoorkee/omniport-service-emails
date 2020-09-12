from datetime import datetime
from django.core.mail import EmailMessage
from email.mime.image import MIMEImage

from omniport.celery import celery_app

celery_app.control.add_consumer('emails', reply=True) # Create separate queue for email task

@celery_app.task(
    queue='emails',
    autoretry_for=(Exception,),   
    retry_kwargs={'max_retries': 5}
)
def queue_push(subject, body, from_email, recipient):
    """
    Batch-wise pushing emails using message-broker
    :param email_message: EmailMessage instance to be sent
    :return: success/failure as 1 or 0
    """

    logo_data = ''
    with open('../branding/maintainers/logo.png', 'rb') as logo_file:
        logo_data = logo_file.read()

    logo = MIMEImage(logo_data)
    logo.add_header('Content-ID', '<logo>')

    email_message = EmailMessage(
        subject=subject,
        body=body,
        from_email=from_email,
        to=[recipient]
    )
    email_message.content_subtype = "html"
    email_message.attach(logo)

    return email_message.send()
