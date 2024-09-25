from rest_framework import serializers
from .models import Game, Event

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'categories', 'image', 'rating')

class EventSerializers(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = '__all__'
