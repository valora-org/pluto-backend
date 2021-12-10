# Generated by Django 3.2.10 on 2021-12-10 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='Nome de usuário')),
            ],
            options={
                'verbose_name': 'Membro',
                'verbose_name_plural': 'Membros',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Time',
                'verbose_name_plural': 'Times',
            },
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256, verbose_name='Sugestão')),
                ('observations', models.CharField(max_length=512, null=True, verbose_name='Observações')),
                ('category', models.CharField(choices=[('keep-doing', 'Continuar fazendo'), ('start-doing', 'Começar a fazer'), ('stop-doing', 'Parar de fazer'), ('less-of', 'Fazer menos'), ('more-of', 'Fazer mais')], max_length=64, verbose_name='Categoria')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='starfish.member', verbose_name='Nome de usuário')),
                ('votes', models.ManyToManyField(related_name='member_votes', to='starfish.Member', verbose_name='Votos')),
            ],
            options={
                'verbose_name': 'Sugestão',
                'verbose_name_plural': 'Sugestões',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(max_length=256, verbose_name='Observações')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('members', models.ManyToManyField(related_name='participating', to='starfish.Member', verbose_name='Votos')),
                ('suggestions', models.ManyToManyField(related_name='reviews', to='starfish.Suggestion', verbose_name='Votos')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='starfish.team', verbose_name='Time')),
            ],
            options={
                'verbose_name': 'Sugestão',
                'verbose_name_plural': 'Sugestões',
            },
        ),
        migrations.AddField(
            model_name='member',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='starfish.team', verbose_name='Time'),
        ),
    ]
