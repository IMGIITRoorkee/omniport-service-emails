from django.urls import path

from emails.views.subscription import Subscription

app_name = 'emails'

urlpatterns = [
    path('', Subscription.as_view()),
]
