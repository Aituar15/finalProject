from django.contrib import admin
from .models import Word
# Register your models here.


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ("title", "definition", "language")
    search_fields = ("title", "definition", "language")
