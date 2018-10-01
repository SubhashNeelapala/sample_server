from django.conf.urls import url
from polls import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^login/',views.UserLogin.as_view()),
    url(r'^registration',views.UserRegistration.as_view()),
    url(r'^getallusers',views.GetAllUsers.as_view()),
    url(r'^userbasedlist',views.GetUsers_by_loginUser.as_view()),
    url(r'^userdetails_byname',views.ProfileDetails.as_view()),
    url(r'^update_profile',views.UserProfile.as_view()),
    url(r'^delete_user',views.DeleteUser.as_view()),
    url(r'^csv_download/(?P<uid>[0-9]?)',views.csv_download)
    ]