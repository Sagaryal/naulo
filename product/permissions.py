from rest_framework.permissions import BasePermission, SAFE_METHODS


class CAN_ACCESS_INVENTORY(BasePermission):
	message = 'You dont have  permission '
	# my_safe_methods = ['GET', 'PUT']
	my_safe_methods = []


	def has_permission(self,request,view):
		# if request.method in self.my_safe_methods:
		# 	return True
		
		# else:
		# 	return(request.user.has_perm('global_permissions.can_create_product'))

		# if request.method=='GET':
		# 	return (request.user.has_perm('global_permissions.product_retrieve'))

		# else:
		# 	return ((request.user.has_perm('global_permissions.product_create')))

		print("yoyokoiko")
		return request.user.has_perm('global_permissions.CAN_ACCESS_INVENTORY')


# class CanRetrieveOrUpdateOrDestroy(BasePermission):
# 	message = 'You dont have  permission '
# 	# my_safe_methods = ['GET', 'PUT']
# 	# my_safe_methods = ['GET']


# 	def has_permission(self,request,view):
# 		if request.method == 'GET' :
# 			return (request.user.has_perm('global_permissions.product_retrieve'))
# 		elif request.method == 'PUT':
# 			return (request.user.has_perm('global_permissions.product_update'))
# 		else:
# 			return(request.user.has_perm('global_permissions.product_delete'))

		




		


	# def has_object_permission(self,request,view, obj):
		
	# 	print('yo')
	# 	try:
	# 		return obj.user == request.user
	# 	except:
	# 		try:
				
	# 			print(obj.route.school.user.username)
	# 			return obj.route.school.user==request.user
	# 		except:
	# 			try:
	# 				return obj.bus.route.school.user==request.user
	# 			except:
	# 				return obj.school.user==request.user