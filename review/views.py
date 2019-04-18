from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Review

from . import serializers
from ipware import get_client_ip


class ReviewViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        """return objects for the current auth'd user only"""
        return self.queryset.filter(reviewer=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        """create a new obj"""
        client_ip, is_routable = get_client_ip(self.request)
        if client_ip is None:
            # Unable to get the client's IP address
            ip_address = ''
        else:
            # We got the client's IP address
            if is_routable:
                # The client's IP address is publicly routable on the Internet
                ip_address = client_ip
            else:
                # The client's IP address is private
                ip_address = client_ip
        serializer.save(reviewer=self.request.user, ip_address=ip_address)
