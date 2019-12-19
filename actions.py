from django.core.mail import EmailMessage

from omniport.settings import settings
from kernel.models import Person
from categories.redisdb import Subscription
from emails.tasks.push_email import qpush

def email_push(
        subject_text,
        body_text,
        category,
        by,
        has_custom_user_target=False,
        persons=None,
        ):

    email_from = settings.EMAIL_HOST_USER
    if has_custom_user_targets:
        if persons is None:
            raise ValueError(
                '\'persons\' cannot be None while \'has_custom_users_target\' '
                'is True '
            )
        else:
            for x in persons:
                p = Person.objects.get(id=x)
                msg = EmailMessage(
                    subject=subject_text,
                    body=html_content.replace("Subject/Text", subject_text).replace("Body/Text", body_text).replace("Sender/Text", p.full_name),
                    from_email=email_from,
                    to=[p.contact_information.get().email_address]
                )
                msg.content_subtype = "html"
                qpush(msg)

    else:
        category = category.slug
        persons = Subscription.fetch_people(category_slug=category, action='email')
        for x in persons:
            p = Person.objects.get(id=x)
            msg = EmailMessage(
                subject=subject_text,
                body=html_content.replace("Subject/Text", subject_text).replace("Body/Text", body_text),
                from_email=email_from,
                to=[p.contact_information.get().email_address]
            )
            msg.content_subtype = "html"
            qpush(msg)   
