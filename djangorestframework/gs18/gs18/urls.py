from rest_framework.routers import DefaultRouter
from api import views
from django.urls import path, include
from django.contrib import admin


router = DefaultRouter()
router.register(r'studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]