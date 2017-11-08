from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
	name = models.CharField(max_length=140)
	slug = models.SlugField(max_length=250)


	def __str__(self):
		return self.name





class Project(models.Model):
	STATUSCHOICES = (
			('editing', 'Editando'),
			('review', 'Revisando'),
			('rejected', 'Rechazado'),
			('approved', 'Aprobado')
		)

	author = models.ForeignKey(User, related_name='projects')
	photoURL = models.URLField(null=True, blank=True)
	name = models.CharField(max_length=140)
	slug = models.SlugField(max_length=240, null=True, blank=True)
	goal = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)
	description = models.TextField(null=True, blank=True)
	created = models.DateTimeField(null=True, blank=True)
	publish = models.DateTimeField(null=True, blank=True)
	finish = models.DateTimeField(null=True, blank=True)
	photo = models.URLField(max_length=500,blank=True, null=True)
	reached = models.DecimalField(decimal_places=2,  max_digits=6, null=True, blank=True)
	video = models.URLField(null=True, blank=True)
	followers = models.ManyToManyField(User, through="Follow", blank=True, symmetrical=False)
	validated = models.BooleanField(default=False)
	status = models.CharField(max_length=140, default="editing", choices=STATUSCHOICES)
	category = models.ManyToManyField(Category, related_name='projects', null=True, blank=True)
	summary = models.CharField(max_length=140, 	blank=True, null=True)
	destacado = models.BooleanField(default=False)


	def __str__(self):
		return self.name

	def set_default_category(self):
		return Category.objects.all().filter(name='salud')




class Follow(models.Model):
	user_from = models.ForeignKey(User, related_name='rel_from_set')
	project = models.ForeignKey(Project, related_name='rel_to_set')
	created = models.DateTimeField(auto_now_add=True, db_index=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return '{} sigue a {}'.format(self.user_from, self.project)




class Reward(models.Model):
	project = models.ForeignKey(Project, related_name='rewards')
	title = models.CharField(max_length=140)
	description = models.CharField(max_length=240)
	amount = models.DecimalField(decimal_places=2, max_digits=8)
	date = models.DateField(blank=True, null=True)
	quantity = models.IntegerField(blank=True, null=True)



	def __str__(self):
		return "{} de {}".format(self.title, self.project)


class Observaciones(models.Model):
	project = models.ForeignKey(Project, related_name="observation")
	text = models.TextField()

	def __str__(self):
		return "observation of {}".format(self.project)

class Updates(models.Model):
	project = models.ForeignKey(Project, related_name='updates', null=True)
	author = models.ForeignKey(User, related_name='updater', null=True)
	update = models.CharField(max_length=140, null=True, blank=True)
	image = models.URLField(max_length=1000, null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True, db_index=True, null=True, blank=True)

	def __str__(self):
		return "update of {}".format(self.project)

