from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
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
		print(request.user.groups.filter(name='ADMIN').exists())
		return request.user.groups.filter(name='ADMIN').exists()
