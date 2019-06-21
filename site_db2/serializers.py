from rest_framework import serializers

from site_db2.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class MessagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        field = '__all__'