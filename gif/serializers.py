from rest_framework import serializers

from gif.models import Gif, Vote
from gif.relations import GifModelSerializer

class GifSerializer(serializers.Serializer):
	class Meta:
		model = Gif
		fields = ('pk', 'url')

class VoteSerializer(serializers.Serializer):
	class Meta:
		model = Vote
		fields = ('pk', 'time')
	Gif = GifModelSerializer(many=False, read_only=False)