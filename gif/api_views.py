from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic import View

from gif.serializers import GifSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from gif.models import Gif, Vote

import json


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class AllGifsView(View):
	def get(self, request):
		gifs = Gif.objects.all()
		gifs_to_show = []
		for gif in gifs:
			votes = len(Vote.objects.filter(Gif=gif))
			gifs_to_show.append({'url': gif.url, 'votes': votes})
		return JSONResponse(gifs_to_show)