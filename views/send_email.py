import json
from rest_framework.views import APIView
from rest_framework.response import Response

from categories.models import Category
from emails.actions import email_push

class SendEmail(APIView):

    def post(self, request):
        token = self.request.data['token']

        category = Category.objects.get(slug=self.request.data['slug'])
        if category.meta['token']==token:
            subject = self.request.data['subject']
            body = self.request.data['body']
            
            try:
                by = self.request.data['by']
            except:
                by=None

            try:
                email_ids = self.request.data['email_ids']
            except:
                email_ids=None

            try:
                target_app_name = self.request.data['targetAppName']
            except:
                try:
                    target_app_name = category.meta['targetAppName']
                except:
                    target_app_name=None


            try:
                target_app_url = self.request.data['targetAppUrl']
            except:
                try:
                    target_app_url = category.meta['targetAppUrl']
                except:
                    target_app_url=None

            try:
                use_custom_email = self.request.data['use_custom_email']
            except:
                use_custom_email=False

            try:
                check_if_verified = self.request.data['check_if_verified']
            except:
                check_if_verified=False
            if email_ids:
                email_push(subject,
                           body,
                           None,
                           True,
                           None,
                           email_ids,
                           by,
                           use_custom_email,
                           check_if_verified,
                           target_app_name,
                           target_app_url)
#return Response(self)
