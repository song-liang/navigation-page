from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Link


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_preview', 'weight')
    search_fields = ('name',)

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.icon.url)
        return "无图标"
    # icon_preview.allow_tags = True
    icon_preview.short_description = '图标预览'


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'weight', 'icon_preview')
    list_filter = ('category',)
    search_fields = ('title', 'url')

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.icon.url)
        return "无图标"
    # icon_preview.allow_tags = True
    icon_preview.short_description = '图标预览'
