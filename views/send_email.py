from rest_framework.views import APIView
from rest_framework.response import Response

from categories.models import Category
from emails.actions import email_push


class SendEmail(APIView):
    """
    View to send an email by an API request
    """

    def post(self, request):
        """
        Send email
        :param request: API request
        :return: API response 1 if successful
        """
        token = self.request.data.get('token', None)
        category = Category.objects.get(slug=self.request.data['slug'])

        if category.meta['token'] == token:
            subject = self.request.data.get('subject', None)
            body = self.request.data.get('body', None)
            by = self.request.data.get('by', None)
            email_ids = self.request.data.get('email_ids', None)
            target_app_name = self.request.data.get(
                'targetAppName',
                category.meta.get('targetAppName', None)
            )
            target_app_url = self.request.data.get(
                'targetAppUrl',
                category.meta.get('targetAppUrl', None)
            )
            use_primary_email = self.request.data.get('useCustomEmail', False)
            check_if_primary_email_verified = self.request.data.get('checkIfVerified', False)

            if email_ids:
                return Response(
                    email_push(
                        subject_text=subject,
                        body_text=body,
                        category=None,
                        has_custom_user_target=True,
                        persons=None,
                        email_ids=email_ids,
                        by=by,
                        use_primary_email=use_primary_email,
                        check_if_primary_email_verified=check_if_primary_email_verified,
                        target_app_name=target_app_name,
                        target_app_url=target_app_url
                    )
                )
