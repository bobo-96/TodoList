from rest_framework import serializers

from tasks.models import Task
from user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class TaskSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('owner',)

    def get_category_name(self, obj):
        return obj.category.title

    def create(self, validated_data):
        user = self.context.get('request').user

        task = Task.objects.create(owner=user, **validated_data)
        return task
