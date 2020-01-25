from datetime import datetime
from django.core.mail import EmailMessage
from django.conf import settings
from email.mime.image import MIMEImage

from kernel.models import Person
from categories.redisdb import Subscription
from emails.html_content import get_html_content
from emails.utils.get_people_contact import get_people_contact
from emails.tasks.push_email import queue_push


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
    """
    TODO
    :param subject_text: subject of the email to be sent
    :param body_text: body of the email to be sent
    :param category: category of subscription
    :param has_custom_user_target: Boolean for whether
    :param persons: ids of the persons to whom it is to be sent
    :param email_ids: email ids of the persons to whom it is to be sent
    :param by: id of the person who is posting the mail
    :param use_custom_email: Boolean for whether to use custom email address
    :param check_if_verified: Boolean for whether to check email verification
    :param target_app_name: name of a target app to be passed
    :param target_app_url: url of a link from the target app
    :return: response of the request
    """

    if target_app_name is not None and target_app_url is None:
        target_name = target_app_name
        target_url = ''

    elif target_app_name is not None and target_app_url is not None:
        target_name = 'Open in ' + target_app_name
        target_url = target_app_url

    else:
        target_name = ''
        target_url = ''

    email_from = settings.EMAIL_HOST_USER
    logo_data = open('../branding/maintainers/logo.png', 'rb').read()
    logo = MIMEImage(logo_data)
    logo.add_header('Content-ID', '<logo>')

    if has_custom_user_target:
        if persons is not None:
            recipients = get_people_contact(
                persons,
                use_custom_email,
                check_if_verified
            )
        elif email_ids is not None:
            recipients = email_ids
        else:
            raise ValueError(
                '\'persons\' and \'email_ids\' cannot be None '
                'while \'has_custom_users_target\' '
                'is True '
            )

    else:
        persons = Subscription.fetch_people(
            category_slug=category.slug,
            action='email'
        )
        recipients = get_people_contact(
            persons,
            use_custom_email,
            check_if_verified
        )
    html_content = get_html_content()
    if html_content is not None:
        if by is not None:
            sender = Person.objects.get(id=by).full_name
            html_content_mod = html_content.replace("Sender", sender)
        else:
            sender = ''
            html_content_mod = html_content.replace(
                "<b>Posted By:</b> Sender", sender
            )
        for recipient in recipients:
            msg = EmailMessage(
                subject=subject_text,
                body=html_content_mod.replace(
                    "Subject", subject_text
                ).replace(
                    "Body", body_text
                ).replace(
                    "TargetApp", target_name
                ).replace(
                    "TargetURL", target_url
                ).replace(
                    "Time", datetime.now().strftime("%d %B %Y at %H:%M")
                ),
                from_email=email_from,
                to=[recipient]
            )
            msg.content_subtype = "html"
            msg.attach(logo)
            return queue_push(msg)
