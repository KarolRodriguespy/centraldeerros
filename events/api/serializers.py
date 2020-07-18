from rest_framework import serializers

from events.models import Event


class EventModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'user', 'level', 'environment', 'address', 'log', 'date', 'archive', 'count_events']
