from django.core.mail import EmailMultiAlternatives
from omniport.settings import settings
from django.template.loader import render_to_string

from kernel.models import Person

from categories.redisdb import Subscription
from emails.tasks.push_email import qpush

def email_push(
        subject,
        ):
        html_content = render_to_string('emails/samp.html'),
        msg = EmailMultiAlternatives(
                subject=subject,
                body=html_content,
                from_email=settings.EMAIL_HOST_USER,
                to=['pchoudhary1@ee.iitr.ac.in']
        )
        msg.attach_alternative(html_content, "text/html")
        qpush(msg)
