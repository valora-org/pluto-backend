from rest_framework import viewsets, decorators, response, status
from starfish import models, serializers


class SuggestionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SuggestionSerializer
    queryset = models.Suggestion.objects.all()

    @decorators.action(
        methods=["post"],
        url_path="vote",
        url_name="vote",
        detail=False,
    )
    def vote(self, reqeust):
        return response.Response(
            {"messege": 'Vary good!".'},
            status=status.HTTP_200_OK,
        )
