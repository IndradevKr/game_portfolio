from django.contrib import admin
from .models import Game, Category, Contact

# Register your models here.
admin.site.register(Category)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
