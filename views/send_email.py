import json
from rest_framework.views import APIView
from rest_framework.response import Response

from categories.models import Category
from emails.actions import email_push

class SendEmail(APIView):

    def post(self, request):
        token = self.request.data(['token'])

        category = Category.objects.get(slug=self.request.data['slug'])
        if category.meta['token']==token:
            subject = self.request.data['subject']
            body = self.request.data['body']
            
            try:
                by = self.request.data['by']
            except:
                by=None

            try:
               # if self.request.data['hasCustomUserTarget']
                has_custom_user_target = self.request.data['hasCustomUserTarget']
            except:
                has_custom_user_target=True
            

            try:
                persons = self.request.data['persons']
            except:
                persons=None


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

            email_push(subject, body, category, by, has_custom_user_target, persons, target_app_name, target_app_url, use_custom_email)
            #return Response(self)
