from django.core.mail import EmailMessage
from omniport.settings import settings

from categories.redisdb import Subscription
from emails.tasks.push_email import qpush

def email_push(
        subject,
        body,
        category,
        by,
        has_custom_user_target=False,
        persons=None,
        ):

    """
    Todo: fetch emails for persons, fetch email_from
    """

    if has_custom_user_targets:
        if persons is None:
            raise ValueError(
                '\'persons\' cannot be None while \'has_custom_users_target\' '
                'is True '
            )
        else:
            email_from = settings.EMAIL_HOST_USER
            """html_content = "body_here"
            html_content.replace("body_here",body)"""
            msg = EmailMessage(
                    subject=subject,
                    body=body,
                    email_from=email_from,
                    persons=persons
            )
            msg.content_subtype = "html"
            qpush(msg)

    else:
        category = category.slug
        persons = Subscription.fetch_people(category_slug=category, action='email')
        send_mass_mail(subject, body, by, persons)
