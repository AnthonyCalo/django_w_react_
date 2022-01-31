from rest_framework import routers
from .api import PersonViewSet, LeadsViewSet

router = routers.DefaultRouter()
router.register('api/leads', PersonViewSet, 'persons')
router.register('leads/api', LeadsViewSet, 'persons')

urlpatterns = router.urls