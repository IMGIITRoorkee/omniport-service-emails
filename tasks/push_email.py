from categories.redisdb import Subscription
from omniport.celery import celery_app
from django.core.mail import send_mail
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
            send_mail(subject, body, by, persons)


    else:
        category = category.slug
        persons = Subscription.fetch_people(category_slug=category, action='email')
        send_mail(subject, body, by, persons)
