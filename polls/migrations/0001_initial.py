# Generated by Django 5.1 on 2024-08-30 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('difficulty', models.PositiveSmallIntegerField(default=0)),
                ('reward_point', models.PositiveSmallIntegerField()),
                ('backgroung_image', models.ImageField(upload_to='backgroung_image/')),
                ('challenger_type', models.IntegerField(choices=[(1, 'RESTAURANT'), (2, 'ACTIVITY'), (3, 'STAY'), (4, 'GUIDE'), (5, 'TRANSPORT')])),
                ('challenger_status', models.IntegerField(choices=[(1, 'IN_PROGRESS'), (2, 'COMPLETED'), (3, 'SAVED'), (4, 'OTHER')], default=4)),
                ('description', models.CharField(max_length=500)),
                ('validation_text', models.CharField(max_length=500)),
                ('impact_CO2', models.PositiveSmallIntegerField(default=0)),
                ('impact_water', models.PositiveSmallIntegerField(default=0)),
                ('impact_durable', models.PositiveSmallIntegerField(default=0)),
                ('impact_waste', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('points_cost', models.PositiveSmallIntegerField()),
                ('reward_type', models.IntegerField(choices=[(1, 'FOOD'), (2, 'MAINTAINING'), (3, 'HOUSEHOLD'), (4, 'AWAKENING'), (5, 'MOBILITY'), (6, 'DIGITAL')])),
                ('reduction_type', models.IntegerField(choices=[(1, 'PERCENT'), (2, 'EUROS')], default=2)),
                ('reward_value', models.PositiveSmallIntegerField()),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('reward_text', models.TextField()),
                ('commitment', models.TextField()),
                ('website_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('email_address', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('points', models.PositiveSmallIntegerField(default=0)),
                ('completed_challenge', models.PositiveSmallIntegerField(default=0)),
                ('level', models.PositiveSmallIntegerField(default=1)),
                ('challenges', models.ManyToManyField(blank=True, to='polls.challenge')),
                ('acquired_reward', models.ManyToManyField(blank=True, to='polls.reward')),
            ],
        ),
    ]
