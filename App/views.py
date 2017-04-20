from django.shortcuts import render, render_to_response,RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.defaulttags import csrf_token
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django import forms

from App.models import *
from App.forms import *



''' PAGES '''

#Landing page - Includes Registration and Login forms
def home(request):
	return render(request,'home.html')
	
###########################Test Site#########################################
def test(request):
	return render(request)
#############################################################################
	
#Individual Project Homepage - Includes Group Chat and Overview of Deadlines
@login_required	
def pName(request, prname='test'):
	##Get Project name 

	cur_user = request.user #get cur user
	uID = cur_user.id
	
	#Get user<----->project profiles
	up = list(ProjectProfile.user.through.objects.all())
	
	name = ProjectProfile.objects.get(pname = prname)
	pAbout = name.pabout
	#ProjectProfile.objects.get(
	
	#Get list of members id's
	pMembers = [] 
	for mem in up:
		if mem.projectprofile_id == prname:
			pMembers.append(mem.user_id)
			
			
	#Get list of user names
	ul = list(User.objects.all())  #*Changed*
	pMemName= []
	for user in ul:
		if user.id in pMembers: 
			pMemName.append(user.first_name)
			
	#Get list of tasks
	tl = list(AddTask.objects.all())
	pTasks = []
	for task in tl:
		if task.user == cur_user:
			pTasks.append(task)
			
		
	pName = {'pName':name,
			'pAbout': pAbout,
			'pMembers': pMemName,
			'pTasks': pTasks,
			'cur_user': cur_user}
	
	return render(request,'pName.html', pName)
	
def pTask(request, prname): #pTasks - Task page

	cur_user = request.user
	up = list(ProjectProfile.user.through.objects.all())
	
	#Get list of members id's
	pMembers = [] 
	for mem in up:
		if mem.projectprofile_id == prname:
			pMembers.append(mem.user_id)
			
			
	#Get list of user names
	ul = list(User.objects.all())  #*Changed*
	pMemName= []
	for user in ul:
		if user.id in pMembers: 
			pMemName.append(user)
			
	#Get list of tasks
	tl = list(AddTask.objects.all())
	pTasks = []
	for task in tl:
		if task.user in pMemName:
			pTasks.append(task)
			
	ptask = {'pName': prname,
			'pMember':pMemName,
			'pTask':pTasks,
			'cur_user': cur_user}
	
	return render(request, 'pTasks.html', ptask)
	
def addTask(request ,prname):
	if request.method == 'POST':
		form = addTaskForm(request.POST)
		
		if form.is_valid():
			cd = form.cleaned_data
			
			up = User.objects.all()
			for mem in up: #Submits task to db
				if mem.first_name == cd['user']:
					new_class = AddTask(user = mem,
									date = cd['date'],
									descr = cd['descr'])
					new_class.save()
			url = '/projects/'+prname+'/tasks'
			return HttpResponseRedirect(url)	
		else:
			raise Http404	#Throws 404 if the task entry fails
	
#Tasks/Deadlines Page - Upcoming Deadlines	
@login_required	
def pTasks(request, prname):
	return render(request, 'pTasks.html')	
	
'''	- Possible pages
def pCalendar(request):
	return render(request, 'pCalendar.html')	
	
def pProgress(request):
	return render(request, 'pProgress.html')
'''
	
	
	
	
###########ANDREW FUNCTIONS##################	
	
	
	
def register(request):
	form = UserProfileForm()
	return render(request,
				'register.html',
				{'form': form})

