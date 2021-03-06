"""car_review_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from main_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('add_car/', views.add_car),
    path('add_review/', views.add_review),
    path('<str:pk>/delete_review/', views.delete_review, name='delete'),
    path('view_cars/',views.view_cars),
    path('<str:pk>/modify_review/',views.modify, name='modify'),
    path('all_reviews/',views.all_reviews, name='all_reviews'),
    path('view_cars/<str:pk>',views.view_reviews, name='review'),
    ]
