from django.urls import path
from .views import companyListCreateView

urlpatterns = [
    path('posts/', companyListCreateView.as_view(), name='company-list-create'),
]