from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category


def index(request):
    template = 'blog/index.html'
    # Выбираем посты, которые:
    # 1. Опубликованы
    # 2. У которых опубликована категория
    # 3. Дата публикации не в будущем
    post_list = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]  # Берем последние 5

    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    # Получаем пост или 404, если он не существует или скрыт (по тем же
    # 3 условиям)
    post = get_object_or_404(
        Post.objects.filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True
        ),
        pk=pk
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    # Если категория не существует или скрыта — 404
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    # Посты только этой категории с учетом условий публикации
    post_list = Post.objects.filter(
        category=category,
        pub_date__lte=timezone.now(),
        is_published=True
    ).order_by('-pub_date')

    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template, context)
