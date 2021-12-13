# Generated by Django 3.2.10 on 2021-12-10 19:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('starfish', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='token',
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, verbose_name='Token'),
        ),
        migrations.AlterField(
            model_name='review',
            name='goal',
            field=models.CharField(
                max_length=256, null=True, verbose_name='Observações'),
        ),
    ]