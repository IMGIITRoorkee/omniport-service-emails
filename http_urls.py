from django.urls import path

from emails.views.subscription import Subscription
from emails.views.hello_world import HelloWorld
app_name = 'emails'

urlpatterns = [
    path('', HelloWorld.as_view()),
    path('subscribe/', Subscription.as_view()),
]
