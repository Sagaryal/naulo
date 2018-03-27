from django.db import models
from mongoengine import Document,StringField,FloatField,IntField,DateTimeField,signals
import datetime



# Create your models here.

from datetime import date




class Product(Document):
	# name=models.CharField(max_length=100)
	# price=models.FloatField()	
	# quantity=models.IntegerField()
	# date = models.DateField(blank=True,null=True)


	# def __str__(self): 
	# 	return self.name

	name = StringField(required=True,unique=True,max_length=100)
	price = FloatField()
	quantity = IntField()
	date = DateTimeField()
	created=DateTimeField()
	updated=DateTimeField()


	def save(self,*args,**kwargs):
		if not self.id:
			self.created=self.updated=datetime.datetime.now()
		else:
			self.updated=datetime.datetime.now()
		super(Product,self).save(args,kwargs)
		


# 	@classmethod
# 	def post_save(cls, sender, document, **kwargs):
# 		# print("Post Save Called")
# 		# print(document.billNo)
# 		# print(document.table)
# 		# print(document.payment_option)
# 		if not document
# 		if not (document.updated):
# 			document.update(updated=document.created)
# 		else:
# 			document.update(updated=datetime.datetime.now())
# 		print(datetime.datetime.now())


# signals.post_save.connect(Product.post_save, sender=Product)

















