from django.shortcuts import render
from rest_framework import viewsets
from recipes_api import serializers
from recipes_api import models
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecipeSerializer
    queryset = models.Recipe.objects.all()
    permission_classes = ( IsAuthenticated, )
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)