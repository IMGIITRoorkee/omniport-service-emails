from django.urls import path

from emails.views.subscription import Subscription
from emails.views.template import EmailTemplate
from emails.views.send_email import SendEmail
app_name = 'emails'

urlpatterns = [
    path('', EmailTemplate.as_view()),
    path('subscribe/', Subscription.as_view()),
    path('send/', SendEmail.as_view()),
]
