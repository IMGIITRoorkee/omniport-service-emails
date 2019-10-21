from django.urls import path

from emails.views import Subscription, HelloWorld

app_name = 'emails'

urlpatterns = [
    path('', HelloWorld.as_view()),
    path('subscribe/', Subscription.as_view()),
]
