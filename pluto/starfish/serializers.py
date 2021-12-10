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
        read_only_fields = ['id']
        fields = ['id', 'username', 'team']


class ReviewSerializer(serializers.ModelSerializer):
    goal = serializers.CharField(
        required=True, allow_null=False
    )
    members = serializers.PrimaryKeyRelatedField(
        queryset=models.Member.objects.all(),
        required=True,
        allow_null=False
    )
    suggestions = serializers.PrimaryKeyRelatedField(
        queryset=models.Suggestion.objects.all(),
        required=True,
        allow_null=False
    )
    team = serializers.PrimaryKeyRelatedField(
        queryset=models.Team.objects.all(), required=True, allow_null=False
    )
    created_at = serializers.DateTimeField(format=settings.DEFAULT_DATETIME_FORMAT)

    class Meta:
        model = models.Review
        read_only_fields = ['id', 'created_at']
        fields = ['id', 'goal', 'members', 'suggestions', 'team', 'created_at']
