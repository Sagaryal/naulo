

from django.conf.urls import include, url

from rest_framework.views import APIView
from django.http import HttpResponse
import  json
from rest_framework import permissions
from django.contrib.auth.models import Group
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from global_permissions.models import GlobalPermission
from accounts.models import User
from accounts.api.permissions import IsAdmin


class GroupSerializer(ModelSerializer):
	permissions = SerializerMethodField()

	class Meta:
		model=Group
		fields=['id','name','permissions']

	def get_permissions(self,obj):
		result=[]
		for each in obj.permissions.all():
			result.append({'id':each.id,'name':each.name})
		return result



class GroupPutSerializer(ModelSerializer):

	class Meta:
		model=Group
		fields=['id','name']



class GlobalPermissionSerializer(ModelSerializer):
	class Meta:
		model=GlobalPermission
		fields=['id','codename']




class GroupListCreate(APIView):
	permission_classes=[permissions.IsAuthenticated, IsAdmin]
	# permission_classes=[permissions.AllowAny]


	def get(self,request,format=None):
		groups=Group.objects.all()
		serializer=GroupSerializer(groups,many=True)
		return HttpResponse(json.dumps(serializer.data),content_type='application/json')


	def post(self,request,format=None):
		serializer=GroupPutSerializer(data=request.data)
		if serializer.is_valid():
		
			serializer.save()
			msg='success'
			status_code=200
		else:
			msg=serializer.errors
			print(serializer.data)
			status_code=500
	
		return HttpResponse(json.dumps({'msg':msg}),content_type='application/json',status=status_code)


class GroupRUD(APIView):
	permission_classes=[permissions.IsAuthenticated, IsAdmin]
	# permission_classes=[permissions.AllowAny]


	def get(self,request,id,format=None):
		group=Group.objects.get(id=id)
		serializer=GroupSerializer(group)
		return HttpResponse(json.dumps(serializer.data),content_type='application/json')


	def put(self,request,id,format=None):
		group=Group.objects.get(id=id)
		serializer = GroupPutSerializer(group, data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			msg='success'
		else:
			msg=serializer.errors
			return HttpResponse(json.dumps({'msg':msg}),content_type='application/json',status=500)

		
		return HttpResponse(json.dumps({'msg':'rud sucess'}),content_type='application/json')



	def delete(self,request,id,format=None):
		group=Group.objects.get(id=id)
		group.delete()

		return HttpResponse(json.dumps({'msg':'delete sucess'}),content_type='application/json')



# class DeLinkPermission(APIView):
# 	permission_classes=[permissions.IsAuthenticated, IsAdmin]
# 	# permission_classes=[permissions.AllowAny]


# 	def post(self,request,format=None):
# 		gl=GlobalPermission.objects.get(id=request.data['global_permission'])
# 		g=Group.objects.get(id=request.data['group_id'])
# 		g.permissions.remove(gl)
# 		return HttpResponse(json.dumps({'msg':'sucess'}),content_type='application/json')



class EditPermission(APIView):
	permission_classes=[permissions.IsAuthenticated, IsAdmin]
	# permission_classes=[permissions.AllowAny]


	def post(self,request,format=None):
		gl=GlobalPermission.objects.get(id=request.data['global_permission'])
		g=Group.objects.get(id=request.data['group_id'])
		if (request.data['checked']):

			g.permissions.add(gl)
		else:
			g.permissions.remove(gl)

		return HttpResponse(json.dumps({'msg':'sucess'}),content_type='application/json')




class ListPermissions(APIView):
	permission_classes=[permissions.IsAuthenticated, IsAdmin]

	# permission_classes=[permissions.AllowAny]


	def get(self,request,format=None):
		gls=GlobalPermission.objects.all()
		serializer=GlobalPermissionSerializer(gls,many=True)

		
		return HttpResponse(json.dumps(serializer.data),content_type='application/json')





























urlpatterns = [
	# url(r'^products/$',ProductListCreate.as_view()),
	# url(r'^products/(?P<id>.+)/$',ProductRUD.as_view()),



	# # url(r'^editbooks/(?P<id>.+)/$',views.editbooks,name='editbooks'),


	# url(r'^',views.index, name='index'),

	url(r'^group/$',GroupListCreate.as_view()),



	url(r'^group/(?P<id>.+)/$',GroupRUD.as_view()),






	url(r'^editpermission/$',EditPermission.as_view()),

	# url(r'^delinkpermission/$',DeLinkPermission.as_view()),


	url(r'^listpermissions/$',ListPermissions.as_view())
]





