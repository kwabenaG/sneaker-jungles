from django.contrib import admin
from .models import CustomUser, UserProfile


# create custom admin levels here


# Register your models here.
admin.site.register(CustomUser),
admin.site.register(UserProfile)