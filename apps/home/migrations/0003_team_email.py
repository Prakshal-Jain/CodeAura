# Generated by Django 3.1.5 on 2021-01-19 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_team_contribution'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='email',
            field=models.EmailField(default='codeaurahelpdesk@gmail.com', max_length=254, verbose_name='Email'),
        ),
    ]