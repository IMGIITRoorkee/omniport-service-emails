from omniport.celery import celery_app


@celery_app.task(
    queue='celery',
    autoretry_for=(Exception,),
    retry_kwargs={'max_retries': 5}
)
def queue_push(email_message):
    """
    Batch-wise pushing emails using message-broker
    :param email_message: EmailMessage instance to be sent
    :return: success/failure as 1 or 0
    """
    return email_message.send()
