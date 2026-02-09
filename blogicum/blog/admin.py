from django.contrib import admin
from .models import Category, Location, Post


admin.site.site_header = 'Администрирование Блога'
admin.site.site_title = 'Мой сайт администрирования'
admin.site.index_title = 'Добро пожаловать в админ-панель'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author', 'category', 'location',
                    'is_published')
    list_editable = ('is_published', 'category')
    search_fields = ('title', 'text')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published',)
    list_editable = ('is_published',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published',)
    list_editable = ('is_published',)
