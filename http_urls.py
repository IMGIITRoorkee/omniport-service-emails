from django.urls import path

from email.views.hello_world import HelloWorld

app_name = 'email'

urlpatterns = [
    path('', HelloWorld.as_view(), name='hello_world'),
]
