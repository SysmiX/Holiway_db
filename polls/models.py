from django.db import models
from enum import Enum

class Reward_type(Enum):
    FOOD = 1
    MAINTAINING = 2
    HOUSEHOLD = 3
    AWAKENING = 4
    MOBILITY = 5
    DIGITAL = 6

class Reduction_type(Enum):
    PERCENT = 1
    EUROS = 2

class Challenge_status(Enum):
    IN_PROGRESS = 1
    COMPLETED = 2
    SAVED = 3
    OTHER = 4  # not yet selected

class Challenge_type(Enum):
    RESTAURANT = 1
    ACTIVITY = 2
    STAY = 3
    GUIDE = 4
    TRANSPORT = 5

class Challenge(models.Model):
    name = models.CharField(max_length=80)
    difficulty = models.PositiveSmallIntegerField(default=0)
    reward_point = models.PositiveSmallIntegerField()
    backgroung_image = models.ImageField(upload_to='backgroung_image/')

    challenger_type = models.IntegerField(choices=[(tag.value, tag.name) for tag in Challenge_type])
    challenger_status = models.IntegerField(choices=[(tag.value, tag.name) for tag in Challenge_status], default=Challenge_status.OTHER.value)
    description = models.CharField(max_length=500)
    validation_text = models.CharField(max_length=500)

    impact_CO2 = models.PositiveSmallIntegerField(default=0)
    impact_water = models.PositiveSmallIntegerField(default=0)
    impact_durable = models.PositiveSmallIntegerField(default=0)
    impact_waste = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

class Reward(models.Model):
    name = models.CharField(max_length=200)
    points_cost = models.PositiveSmallIntegerField()
    reward_type = models.IntegerField(choices=[(tag.value, tag.name) for tag in Reward_type])
    reduction_type = models.IntegerField(choices=[(tag.value, tag.name) for tag in Reduction_type], default=Reduction_type.EUROS.value)
    reward_value = models.PositiveSmallIntegerField()
    publication_date = models.DateTimeField(auto_now_add=True)

    description = models.TextField()
    reward_text = models.TextField()
    commitment = models.TextField()

    website_link = models.URLField()

    def __str__(self):
        return self.name

class Member(models.Model):
    pseudo = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    registration_date = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    points = models.PositiveSmallIntegerField(default=0)
    completed_challenge = models.PositiveSmallIntegerField(default=0)
    level = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.pseudo
    

class Member_Reward(models.Model): # (list) link reward to a member
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    
class Member_Challenge(models.Model):# (list) link challenge to a member
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    reward = models.ForeignKey(Challenge, on_delete=models.CASCADE)