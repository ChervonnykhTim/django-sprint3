from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import Category, Location, Post


class MyAdminSite(AdminSite):
    site_header = 'Администрирование Блога'
    site_title = 'Мой сайт администрирования'
    index_title = 'Добро пожаловать в админ-панель'


admin_site = MyAdminSite()


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'author',
        'category',
        'location',
        'is_published',
    )
    list_editable = (
        'is_published',
        'category',
    )
    search_fields = ('title', 'text')


@admin.register(Category, site=admin_site)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published',)
    list_editable = ('is_published',)


@admin.register(Location, site=admin_site)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published',)
    list_editable = ('is_published',)
