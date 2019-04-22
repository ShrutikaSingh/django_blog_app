from django.shortcuts import render
from django.http import HttpResponse
from .models import Post #. since the models is in th same directory import our Post class
from django.views.generic import ListView
from django.views.generic import DetailView
"""
#this below code was for earlier when we are using the dummy data as context,
# now we can query to our database using those same cmd line methods like 'posts':Post.objects.all()
posts = [ #it is list of dictionary that has 2 dummy posts
    {
        'author':'Shrutika',
        'title':'Blog Post1',
        'content':'1st Post',
        'date_posted':'25jan,19'
    },
    {
        'author':'Dijvijay',
        'title': 'Blog Post2',
        'content':'2nd Post',
        'date_posted':'26 jan,19'
    }
]
"""
#loading the template methods,1) load the template in and then render it and then pass that to http response
#shortcut -> from django.shortcut import render and now we can return render template instead of httpresponse

def home(request):
    context= {
        'posts':Post.objects.all() #like we use to do in cmd line
        #this below code was for earlier when we are using the dummy data as context,now we can query to our database using those same cmd line methods
        #'posts':posts, #the later white color posts is the dictonary we created above
        #we have context as a dictionary and the keys of the context is accessible from aour template the first orange color posts is key with a value of white color posts of dictionary
        #'title':'home'
    }
    return render(request,'blog/home.html',context) #2nd argument will be name of template eg home.html for home view
# **********blog/home.html is the name of template


#now m going to create a class since class based vieew
class PostListView(ListView):#this class inherting from ListView
    model=Post #the models tell ListView what model to query to
    template_name='blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name='posts' #context variable is used since we use the variable for posts as context in home view
    ordering = ['-date_posted']

#now m going to create a class based view following the default convention
class PostDetailView(ListView):#this class inherting from ListView
    model=Post #the models tell ListView what model to query to
    



"""
#instead of dummy data lets instead run a query on our post modle and pass in all of that data instead
#so first we need to import our post model
#from .models import Post
#now the posts from the database will be visible on the website
#but if we actually want to see the posts of the database on the admin page too we actually have to register it so we if look in the app directory
we will see admin.py file

"""



#def about(request):
 #   return HttpResponse('<h1>Blog about</h1>')
##this was starting wala direct httpresposne method without template

def about(request):
    return render(request,'blog/about.html',{'title':'About'}) #if the context is small like title here then we can directly pass the dictionary

#we will create a templates folder inside the blog directory that will have another blog folder
#blog -> templates -> blog ->templates.html
def events(request):
    return render(request,'blog/events.html',{'title':'Events'})


def endure(request):
    return render(request,'blog/endure.html',{'title':'Team Endure'})
