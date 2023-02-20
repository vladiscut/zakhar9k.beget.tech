from django.contrib import admin
from about_fond.models import *




class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_fond')
    list_editable = ('is_fond',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('time_create',)

admin.site.register(DocumentsFond, DocumentsAdmin)

