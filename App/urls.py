from django.conf.urls import patterns, include, url

#url(r'^xxx/(?P<param>\d+)/$', 'enter.view.here')  
#?P=Parameter/<param>=Called parameter/d+=Regex for type int(d), of any size(+)

urlpatterns = patterns('', 
	url(r'^$', 'App.views.projects'), #Project Hub
	url(r'^(?P<prname>[^/]+)/$',  'App.views.pName'), #Individual Home Page + Chat
	url(r'^(?P<prname>[^/]+)/tasks/$', 'App.views.pTask'),		#Project Tasks/Deadlines
	url(r'^(?P<prname>[^/]+)/addTask/$', 'App.views.addTask'),		#Add task to description	
	) #pname is passed to App.view.test