# apps/base/admin.py

from django.contrib import admin
from .models import Banner, AboutUs, Index

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')

@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'logo', 'banner', 'twitter', 'facebook', 'github', 'gmail')
    search_fields = ('title', 'description')


