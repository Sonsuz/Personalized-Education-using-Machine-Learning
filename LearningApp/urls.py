from django.conf.urls import url
from . import views
from django.conf.urls import include

app_name = 'LearningApp'


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),




    # Profile
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^profile/change-password/$', views.change_password, name='change_password'),

]
