from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(NseIndex)
class NseAdmin(admin.ModelAdmin):

    list_display = ['symbol','date','open','high','low','close']