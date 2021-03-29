from rest_framework import serializers

from categories.models import Category
from user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('owner',)

    def create(self, validated_data):
        user = self.context.get('request').user

        category = Category.objects.create(owner=user, **validated_data)
        return category
