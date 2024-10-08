from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Event, Game
from .serializers import EventSerializers, GameSerializer

# Create your views here.
@api_view(['GET'])
def games_list(request):
    if request.method == "GET":
        limit = request.query_params.get('limit', None)

        games = Game.objects.all()

        if limit is not None:
            try:
                limit = int(limit)
                games = games[:limit]
            except ValueError:
                return Response({'error': 'Limit parameter must be an integer'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = GameSerializer(games, context={'request': request}, many = True )

        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def events_list(request):
    if request.method == "GET":
        limit = request.query_params.get('limit', None)

        events = Event.objects.all()

        if limit is not None:
            try:
                limit = int(limit)
                events = events[:limit]
            except ValueError:
                return Response({'error': 'Limit parameter must be an integer'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = EventSerializers(events, context={'request': request}, many = True )

        return Response(serializer.data, status=status.HTTP_200_OK)
