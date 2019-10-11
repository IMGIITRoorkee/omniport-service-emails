from categories.redisdb import Subscription
from omniport.celery import celery_app
from django.core.mail import send_mass_mail
from django.core.mail import EmailMessage

@celery_app.task(
        queue='celery',
        autoretry_for=(Exception,),
        retry_kwargs={'max_retries': 5}
)
def email_push(
        subject,
        body,
        category,
        title,
        by,
        has_custom_user_target=False,
        persons=None,
        ):




    if has_custom_user_targets:
        if persons is None:
            raise ValueError(
                '\'persons\' cannot be None while \'has_custom_users_target\' '
                'is True '
            )
        else:
    """
    Todo: Process body to html_content
          fetch email_from
    """
           " email_from = settings.EMAIL_HOST_USER"
            html_content = "body_here"
            html_content.replace("body_here",body)
            msg = EmailMessage(subject, html_content, email_from, persons)
            msg.content_subtype = "html"
            msg.send()

    """
    Todo: fetch email_id for persons
    """
    else:
        category = category.slug
        persons = Subscription.fetch_people(category_slug=category, action='email')
        send_mass_mail(subject, body, by, persons)
