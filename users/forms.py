#displaaying email along with name in usercreation form
#what we are doing here is that till now we just have name of user in the usercreation  form now if we
#wanted to add gmail too then we have to inherit the usercreationform and make changes in it so that it
#can display email too
#within this file we are going to create our 1st form that inherits from the  user creation form
#this form to be used in users/templates/users/register.html
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#inherting UserRegisterForm from UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  #the default is required = true and we can change it to optional by EmailField(required=false)
#this class meta gives us a nested namespace for configuration and keeps the configuration in one place and within the configuration what we are saying that the models that is affected is user model for eg. when we do form.save its going to sab=ve it to user model and the fields that we want in form in what order
    class Meta:
        model = User    #in class meta we specify the model that we want the form to interact with the modelis going to be user because whenever the form vvaliade it create new user
        fields = ['username','email','password1','password2']#the field that we want to shown on our form in the order and then the matching password ie password1,password confirmation is password2

#so we we have completed form that inherits from the UserCreationForm and adds this email field and now we can just use this form in our views instead of just the usercreatonform
#so go back to the views (users/views.py) and at the top inherit this form there
#and then we can use the UserRegisterform with that email field indtead of usercreationform
#thereform in views.py we need to replace the usercreation form with UserRegisterForm to see the formun with emailfield

#creating the model form that will helps in updating the users profile
#model form is the form that allows us to create a from that helps us to create a specific database form

class  UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields=['username','email']#it means we want to work with username and email
                #for adding the profile picture here for updationwe need to create another form  we first have to import Profile model here from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['image']

#we created 2 forms but whenever we r going to put in the ttemplate it looks like one form
#so now we have to add these in views.py so that we can add these froms to profile views
