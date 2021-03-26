from rest_framework import serializers

from tasks.models import Task
from user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class TaskSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user

        category = Task.objects.create(owner=user, **validated_data)
        return category
