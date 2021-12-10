from rest_framework import (filters, permissions, viewsets)
from starfish import models
from starfish import serializers

class TeamViewSet(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ['name']
    ordering_fields = ['-id', 'name']


class MemberViewSet(viewsets.ModelViewSet):
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ['username', 'team__name']
    ordering_fields = ['-id', 'username']


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ['goal', 'suggestions__text']
    ordering_fields = ['-id']
