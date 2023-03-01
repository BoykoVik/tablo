from django.contrib import admin
from .models import Slides, Holidays, Runningrow
# Register your models here.
@admin.register(Slides)
class SlidesAdmin(admin.ModelAdmin):
    list_display = ("title", "isactive",)

@admin.register(Holidays)
class HolidaysAdmin(admin.ModelAdmin):
    list_display = ("day", "month",)

@admin.register(Runningrow)
class HolidaysAdmin(admin.ModelAdmin):
    list_display = ("name", "day", "month", "isactive",)