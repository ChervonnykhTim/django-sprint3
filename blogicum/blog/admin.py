from django.contrib import admin

from .models import Category, Location, Post

# Настройка заголовка админ-панели (опционально, для красоты)
admin.site.site_header = 'Администрирование Блога'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Список полей, которые будут отображаться в таблице всех постов
    list_display = (
        'title',
        'pub_date',
        'author',
        'category',
        'location',
        'is_published',
    )
    # Поля, которые можно редактировать прямо в списке
    list_editable = (
        'is_published',
        'category',
    )
    # Поля, по которым можно искать посты
    search_fields = ('title', 'text')
    # Фильтры справа
    list_filter = ('category', 'is_published', 'pub_date')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'is_published',
    )
    list_editable = ('is_published',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
    )
    list_editable = ('is_published',)
