from django.conf.urls import url, include
from .models import *
from . import views
from rest_framework.views import APIView
from django.http import HttpResponse
import  json

from rest_framework.serializers import(
    ModelSerializer, 
    HyperlinkedIdentityField, 
    SerializerMethodField
    )

from rest_framework import permissions


from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from .permissions import *



class ProductSerializer(DocumentSerializer):
	class Meta:
			model=Product
			# exclude=('date',)
			fields='__all__'
			# fields=['name','price','quantity','date']





class ProductListCreate(APIView):

	# permission_classes=[permissions.AllowAny]
	permission_classes=[permissions.IsAuthenticated, CAN_ACCESS_INVENTORY]


	def get(self,request,format=None):
		products=Product.objects.all()
		serializer=ProductSerializer(products,many=True)
		return HttpResponse(json.dumps(serializer.data),content_type='application/json')

	def post(self,request,format=None):
		print(request.data)
		serializer=ProductSerializer(data=request.data)
		if serializer.is_valid():
		
			serializer.save()
			msg='success'
		else:
			msg=serializer.errors
			return HttpResponse(json.dumps({'msg':msg}),content_type='application/json',status=500)


	
		return HttpResponse(json.dumps({'msg':msg}),content_type='application/json')


class ProductRUD(APIView):

	permission_classes=[permissions.IsAuthenticated, CAN_ACCESS_INVENTORY]

	
	def get(self,request,id,format=None):
		product=Product.objects.get(id=id)
		serializer=ProductSerializer(product)
		print(product.created)
		print(serializer.data)
		return HttpResponse(json.dumps(serializer.data),content_type='application/json')

	def put(self,request,id,format=None):
		product=Product.objects.get(id=id)
		print(request.data)
		serializer = ProductSerializer(product, data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			msg='success'
		else:
			msg=serializer.errors
			
			return HttpResponse(json.dumps({'msg':msg}),content_type='application/json',status=500)

		
		return HttpResponse(json.dumps({'msg':'success'}),content_type='application/json')


	def delete(self,request,id,format=None):
		product=Product.objects.get(id=id)
		product.delete()

		return HttpResponse(json.dumps({'msg':'success'}),content_type='application/json')














urlpatterns = [
	url(r'^products/$',ProductListCreate.as_view()),
	url(r'^products/(?P<id>.+)/$',ProductRUD.as_view()),



	# url(r'^editbooks/(?P<id>.+)/$',views.editbooks,name='editbooks'),


	url(r'^',views.index, name='index'),
]




