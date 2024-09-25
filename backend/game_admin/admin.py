from django.contrib import admin
from .models import Game, Category, Contact, Event

# Register your models here.
admin.site.register(Category)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created"

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "location", "startDate", "endDate"]
