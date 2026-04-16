from django.contrib import admin

# Register your models here.

from .models import Agenda

admin.site.register(Agenda)

from .models import Local
admin.site.register(Local)