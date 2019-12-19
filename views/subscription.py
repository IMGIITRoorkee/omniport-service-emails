from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from categories.models import UserSubscription, Category
from categories.serializers import CategorySerializer, SubscriptionTreeSerializer


class Subscription(APIView):

    permission_classes = [IsAuthenticated, ]
    
    def get(self, request, *args, **kwargs):

        roots = Category.objects.root_nodes()
        serializer = SubscriptionTreeSerializer(roots, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
      
        try:
            new_subscriptions = request.data['save']
            new_unsubscription = request.data['delete']
        except KeyError:
            return Response(
                data={
                    'success': False,
                    'error': 'Invalid payload'
                },
                status=400
            )

        for category in new_subscriptions:
            _ = UserSubscription(
                person=request.person,
                category=category,
                action='email',
            ).subscribe()

        for category in new_unsubscription:
            _ = UserSubscription(
                person=request.person,
                category=category,
                action='email',
            ).unsubscribe()

        return Response(
            data={
                'success': True,
            },
            status=200
        )
