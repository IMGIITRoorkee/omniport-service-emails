from django.core.mail import EmailMessage
from core.configuration.models.project.emails import Emails
from kernel.models import Person

from categories.redisdb import Subscription
from emails.tasks.push_email import qpush
from emails.html_content import html_content

def email_push(
        subject,
        ):
        em = Emails()
        msg = EmailMessage(
                subject=subject,
                body=html_content,
                from_email=em.EMAIL_HOST_USER,
                to=['pchoudhary1@ee.iitr.ac.in']
        )
        msg.content_subtype = "html"
        msg.mixed_subtype = "related"
        msg.attach('logo_192.png', 'image/png')
        qpush(msg)

