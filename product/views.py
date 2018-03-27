from django.shortcuts import render
from django.http import HttpResponse
from global_permissions.models import GlobalPermission
from accounts.models  import User
from django.contrib.auth.models import Group


# Create your views here.


def index(request):

	permissions_set = [
   'CAN_ADD_USER',
   'CAN_VIEW_USERS',
   'CAN_VIEW_GROUPS',
   'CAN_VIEW_PERMISSIONS',
   'CAN_ACCESS_FOOD_CATEGORY',
   'CAN_ACCESS_FOOD_ITEM',
   'CAN_ACCESS_INVENTORY',
   'CAN_ACCESS_BILL'

];

	try:
		g=Group.objects.get(name='ADMIN')
	except:
		g=Group.objects.create(name='ADMIN')


	for each in permissions_set:

		try:

			gl=GlobalPermission.objects.get( codename=each)

		except:
			gl=GlobalPermission.objects.create(name=each, codename=each)

		g.permissions.add(gl)

	try:
		# pass
		u=User.objects.create_user(username='paaila',password='asdf1234')
	
		u.groups.add(g)
	except:
		pass







	# print("k")
	# u=User.objects.get(username='leomessi')
	# print("K")
	# g=Group.objects.get(name='manager')
	# print("k")



	# try:

	# 	gl=GlobalPermission.objects.get( codename='product_create')

	# except:
	# 	gl=GlobalPermission.objects.create(name='product_create', codename='product_create')

	# g.permissions.add(gl)



	# try:

	# 	gl=GlobalPermission.objects.get( codename='product_retrieve')

	# except:
	# 	gl=GlobalPermission.objects.create(name='product_retrieve', codename='product_retrieve')

	# g.permissions.add(gl)



	# try:

	# 	gl=GlobalPermission.objects.get( codename='product_update')

	# except:
	# 	gl=GlobalPermission.objects.create(name='product_update', codename='product_update')


	# g.permissions.add(gl)



	# try:

	# 	gl=GlobalPermission.objects.get( codename='product_delete')

	# except:
	# 	gl=GlobalPermission.objects.create(name='product_delete', codename='product_delete')














	# g.permissions.add(gl)
	# print("k")
	# print(u.get_group_permissions())
	# print("k")


	return HttpResponse('sdfsdafas')