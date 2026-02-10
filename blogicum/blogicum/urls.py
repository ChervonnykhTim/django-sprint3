from django.urls import include, path

from blog.admin import admin_site

urlpatterns = [
    path('', include('blog.urls', namespace='blog')),
    path('pages/', include('pages.urls', namespace='pages')),
    path('admin/', admin_site.urls),
]
