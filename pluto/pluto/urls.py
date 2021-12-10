from django.contrib import admin
from django.urls import path, include
import starfish.urls


urlpatterns = [
    path("api/", include(starfish.urls)),
    path("admin/", admin.site.urls),
]
