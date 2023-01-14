from rest_framework import serializers
from recipes_api import models

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recipe
        fields = ('id', 'author', 'title', 'description', 'created_on')
        extra_kwargs = {
            'user_profile': {
                'read_only': True
            }
        }