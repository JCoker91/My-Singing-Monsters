from rest_framework.routers import DefaultRouter
from .views import MonsterViewSet

router = DefaultRouter()
router.register('monster',MonsterViewSet)

urlpatterns = router.urls