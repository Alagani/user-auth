from django.contrib import admin

# Register your models here.
# admin.py for custom model
# from django.contrib import admin
from .models import SignUp

admin.site.register(SignUp)
