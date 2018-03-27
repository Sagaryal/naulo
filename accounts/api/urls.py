from django.conf.urls import url
from .views import UserListCreateView, UserRUDView, GroupListCreateView,GetUserInfoView


urlpatterns = [

    url(r'^user/$',UserListCreateView.as_view()),
	url(r'^user/(?P<id>.+)/$',UserRUDView.as_view()),
	url(r'^group/$',GroupListCreateView.as_view()),
	url(r'^getuserinfo/$',GetUserInfoView.as_view()),

]