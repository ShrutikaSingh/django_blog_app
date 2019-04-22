#************to add any field in admin section just create a model here and register in admin.py*********


from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model): #inherting from models.Model
    user=models.OneToOneField(User,on_delete=models.CASCADE)#for one to one relation since one user can have one profile and one profile will be used by one user
    image=models.ImageField(default="default.jpeg",upload_to='profile_pics')#on delete is for what to do when the user is deleted cascade mwans delete the profile when user is deleted but not vice versa
    #it will create a directory called profile pics and upload all the pics in that directory
    def __str__(self):#this is dunderedd//a str method for more descriptive
        return f'{self.user.username} Profile' #it will print out the user name and then profile
#now to let these changes happen we have to make migrations
#on teminal >python manage.py makemigrations
##pip install pillow pillow is a library to work with images in python
#migrate to update the database with new migrations
#>python manage.py migrate
#we need to register this model within admin file of our app **********

#if multiple users are all saving different kinds of images then they clutter up our project directory with different image directory
#so lets change the setting so that we can change the location  of where the images are saved
#we also ned to change some additional settings so that or website can find these images when we try to view the images from browser
#in the seeting (djangoproject->another djangoproject->setting.py)we need to define something called media route and media url
