from rest_framework.serializers import(
	ModelSerializer)
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.models import Group
from django.conf import settings
from rest_framework.response import Response





class UserSerializer(ModelSerializer):
	username = serializers.CharField(
				required=True,
				validators=[UniqueValidator(queryset=User.objects.all())] 
				)

	password = serializers.CharField(min_length=8)
	# group = serializers.SerializerMethodField()
	
	def create(self, validated_data):
		
		user = User.objects.create_user(username=validated_data['username'],
             password=validated_data['password'])
		if 'email' in validated_data:
			user.email=validated_data['email']
		if 'first_name' in validated_data:
			user.first_name=validated_data['first_name']
		if 'last_name' in validated_data:
			user.last_name=validated_data['last_name']
		user.save()
		return user

	class Meta:
		model = User
		fields='__all__'
		read_only_fields = ('id',)
		write_only_fields = ('password',)



class UserNoPasswordSerializer(ModelSerializer):

	permissions = serializers.SerializerMethodField()
	groups=serializers.SerializerMethodField()

	class Meta:
		model = User
		exclude=('password','user_permissions')
		read_only_fields = ('id',)

	def get_permissions(self,obj):
		result=[]
		# for each in obj.get_group_permissions():
		# 	print(each)
			# result.append(each.id)
		for each in obj.groups.all():
			for eaches in each.permissions.all():
				result.append({'id':eaches.id,'name':eaches.name})
		return result

	def get_groups(self,obj):
		result=[]
		for each in obj.groups.all():
			result.append({'id':each.id,'name':each.name})
		return result







