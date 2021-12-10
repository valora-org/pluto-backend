from rest_framework import filters, permissions, viewsets, decorators
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
    search_fields = ["name"]
    ordering_fields = ["-id", "name"]


class MemberViewSet(viewsets.ModelViewSet):
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ["username", "team__name"]
    ordering_fields = ["-id", "username"]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ["goal", "suggestions__text"]
    ordering_fields = ["-id"]


class SuggestionViewSet(viewsets.ModelViewSet):
    queryset = models.Suggestion.objects.all()
    serializer_class = serializers.SuggestionSerializer
    permission_classes = (permissions.AllowAny,)

    @decorators.action(
        methods=["post"],
        url_path="vote",
        url_name="vote",
        detail=False,
    )
    def vote(self, reqeust):
        pass
