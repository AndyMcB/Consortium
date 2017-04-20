from django import forms
from django.contrib.auth.models import User
from models  import AddTask

class UserProfileForm(forms.ModelForm): #ModelForm allows us to create a form from a model
	class Meta: #The Meta class references the model we wish to create a form from
		model = User
		fields = ['first_name', 'last_name', 'email', 'password'] #Set which fields to use
	
class ProjectProfileForm(forms.Form):
	pname = forms.CharField(label="Project Name")
	ppassword = forms.CharField(label="Project Password")
	pabout = forms.CharField(label="Project Description")
	
class LoginForm(forms.Form):
	username = forms.CharField(label='Email')
	password = forms.CharField(label='Password')
	
class AddMemberProject(forms.Form):
	pname = forms.CharField(label="Project Name")
	ppassword = forms.CharField(label="Project Password") 
	
class addTaskForm(forms.Form):
	user = forms.CharField(label='user')
	date = forms.CharField(label='date')
	descr = forms.CharField(label='descr')
	
