from rest_framework.routers import DefaultRouter
from .views import MasterViewSet, SubsidiaryViewSet, PersonViewSet



router = DefaultRouter()

router.register('masters', MasterViewSet,basename='master')
router.register(r'subsidiaries', SubsidiaryViewSet, basename='subsidiary')
router.register(r'persons', PersonViewSet, basename='person')
urlpatterns = router.urls

