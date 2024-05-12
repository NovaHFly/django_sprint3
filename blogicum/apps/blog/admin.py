# Register your models here.
from django.contrib import admin

from blog.models import BlogPost, Category


class BlogPostInline(admin.StackedInline):
    model = BlogPost
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (BlogPostInline,)
    list_display = ('title',)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('is_published', 'date', 'location', 'category')
    list_editable = ('is_published', 'category',)
    search_fields = (
        'text',
        'location',
    )
    list_filter = ('category',)
    list_display_links = ('date',)
    empty_value_display = 'Не задано'


admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
