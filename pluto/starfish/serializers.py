from pluto import settings
from starfish import models
from rest_framework import serializers


class TeamSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True, allow_null=False
    )

    class Meta:
        model = models.Team
        read_only_fields = ['id']
        fields = ['id', 'name']


class MemberSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True, allow_null=False
    )
    team = serializers.PrimaryKeyRelatedField(
        queryset=models.Team.objects.all(), required=True, allow_null=False
    )

    class Meta:
        model = models.Member
        read_only_fields = ['id', 'team']
        fields = ['id', 'username', 'team']


class ReviewSerializer(serializers.ModelSerializer):
    goal = serializers.CharField(
        required=False, allow_null=True
    )
    token = serializers.UUIDField(
        read_only=True
    )
    members = serializers.PrimaryKeyRelatedField(
        queryset=models.Member.objects.all(),
        many=True,
        required=False,
        allow_null=True
    )
    suggestions = serializers.PrimaryKeyRelatedField(
        queryset=models.Suggestion.objects.all(),
        many=True,
        required=False,
        allow_null=True
    )
    team = serializers.PrimaryKeyRelatedField(
        queryset=models.Team.objects.all(), required=False, allow_null=True
    )
    created_at = serializers.DateTimeField(format=settings.DEFAULT_DATETIME_FORMAT, read_only=True)

    class Meta:
        model = models.Review
        read_only_fields = ['id', 'created_at']
        fields = ['id', 'goal', 'token', 'members', 'suggestions', 'team', 'created_at']
