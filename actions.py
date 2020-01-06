from datetime import datetime
from django.core.mail import EmailMessage
from django.conf import settings
from kernel.models import Person
from categories.redisdb import Subscription

from emails.html_content import html_content
from emails.utils.get_person_contact import get_person_contact
from emails.tasks.push_email import qpush


def email_push(
        subject_text,
        body_text,
        category,
        has_custom_user_target=False,
        persons=None,
        email_ids=None,
        by=None,
        use_custom_email=False,
        check_if_verified=False,
        target_app_name=None,
        target_app_url=None,
):
    if target_app_name is not None and target_app_url is None:
        target_name = target_app_name
        target_url = ''

    elif target_app_name is not None and target_app_url is not None:
        target_name = 'Open in ' + target_app_name
        target_url = target_app_url

    else:
        target_name = ''
        target_url = ''

    now = datetime.now()
    email_from = settings.EMAIL_HOST_USER
    if by is not None:
        sender = Person.objects.get(id=by).full_name
        html_content_mod = html_content.replace("Sender/Text", sender)
    else:
        sender = ''
        html_content_mod = html_content.replace(
            "<b>Posted By:</b> Sender/Text", sender)

    if has_custom_user_target:
        if persons is not None:
            for x in persons:
                p = None
                try:
                    p = Person.objects.get(id=x)
                except:
                    pass

                if p:
                    to = [get_person_contact(p, use_custom_email, check_if_verified)]

        elif persons is None and email_ids is not None:
            to = email_ids

        else:
            raise ValueError(
                '\'persons\' and \'email_ids\' cannot be None while \'has_custom_users_target\' '
                'is True '
            )

    else:
        category = category.slug
        persons = Subscription.fetch_people(category_slug=category, action='email')
        for x in persons:
            p = None
            try:
                p = Person.objects.get(id=x)
            except Exception:
                pass

            if p:
                to = [get_person_contact(p, use_custom_email, check_if_verified)]

    msg = EmailMessage(
        subject=subject_text,
        body=html_content_mod.replace("Subject/Text", subject_text).replace("Body/Text", body_text).replace(
            "TargetApp/Text", target_name).replace("TargetURL/Text", target_url).replace("Time/Text", now.strftime(
            "%d %B %Y at %H:%M")),
        from_email=email_from,
        to=to
    )
    msg.content_subtype = "html"
    qpush(msg)
