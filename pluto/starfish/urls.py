from starfish import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"suggestions", views.SuggestionViewSet)


urlpatterns = []
urlpatterns += router.urls
