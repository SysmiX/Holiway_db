# Generated by Django 5.1 on 2024-08-30 12:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_member_acquired_reward_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member_Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.member')),
                ('reward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.challenge')),
            ],
        ),
        migrations.CreateModel(
            name='Member_Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.member')),
                ('reward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.reward')),
            ],
        ),
    ]