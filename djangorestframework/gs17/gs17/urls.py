from rest_framework.routers import DefaultRouter
from  api import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = router.urls