from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from emails.html_content import html_content
class EmailTemplate(APIView):
    """
    Returns the email template
    """

    def get(self, request, *args, **kwargs):
        return HttpResponse(html_content)
