"""try_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import home_page, about_view, contact_view
from searches.views import search_view
from blog.views import blog_create_view

urlpatterns = [
    path("blog/", include("blog.urls")),
    path("btc/", include("BTC.urls")),
    path("chat/", include("chat.urls")),
    path("blog-new/", blog_create_view, name="blog_new"),
    path("search/", search_view),
    path("admin/", admin.site.urls),
    path("", home_page),
    path("about/", about_view),
    path("contact/", contact_view),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)