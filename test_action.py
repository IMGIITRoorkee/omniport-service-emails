from django.core.mail import EmailMessage
from omniport.settings import settings

from categories.redisdb import Subscription
from emails.tasks.push_email import qpush
from emails.html_content import html_content

def email_push(
        subject,
        ):
        msg = EmailMessage(
                subject=subject,
                body=html_content,
                from_email=settings.EMAIL_HOST_USER,
                to=['pchoudhary1@ee.iitr.ac.in']
        )
        msg.content_subtype = "html"
        qpush(msg)

