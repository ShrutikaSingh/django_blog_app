#video number 8 timing from 30:00 minutes

#in this we are creating this page so that w=each time we dont have to update the user piocture through admin  but directly when user is created profile gets created
from django.db.models.signals import post_save
#get a post ssave signal when a user is created
from django.contrib.auth.models import User
from django.dispatch import receiver
#we also need to create a receiver to receive teh signal and perform the task
from .models import Profile

@receiver(post_save,sender=User)    #receiver is going to be decorator it takes the signal that we want post_save here
#when a user is saved then send this signal (post_save) and this signal is received by  receiver(create_profile function)
def create_profile(sender,instance,created,**kwargs): #the receiver is create_profile finction#instace is the instance of user
    if created:
        Profile.objects.create(user=instance)
#kwargs just accepts any additional keyword arguments into the end of function
#lets create save function that saves the profile everytime user is updated
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()

    #we have to import our signals inside the ready functions in our users->app.puy
