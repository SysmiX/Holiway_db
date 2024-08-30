from django.contrib import admin

# Register your models here.

from .models import Member, Challenge, Reward, Member_Reward, Member_Challenge

admin.site.register(Member)
admin.site.register(Challenge)
admin.site.register(Reward)
admin.site.register(Member_Reward)
admin.site.register(Member_Challenge)