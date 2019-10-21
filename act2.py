from django.core.mail import EmailMessage
from omniport.settings import settings
from kernel.models import Person

from categories.redisdb import Subscription
from emails.tasks.push_email import qpush
from emails.html_content import html_content

def email_push(
        subject,
        pid
        ):
        p = Person.objects.get(pid)
        msg = EmailMessage(
                subject=subject,
                body=html_content,
                from_email=settings.EMAIL_HOST_USER,
                to=[p.contact_information.get().email_address]
        )
        msg.content_subtype = "html"
        qpush(msg)
