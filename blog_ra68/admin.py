from django.contrib import admin
from .models import Post, Category, MenuItem

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'publish_date')
    list_filter = ('status', 'category', 'publish_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('publish_date', 'updated_date')
    autocomplete_fields = ('author',)
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author', 'category', 'status', 'featured_image', 'excerpt', 'content')
        }),
        ('Dates', {
            'fields': ('publish_date', 'updated_date'),
            'classes': ('collapse',)
        }),
    )



# menu/admin.py
from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'order', 'named_url', 'url')
    list_editable = ('order',)  # Only 'order' exists and is editable
    search_fields = ('title', 'named_url', 'url')
    list_filter = ('parent',)
    ordering = ('order',)

    # Optional: Improve UX
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('parent')
