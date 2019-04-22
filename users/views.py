from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm till 6th video we were using usercreation field that was just having name field no emailfield
from django.contrib import messages #for importing the flash message for ex. to show alert there are different types of message 1)message.debug 2)message.info 3)message.success 4)message.error 5)message.warning
from django.contrib.auth.decorators import login_required #we want user to access profile page only when they have logged in
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm #import the form that we created in forms.py to show the email along with name in usercreationform and now we can use the UserRegisterform with that email field indtead of usercreationform
##thereform in views.py we need to replace the usercreation form with UserRegisterForm to see the form with emailfield


# Create your views here.

def register(request):
    if request.method=='POST':    #since we dint specify where to post the data therefore we have to apply a condition that if we get post request
         #form = UserCreationForm(request.POST) intialyy till 6t part of video it was usercreationform taht was not having emailfield
         form = UserRegisterForm(request.POST)
         if form.is_valid(): #this is done by UserCreationForm
             form.save()    #user is created if the form is valid
             username = form.cleaned_data.get('username')#for grabinng the username if the form is valid #all validated data of form remains in .cleaned_data dictionary of from there we have to grab username
             #messages.success(request, f'Account successfully created for {username}!') #this was before video 7 ,,leran f string in python #this is for success message and we have to update the base template to see the flash message/to display that message in the register route when form got submittr
             #return redirect('blog-home')#after succesfully submiting the form return to home
             messages.success(request, f'Your account has been creatd ! you are now able to login.')
             return redirect('login')


    else:                          #if it says get request we just mak the form blank django form
        #form = UserCreationForm()  initially it was UserCreationForm
        form=UserRegisterForm()
    return render(request, 'users/register.html',{'form':form}) #requesting the template register.html and
    #pass in th eform as context so that we can access the form within the template
    #so pass the form as dictionary and the value taht we wanted is the new instance of form that we created above importing UsersCreationForm
   #since we dint specify where to post the data therefore we have to apply a condition that if we get post request
   #then we have to valiadate the data and if it says get request we just mak the form blank


@login_required #adding login_required decorater basically decorator adds functionality to exsiting functions but if we use class based view then the process of login_required is different check that out we havent used class based view here
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)#creating the instace for UserUpdateForm #request.user that is current logged in user #it means when we go to the user profile then the previous valuea of user should already be there
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)#it means when we go to the user profile then the previous value of profile should already there
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated !.')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)#creating the instace for UserUpdateForm #request.user that is current logged in user #it means when we go to the user profile then the previous valuea of user should already be there
        p_form=ProfileUpdateForm(instance=request.user.profile)


        context = {#context which is dictionnary and key is the variable that we going to acces within the template
            'u_form':u_form, #user update form
            'p_form':p_form  #profile update form
        }
        #now we have to pass the context into the templa
    return render(request, 'users/profile.html',context) #now create the profile.html template inside users template
