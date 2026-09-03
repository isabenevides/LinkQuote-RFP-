from rest_framework.routers import DefaultRouter
from .views import RFPViewSet

router = DefaultRouter()
router.register('rfps', RFPViewSet, basename= 'rfp')

urlpatterns= router.urls