from rest_framework import serializers
from gif.models import Gif


class GifModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Gif
		fields = ('pk', 'url')
