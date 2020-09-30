import logging

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from categories.models import UserSubscription, Category
from categories.serializers import SubscriptionTreeSerializer
from categories.utils.get_subscription import GetSubscription

logger = logging.getLogger('emails')


class Subscription(APIView):
    """
    Handle email subscription
    """
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        """
        Fetch email subscription tree of the user
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        roots = Category.objects.root_nodes()
        serializer = SubscriptionTreeSerializer(roots, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        Update email subscription tree of the user
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        try:
            new_subscriptions = request.data['save']
            new_unsubscription = request.data['drop']
        except KeyError:
            logger.error(
                f'Post request sent by {self.request.person} '
                'was identified as bad request due to \'KeyError\' exception'
            )
            return Response(
                data={
                    'success': False,
                    'error': 'Invalid payload'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        subscribe,unsubscribe = GetSubscription(
                                new_subscriptions,
                                new_unsubscription,
                                request.person,
                                'notifications'
                            ).get_should_subscribe()

        for category in unsubscribe:
            _ = UserSubscription(
                person=request.person,
                category=category,
                action='emails',
            ).unsubscribe()
            
        for category in subscribe:
            _ = UserSubscription(
                person=request.person,
                category=category,
                action='emails',
            ).subscribe()

        logger.info(
            'Successfully updated the email subscriptions for '
            f'{self.request.person}'
        )
        return Response(
            data={
                'success': True,
            },
            status=status.HTTP_201_CREATED
        )
