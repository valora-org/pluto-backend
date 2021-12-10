from django.urls import path, include
from starfish.routes import router


urlpatterns = [
    path('api/', include(router.urls))
]
