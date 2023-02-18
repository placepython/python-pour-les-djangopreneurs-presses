"""config URL Configuration."""
from django.contrib import admin
from django.urls import path
from blog.views import home, nouvelle_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("autre/", nouvelle_page, name="nouvelle_page"),
]
