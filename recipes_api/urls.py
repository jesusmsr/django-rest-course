from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipes_api import views

router = DefaultRouter()
router.register('', views.RecipeViewSet)
