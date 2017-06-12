from django.db import models
from projects.models import Project, Reward
from django.contrib.auth.models import User



class Input(models.Model):
	amount = models.DecimalField(decimal_places=2,  max_digits=9)
	project = models.ForeignKey(Project, related_name='inputs')
	user = models.ForeignKey(User, related_name='inputs')
	date = models.DateTimeField(auto_now=True)
	reward = models.ForeignKey(Reward, related_name='inputs')
	paid = models.BooleanField(default=False)


