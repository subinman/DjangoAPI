"""
URL configuration for gs13 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentListApi/', views.StudentList.as_view()),
    path('studentCreateApi/', views.StudentCreate.as_view()),
    path('studentRetriveApi/<int:id>/', views.StudentRetrieve.as_view(), name='student-retrieve'),
     path('studentUpdateApi/<int:id>/', views.StudentUpdate.as_view(), name='student-update'),
      path('studentdeleteApi/<int:id>/', views.StudentDelete.as_view(), name='student-delete'),
]
