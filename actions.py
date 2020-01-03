from django.core.mail import EmailMessage
from emails.html_content import html_content
from omniport.settings import settings
from kernel.models import Person
from categories.redisdb import Subscription
from emails.tasks.push_email import qpush
from datetime import datetime

def email_push(
        subject_text,
        body_text,
        category,
        by,
        has_custom_user_target=False,
        persons=None,
        target_app_name=None,
        target_app_url=None
        ):
    
    if target_app_name is not None and target_app_url is None:
        target_name=target_app_name
        target_url=''

    elif target_app_name is not None and target_app_url is not None:
        target_name='Open in ' + target_app_name
        target_url=target_app_url

    else:
        target_name=''
        target_url=''

    now = datetime.now()
    email_from = settings.EMAIL_HOST_USER

    if has_custom_user_target:
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
                    body=html_content.replace("Subject/Text", subject_text).replace("Body/Text", body_text).replace("Sender/Text", p.full_name).replace("TargetApp/Text", target_name).replace("TargetURL/Text", target_url).replace("Time/Text", now.strftime("%d %B at %Y %H:%M")),
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
                body=html_content.replace("Subject/Text", subject_text).replace("Body/Text", body_text).replace("Sender/Text", p.full_name).replace("TargetApp/Text", target_name).replace("TargetURL/Text", target_url).replace("Time/Text", now.strftime("%d %B %Y at %H:%M")),
                from_email=email_from,
                to=[p.contact_information.get().email_address]
            )
            msg.content_subtype = "html"
            qpush(msg)   
