from django.db import models
from django.contrib import admin
class Player (models.Model):
    Playerid=models.CharField(max_length=20,help_text="Player ID")
    name=models.CharField(max_length=100)
    goals=models.IntegerField()
    age=models.IntegerField()
    email =models.EmailField()
    number=models.IntegerField()

class PlayerAdmin(admin.ModelAdmin):
    list_display=('Playerid','name','goals','age','email','number')


