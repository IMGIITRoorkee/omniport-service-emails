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
                                'emails'
                            ).get_should_subscribe()

        failures = list()

        for category in unsubscribe:
            if not UserSubscription(
                person=request.person,
                category=category,
                action='emails',
            ).unsubscribe():
                failures.append(category.slug)

        for category in subscribe:
            if not UserSubscription(
                person=request.person,
                category=category,
                action='emails',
            ).subscribe():
                failures.append(category.slug)

        # Safe for the caller to retry: both calls are idempotent
        if failures:
            logger.error(
                'Failed to update the email subscriptions of '
                f'{self.request.person} for the categories {failures}'
            )
            return Response(
                data={
                    'success': False,
                    'error': 'Some subscriptions could not be updated',
                    'failed': failures,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

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
