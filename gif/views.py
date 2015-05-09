from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic import View

from gif.models import Gif, Vote

# Create your views here.
class AllGifsView(View):
	def get(self, request):
		gifs = Gif.objects.all()
		gifs_to_show = []
		for gif in gifs:
			votes = len(Vote.objects.filter(Gif=gif))
			gifs_to_show.append({'url': gif.url, 'votes': votes})
		context = {
			'gifs': gifs_to_show,
		}
		return render(request, "gif/all_gifs.html", context)