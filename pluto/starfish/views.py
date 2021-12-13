from rest_framework import filters, permissions, viewsets, decorators, response, status
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

    @decorators.action(
        methods=["post"],
        url_path="export",
        url_name="export",
        detail=True,
    )
    def export_csv(self, request, pk):
        review = models.Review.objects.get(id=pk)
        serializer = serializers.ReviewSerializer(review)
        
        review.export(data=serializer.data)

        return response.Response(status=status.HTTP_200_OK)



class SuggestionViewSet(viewsets.ModelViewSet):
    queryset = models.Suggestion.objects.all()
    serializer_class = serializers.SuggestionSerializer
    permission_classes = (permissions.AllowAny,)

    @decorators.action(
        methods=["post"],
        url_path="vote",
        url_name="vote",
        detail=True,
    )
    def vote(self, request, pk):
        suggestion = models.Suggestion.objects.get(id=pk)
        member = models.Member.objects.get(id=request.data["id_member"])

        suggestion.vote(member=member)
        return response.Response(status=status.HTTP_200_OK)
