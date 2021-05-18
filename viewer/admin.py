from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Genre, Movie

admin.site.register(Genre)


class MovieAdmin(ModelAdmin):

    @staticmethod
    def released_year(obj):
        return obj.released.year

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description="This description has been cleaned up")

    ordering = ['id']
    list_display = ['id', 'title', 'genre', 'released_year']
    list_per_page = 5
    list_display_links = ['id', 'title']
    list_editable = ['genre']
    list_filter = ['genre']
    search_fields = ['title']
    actions = ['cleanup_description']
    date_hierarchy = 'released'

    fieldsets = [
        (None, {'fields': ['title', 'created']}),
        (
            'External Information',
            {
                'fields' : ['genre', 'released'],
                'description': "These fields are containing information about the movie coming from external resources"
            }
        ),
        (
            'User Information',
            {
                'fields': ['rating', 'description'],
                'description': (
                    "These fields are coming "
                    "from the inputs of the website's user"
                )
            }
        )
    ]
    readonly_fields = ['created']


admin.site.register(Movie, MovieAdmin)
