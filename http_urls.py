from django.urls import path

from emails.views.subscription import Subscription
from emails.views.send_email import SendEmail
app_name = 'emails'

urlpatterns = [
    path('subscribe/', Subscription.as_view()),
    path('send/', SendEmail.as_view()),
]
