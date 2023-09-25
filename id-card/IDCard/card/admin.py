from django.contrib import admin
from .models import Card


@admin.register(Card)
class QuestionAdmin(admin.ModelAdmin):
    list_filter = ('first_name','last_name','card_id', 'father_name', 'birth_data', 'expiration_data')
    search_fields = ('first_name','last_name','card_id', 'father_name', 'birth_data', 'expiration_data')
    list_display = (
        'first_name',
        'last_name',
        'card_id',
        'father_name',
        'birth_data',
        'expiration_data'
    )