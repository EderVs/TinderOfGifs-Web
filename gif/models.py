from django.db import models

class Gif(models.Model):
	url = models.URLField()

	def __unicode__(self):
		return self.url

class Vote(models.Model):
	id = models.AutoField(primary_key=True)
	time = models.DateField(auto_now=True)
	Gif = models.ForeignKey(Gif)

	def __unicode__(self):
		return str(self.id)