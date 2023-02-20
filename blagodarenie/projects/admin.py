from django.contrib import admin
from .models import *




class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('is_published',)
    list_filter = ( 'is_published', 'time_create')
    prepopulated_fields = {'slug': ("title",)}
admin.site.register(Projects, ProjectsAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'project_id',  'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('is_published',)
    list_filter = ( 'is_published', 'time_create')
    prepopulated_fields = {'slug': ("title",)}
    prepopulated_fields = {'slug': ("title",)}
admin.site.register(News, NewsAdmin)

class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('id','project_id', 'title', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('time_create',)
admin.site.register(Documents, DocumentsAdmin)
