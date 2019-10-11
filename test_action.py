from django.core.mail import EmailMessage
from omniport.settings import settings

from categories.redisdb import Subscription
from emails.tasks.push_email import qpush

def email_push(
        subject,
        body,
        ):
        msg = EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.EMAIL_HOST_USER,
                to=['pchoudhary1@ee.iitr.ac.in']
        )
        qpush(msg)

