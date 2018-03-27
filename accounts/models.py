from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.core import serializers
from django.forms.models import model_to_dict

from mongoengine import Document, IntField, StringField
# assuming obj is your model instance

class MongoUser(Document):
	userid=IntField()
	username=StringField()
	first_name=StringField()
	last_name=StringField()



#additional fields required for User class
class User(AbstractUser):
	bio = models.TextField(max_length=500, default="Give your Bio")


	@staticmethod
	def post_save(sender, **kwargs):
		# print(kwargs)
		# print(sender)
		instance=kwargs.get('instance')

		try:
			u=MongoUser.objects.get(userid=instance.id)
			u.username=instance.username
			u.first_name= instance.first_name
			u.last_name=instance.last_name
			u.save()
		except:
			u=MongoUser(userid=instance.id,username=instance.username,first_name=instance.first_name,last_name=instance.last_name)

			u.save()
			


		# print(instance.username)
		# print(instance.password)
		# try:
		# 	print(instance.first_name)
		# 	print(instance.last_name)
		# 	print(instance.groups)
		# except:
		# 	pass

		# print(instance)
	
		# print(instance)




post_save.connect(User.post_save, sender=User)









