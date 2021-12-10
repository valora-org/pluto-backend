import uuid

from django.db import models

from starfish import choices


class Team(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=64, null=False)

    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Times'

    def __str__(self):
        return self.name


class Member(models.Model):
    username = models.CharField(
        verbose_name='Nome de usuário', max_length=64, null=False
    )
    team = models.ForeignKey(
        Team, verbose_name='Time', on_delete=models.CASCADE, null=False
    )

    class Meta:
        verbose_name = 'Membro'
        verbose_name_plural = 'Membros'

    def __str__(self):
        return self.username


class Suggestion(models.Model):
    text = models.CharField(
        verbose_name='Sugestão', max_length=256, null=False
    )
    observations = models.CharField(
        verbose_name='Observações', max_length=512, null=True
    )
    owner = models.ForeignKey(
        Member,
        verbose_name='Nome de usuário',
        on_delete=models.CASCADE,
        null=False,
    )
    category = models.CharField(
        verbose_name='Categoria',
        choices=choices.CATEGORIES,
        max_length=64,
        null=False,
    )
    votes = models.ManyToManyField(
        Member, related_name='member_votes', verbose_name='Votos'
    )

    class Meta:
        verbose_name = 'Sugestão'
        verbose_name_plural = 'Sugestões'

    def vote(self, member: Member):
        self.votes.add(member)

    def __str__(self):
        return f'{self.text} por: {self.owner.username}'


class Review(models.Model):
    goal = models.CharField(
        verbose_name='Observações', max_length=256, null=True
    )
    token = models.UUIDField(
        verbose_name='Token', default=uuid.uuid4, editable=False
    )
    members = models.ManyToManyField(
        Member, related_name='participating', verbose_name='Votos'
    )
    suggestions = models.ManyToManyField(
        Suggestion, related_name='reviews', verbose_name='Votos'
    )
    team = models.ForeignKey(
        Team, verbose_name='Time', on_delete=models.CASCADE, null=True
    )
    created_at = models.DateTimeField(
        verbose_name='Criado em', auto_now_add=True
    )

    class Meta:
        verbose_name = 'Sugestão'
        verbose_name_plural = 'Sugestões'

    def __str__(self):
        return self.goal

    def export(self):
        pass
