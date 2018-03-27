from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.models import Group
from .serializers import UserSerializer, UserNoPasswordSerializer
from django.http import HttpResponse
import json


from rest_framework.views import APIView
from rest_framework import permissions

from .permissions import *


from django.conf import settings



class UserListCreateView(APIView):
    permission_classes=[permissions.IsAuthenticated, IsAdmin]

    # permission_classes=[permissions.AllowAny]


    def get(self,request, format=None):
        user = User.objects.all()
        serializer = UserNoPasswordSerializer(user, many=True)
        return HttpResponse(json.dumps(serializer.data),content_type='application/json')

    def post(self,request, format=None):
        print("ksdf")
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            msg="success"
            if 'groups' in request.data:
                created_user = User.objects.get(username=serializer.validated_data['username'])

                for each in request.data['groups']:

                    group = Group.objects.get(id=each)
                    created_user.groups.add(group)

        else:
            msg = serializer.errors
            return HttpResponse(json.dumps({'msg':msg}),content_type='application/json',status=500)


        return HttpResponse(json.dumps({'msg':msg}), content_type = 'application/json')

class UserRUDView(APIView):


    permission_classes=[permissions.IsAuthenticated, IsAdmin]
    # permission_classes=[permissions.AllowAny]



    def get(self,request,id,format=None):
        user=User.objects.get(id=id)
        serializer=UserNoPasswordSerializer(user)
        return HttpResponse(json.dumps(serializer.data),content_type='application/json')

    def put(self,request,id,format=None):
        user=User.objects.get(id=id)
        serializer = UserNoPasswordSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            if 'password' in request.data:
                user.set_password(request.data['password'])
                user.save()
            if 'groups' in request.data:
                created_user = User.objects.get(username=user.username)
                created_user.groups.clear()

                for each in request.data['groups']:

                    group = Group.objects.get(id=each)
                    created_user.groups.add(group)

            msg="success"
        else:
            msg = serializer.errors
            return HttpResponse(json.dumps({'msg':msg}),content_type='application/json',status=500)

        return HttpResponse(json.dumps({'msg':msg}),content_type='application/json')

    def delete(self,request,id,format=None):
        user=User.objects.get(id=id)
        user.delete()
        return HttpResponse(json.dumps({'msg':'deleted'}),content_type='application/json')


class GroupListCreateView(APIView):
    permission_classes=[permissions.IsAuthenticated, IsAdmin]
    # permission_classes=[permissions.AllowAny]


    def get(self,request, format=None):
        group = Group.objects.all()
        serializer = GroupSerializer(group, many=True)
        return HttpResponse(json.dumps(serializer.data),content_type='application/json')


class GetUserInfoView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    # permission_classes=[permissions.AllowAny]
    


    def get(self,request,format=None):
        user=request.user
        print(user.username)
        serializer=UserNoPasswordSerializer(user)
        return HttpResponse(json.dumps(serializer.data),content_type='application/json')

