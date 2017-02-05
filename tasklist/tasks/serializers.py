from rest_framework import serializers
from .models import Task, status_list

from django.http import HttpResponse

from rest_framework.views import APIView



class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=False, max_length=140)
    description = serializers.CharField(required=False, allow_blank=True)
    done = serializers.CharField(required=False)
    created_by = serializers.CharField(required=False)
    amended_by = serializers.CharField(required=False)
    ordering_fields = ('created_by')

    # current_user = serializers.SerializerMethodField('_user', required=False)
    #
    # def _user(self, obj):
    #     user = self.context['request'].user.username
    #     return user

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        # self.created_by =  self.context['request'].user.username
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Task` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.done = validated_data.get('done', instance.done)
        instance.amended_by = validated_data.get('amended_by', instance.amended_by)
        instance.save()
        return instance







class UserSerializer(serializers.Serializer):
    user = serializers.CharField(required=False)
    username = serializers.CharField(required=False, allow_blank=False, max_length=140)

    def get_serializer_context(self):
        return {'request': self.request}
