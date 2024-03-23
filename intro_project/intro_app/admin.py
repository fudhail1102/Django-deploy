from django.contrib import admin
from intro_app import models

# Register your models here.
admin.site.register(models.Topic)
admin.site.register(models.WebPage)
admin.site.register(models.AccessRecord)