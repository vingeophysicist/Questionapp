# Generated by Django 4.2 on 2023-05-04 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionapp', '0004_alter_question_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='coins_given',
            field=models.PositiveSmallIntegerField(choices=[(10, 10), (20, 20), (30, 30), (40, 40), (50, 50), (60, 60), (70, 70), (80, 80), (90, 90), (100, 100)], default=10),
        ),
    ]
