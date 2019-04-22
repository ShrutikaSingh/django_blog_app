from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
#we will create one post model,this willbe a class that will inherits from django models class
#each class has going to be its own table in the database,and we will be creating attribute
#  and each attribute will be different field in the database
#inheriting post class from models.Model




class Post(models.Model):
    title = models.CharField(max_length=100)
#one field that will have for the field is title ,so this is going to be charfield with arguments to constraint it
#so now we have title that will be a field of post table in the database and that title field will be a character field that will have max length=100
    content= models.TextField() #wd no constraints since it will be lots of lines
    date_posted= models.DateTimeField(default=timezone.now) #argument can be 1)auto_now=True which means update the date to date posted to current date time everytime the post was updated
    #2)auto_now_add=True  which means update the date to date posted to current date time only when the object is created
    #3)default we have to import thr utility from django.utils import timezone ,

#now we need to have an author for each post ,this will be user who created the post
#now our user will be seperate table so first we need to import the user model   from django.contrib.auth.models import User
#so post and user are are going to be one to many reltionship and for this we can use a forign key
    #author = models.ForeignKey(User, on_delete=models.CASCADE) #on delete = models.CASCADE for if a user is deleted then we also wanted the post to be deleted but not vice versa
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    image1=models.ImageField(default="default.jpeg",upload_to='book_pics')#migrations is necessary here look below
#re run the migrations to update the database
#on terminal >python manage.py makemigrations
#>python manage.py migrate



'''

this is the method used in models.py of user to upload the image1
i tried the same method
image1=models.ImageField(default="default.jpeg",upload_to='profile_pics')



class Profile(models.Model): #inherting from models.Model
    user=models.OneToOneField(Post,on_delete=models.CASCADE)
    image=models.ImageField(default="default.jpeg",upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    #now to def __str__(self):
        return f'{self.user.username} Profile'
    #on teminal >python manage.py makemigrations
    #>python manage.py migrate

'''


def __str__(self): #to get the posts with descrpition in python shell Post.objects.all()
    return self.title #write the description that we want to see in post
def __str__(self):
    return f'{self.user.username} Profile'
