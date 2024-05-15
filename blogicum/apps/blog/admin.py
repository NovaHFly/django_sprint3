# Register your models here.
from django.contrib import admin

import blog.models


class PostInline(admin.StackedInline):
    model = blog.models.Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
    )
    list_display_links = ('title',)
    list_editable = ('is_published',)
    search_fields = ('title',)
    inlines = (PostInline,)


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
    )
    list_display_links = ('name',)
    list_editable = ('is_published',)
    search_fields = ('name',)
    inlines = (PostInline,)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'is_published',
        'pub_date',
        'category',
        'location',
    )
    list_display_links = ('id', 'title')
    list_editable = ('is_published', 'category', 'location')
    list_filter = ('category', 'location')
    search_fields = ('title', 'text')


admin.site.register(blog.models.Category, CategoryAdmin)
admin.site.register(blog.models.Location, LocationAdmin)
admin.site.register(blog.models.Post, PostAdmin)
