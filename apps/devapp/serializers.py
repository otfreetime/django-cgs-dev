from unicodedata import category
from rest_framework import serializers
from .models import CodesModel,CategoriesModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesModel
        fields = '__all__'

class CodesSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = CodesModel
        fields = '__all__'
