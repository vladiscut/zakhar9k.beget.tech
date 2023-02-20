from django.contrib import admin
from .models import *




class PartnersAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('is_published',)
    list_filter = ( 'is_published', 'time_create')
admin.site.register(Partners, PartnersAdmin)