def add_member(request): #Adds a new user to the DB
	if request.method == 'POST':
		form = UserProfileForm(request.POST)
		
		if form.is_valid():
			cd = form.cleaned_data
			
			if User.objects.filter(username = cd['email']).exists():#Checks if the inputted email is already in use
				return HttpResponseRedirect('http://danu6.it.nuigalway.ie:8667') #(request, 'alert.html',{'message': message})
			else:
				new_user =  User.objects.create_user(username = cd['email'],
											email = cd['email'], 
											first_name = cd['first_name'],
											last_name = cd['last_name'],
											password = cd['password'])
				
				new_user.save()
				
				#Login the user after registering them
				log_user = auth.authenticate(username=cd['email'], 
										password=cd['password'])
				if log_user is not None: #checks if the username and password are in the database
					if log_user.is_active: #checks that the user account is marked active
						auth.login(request, log_user) #sets user to logged in
						return HttpResponseRedirect('/projects/')
					else:
						return render(request, 'login_fail.html')
				else:
					return render(request, 'login_fail.html')
		else:
			return render(request,
			'register.html',
			{'form':form})
			
		
def login(request):

	if request.user.is_authenticated():
		http = '<http><body><p>You are already logged in</p><body></http>'
		return HttpResponse(http)
	else:
		form = LoginForm()
		return render(request,
					'login.html',
					{'form' : form})
	
def login_req(request):
	username = password = ''
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		
		user = auth.authenticate(username=username, password=password)
		
		if user is not None: #checks if the username and password are in the database
			if user.is_active: #checks that the user account is marked active
				auth.login(request, user) #sets user to logged in
				return HttpResponseRedirect('/projects/')
			else:
				return render(request, 'login_fail.html')
		else:
			return render(request, 'login_fail.html')
	else:		
		return render(request, 'login_fail.html')
	
@login_required		
def logout_req(request):
	logout(request)
	return render(request,'home.html')
	
	
@login_required
def project (request):
	form = ProjectProfileForm()
	return render(request, 
				'project.html',
				{'form':form})
	
	
@login_required	
def add_project(request):
	if request.method == 'POST':
		form = ProjectProfileForm(request.POST)
		
		if form.is_valid():
			cd = form.cleaned_data
			
			project = ProjectProfile(pname = cd['pname'],
									 ppassword = cd['ppassword'], 
									 pabout = cd['pabout']) 
									
			if project.pname and project.ppassword and project.pabout:  #Checks that user has filled all fields
				project.save()
				project.user.add(request.user) #Records current user as the user that created the project
				return HttpResponseRedirect('/projects/')	
			else:
				return render(request, 
				'project.html',
				{'form':form})
		else:
			return render(request, 
				'project.html',
				{'form':form})
	else:	
		return HttpResponseRedirect('/projects/')	
		
def add_project_tab():
	return

	
@login_required	
def mem_project(request):
	form = AddMemberProject()
	return render(request, 
				'add_member_project.html',
				{'form':form})
				
def add_mem_project(request): #add a member to an existing project
	if request.method == 'POST':
		form = AddMemberProject(request.POST)
		
		if form.is_valid():
			cd = form.cleaned_data
			
			if ProjectProfile.objects.filter(pname = cd['pname']).exists():
				project = ProjectProfile.objects.get(pname = cd['pname'], ppassword = cd['ppassword'])
				project.user.add(request.user)
				HttpResponseRedirect('/projects/')
			else:
				return HttpResponseRedirect('/projects/') #If they fail the test they are sent back to home page
			 
		else:
			return render(request, 
				'add_member_project.html',
				{'form':form})
				
	return  HttpResponseRedirect('/projects/')
		
@login_required
def projects(request): #Projects page - Includes Your Projects, Create a Project and Join Project

	cur_user = request.user #get user object
	Name = cur_user.first_name #get users first name

	#Get project <----> user objects
	up = list(ProjectProfile.user.through.objects.all()) #up=userprofile
	
	pName = ['+', '+', '+', '+'] #List of project names's
	for id in up: #iterate through list of joint table objects
		if id.user_id == cur_user.id:
			pName.reverse()
			pName.append(id.projectprofile_id)#get id of projects the users is in
			pName.reverse()
	
	projects = {'Username': Name,
			'pName1':pName[0],
			'pName2':pName[1],
			'pName3':pName[2],
			'pName4':pName[3]}	
				
	return render(request,'projects.html',projects)

