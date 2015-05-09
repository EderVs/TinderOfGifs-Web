from django.contrib import admin

from gif.models import Gif, Vote


class GifAdmin(admin.ModelAdmin):
	list_display = ['pk', 'url']
	search_fields = ['pk', 'url']

class VoteAdmin(admin.ModelAdmin):
	list_display = ['pk', 'time']

admin.site.register(Gif, GifAdmin)
admin.site.register(Vote, VoteAdmin)
