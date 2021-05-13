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
from django.urls import path
from .views import (
    blog_post_detail_view,
    blog_list_view,
    blog_delete_view,
    blog_retrieve_view,
    blog_update_view,
    blog_contact_view,
)

urlpatterns = [
    path("", blog_list_view),
    path("contact/", blog_contact_view),
    path("<slug:post_slug>/", blog_post_detail_view),
    path("<slug:slug>/edit/", blog_update_view),
    path("<slug:slug>/delete/", blog_delete_view),
    path("<slug:slug>/", blog_post_detail_view),
]
