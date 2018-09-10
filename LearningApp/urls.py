from django.conf.urls import url
from . import views
from django.conf.urls import include

app_name = 'LearningApp'


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    url(r'^courses/$', views.v_courses, name='v_courses'),
    url(r'^courses/(?P<course_id>[0-9]+)/$', views.course_detail, name='course_detail'),

    url(r'^discussions/$', views.v_discussion, name='v_discussion'),
    url(r'^discussions/(?P<discussion_id>[0-9]+)/$', views.discussion_detail, name='discussion_detail'),


    # Profile
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^profile/change-password/$', views.change_password, name='change_password'),

]
