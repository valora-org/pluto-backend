from rest_framework import routers
from starfish import views


router = routers.DefaultRouter()

router.register(r'teams', views.TeamViewSet, basename='team')
router.register(r'members', views.MemberViewSet, basename='member')
router.register(r'reviews', views.ReviewViewSet, basename='review')
