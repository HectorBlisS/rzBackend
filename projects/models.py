from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
	author = models.ForeignKey(User, related_name='projects')
	name = models.CharField(max_length=140)
	goal = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
	description = models.TextField(null=True, blank=True)
	created = models.DateTimeField(null=True, blank=True)
	publish = models.DateTimeField(null=True, blank=True)
	finish = models.DateTimeField(null=True, blank=True)
	photo = models.ImageField(blank=True, null=True)
	reached = models.DecimalField(decimal_places=2,  max_digits=6, null=True, blank=True)
	video = models.URLField(null=True, blank=True)
	followers = models.ManyToManyField(User, related_name='following', blank=True)
	validated = models.BooleanField(default=False)


	def __str__(self):
		return self.name

class Reward(models.Model):
	project = models.ForeignKey(Project, related_name='rewards')
	title = models.CharField(max_length=140)
	description = models.CharField(max_length=240)
	amount = models.DecimalField(decimal_places=2, max_digits=6)

	def __str__(self):
		return "{} de {}".format(self.title, self.project)

