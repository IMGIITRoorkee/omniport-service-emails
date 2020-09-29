import swapper

from datetime import datetime
from django.conf import settings

from categories.redisdb import Subscription

from emails.html_content import get_html_content
from emails.utils.get_people_contact import get_people_contact
from emails.tasks.push_email import queue_push

Person = swapper.load_model('kernel', 'Person')


def email_push(
        subject_text,
        body_text,
        category,
        has_custom_user_target=False,
        persons=None,
        email_ids=None,
        by=None,
        use_primary_email=False,
        check_if_primary_email_verified=False,
        target_app_name=None,
        target_app_url=None,
        send_only_to_subscribed_users=False
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
    :param use_primary_email: Boolean for whether to use custom email address
    :param check_if_primary_email_verified: Boolean for whether to check email verification
    :param target_app_name: name of a target app to be passed
    :param target_app_url: url of a link from the target app
    :param send_only_to_subscribed_users: Flag for a notification only to be sent to subscribed users
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

    from_email = (f'{settings.SITE.nomenclature.verbose_name} '
                  f'<{settings.EMAIL_HOST_USER}>')

    if has_custom_user_target:
        if persons is not None:
            persons = [
                person.id if isinstance(person, Person) else person
                for person in persons
            ]

            if send_only_to_subscribed_users:
                # Get a set of all subscribed people ids
                subscribed_persons = {
                    int(person_id) for person_id in
                    Subscription.fetch_people(
                        category_slug=category.slug,
                        action='emails'
                    )
                }

                # Grab an intersection of the subscribed people and the complete list
                persons = list(subscribed_persons.intersection(persons))

            recipients = get_people_contact(
                persons,
                use_primary_email,
                check_if_primary_email_verified
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
            action='emails'
        )
        recipients = get_people_contact(
            persons,
            use_primary_email,
            check_if_primary_email_verified
        )
    html_content = get_html_content()
    if html_content is not None:
        if by is not None:
            sender = Person.objects.get(id=by).full_name
            html_content = html_content.replace('Sender', sender)
        else:
            sender = ''
            html_content = html_content.replace(
                '<b>Posted By:</b> Sender', sender
            )
        body = html_content.replace(
            'Subject', subject_text
        ).replace(
            'Body', body_text
        ).replace(
            'TargetApp', target_name
        ).replace(
            'TargetURL', target_url
        ).replace(
            'Time', datetime.now().strftime('%d %B %Y at %H:%M')
        )

        for recipient in recipients:
            queue_push.delay(
                subject_text,
                body,
                from_email,
                recipient,
            )
