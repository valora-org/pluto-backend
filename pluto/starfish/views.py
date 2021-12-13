from rest_framework import (
    decorators,
    filters,
    permissions,
    response,
    status,
    viewsets,
)
from rest_framework.generics import get_object_or_404

from starfish import models, pusher, serializers


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

    def create(self, request, *args, **kwargs):
        serializer = serializers.ReviewSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return response.Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        review = models.Review.objects.create()

        channel = pusher.Channels.STARFISH
        event = pusher.Events.CREATE
        client = pusher.Pusher(channel=channel, event=event)

        message = f'Review {review.token} criada.'
        client.trigger(message)

        return response.Response(
            data=dict(id=review.id, token=review.token),
            status=status.HTTP_201_CREATED,
        )

    @decorators.action(
        methods=['post'], detail=True, url_name='join', url_path='join'
    )
    def join(self, request, pk):
        review = get_object_or_404(models.Review, pk=pk)
        team = get_object_or_404(models.Team, pk=request.data['team'])
        member, created = models.Member.objects.get_or_create(
            username=request.data['username'], team=team
        )
        review.members.add(member)

        channel = pusher.Channels.STARFISH
        event = pusher.Events.CREATE
        client = pusher.Pusher(channel=channel, event=event)

        message = f'Usuário {member.username} entrou na sala.'
        client.trigger(message)

        return response.Response(data=message, status=status.HTTP_200_OK)

    @decorators.action(
        methods=['post'], detail=False, url_name='start', url_path='start'
    )
    def start(self, request, pk):
        channel = pusher.Channels.STARFISH
        event = pusher.Events.START
        client = pusher.Pusher(channel=channel, event=event)

        message = 'Starfish iniciado!'
        client.trigger(message)

        return response.Response(data=message, status=status.HTTP_200_OK)

    @decorators.action(
        methods=['post'], detail=False, url_name='stop', url_path='stop'
    )
    def stop(self, request):
        channel = pusher.Channels.STARFISH
        event = pusher.Events.STOP
        client = pusher.Pusher(channel=channel, event=event)

        message = 'Starfish finalizado!'
        client.trigger(message)

        return response.Response(data=message, status=status.HTTP_200_OK)

    @decorators.action(
        methods=['post'], detail=False, url_name='vote', url_path='vote'
    )
    def vote(self, request):
        channel = pusher.Channels.STARFISH
        event = pusher.Events.VOTING
        client = pusher.Pusher(channel=channel, event=event)

        message = 'Iniciando votação!'
        client.trigger(message)

        return response.Response(data=message, status=status.HTTP_200_OK)

    @decorators.action(
        methods=['post'],
        detail=False,
        url_name='counting',
        url_path='counting',
    )
    def counting(self, request):
        channel = pusher.Channels.STARFISH
        event = pusher.Events.COUNTING
        client = pusher.Pusher(channel=channel, event=event)

        # TODO: should implement counting votes after merge suggestions

        message = 'Contabilizando votação!'
        client.trigger(message)

        return response.Response(data=message, status=status.HTTP_200_OK)

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
        methods=['post'], url_path='vote', url_name='vote', detail=True,
    )
    def vote(self, request, pk):
        suggestion = models.Suggestion.objects.get(id=pk)
        member = models.Member.objects.get(id=request.data['id_member'])

        suggestion.vote(member=member)
        return response.Response(status=status.HTTP_200_OK)
