from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from App.views import * 

urlpatterns = patterns('',

	url(r'^admin/', include(admin.site.urls)),
	
	#Pages
	url(r'^$', home), #Landing Page - login/register
	
	(r'^projects/', include('App.urls')),  ##Points all project urls to the urls in App
	
	#Possible Pages
	#url(r'^projects/name/calendar/$', pCalendar),
	#url(r'^projects/name/progress/$', pProgress),
	
	
	#Andrew Functions
	url(r'^test/$', test), #Test Site
	url(r'^accounts/register/$', register), #Registration Form
	url(r'^accounts/loginRequest/$', login_req),#Logs in User
	url(r'^accounts/login/$', login), #Login Form
	url(r'^accounts/logout/$', logout_req), #Logout Form
	url(r'^accounts/addMember/$',add_member), #Creates New User
	url(r'^createProject/$',project), #New Project Form
	url(r'^accounts/addProject/$',add_project), # Creates new project
	url(r'^accounts/joinProject/$', mem_project), #Form to join an existing project
	url(r'^accounts/joinProjectRequest/$', add_mem_project), #Joins user to existing project
)


