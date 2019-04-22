"""djnago_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views #for user login and logout
from django.conf.urls import url,include
from users import views as user_views #importing the views.py file from user for the register page since there can be many apps in views so therefore add _(underscore) for the getting the users
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('admin/doc/',include('django.contrib.admindocs.urls'),),
    url('admin/', admin.site.urls),
    url('register/',user_views.register,name='register'),
    url('profile/',user_views.profile,name='profile'),
    url('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),  #pass teh template location i.e users/login.html as an argument to as_view
    url('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'), #if you wanna see default logout page then remove the template_name but here it will look out atlogout.html template
    url('users/',include('users.urls'),),
    url('blog/',include('blog.urls'),), #for about page blog/about/
    url('',include('blog.urls'),), #for home page
]


'''
below code is taken from django docs for making the profile pic o get uploaded
https://docs.djangoproject.com/en/2.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development
Serving files uploaded by a user during development¶
During development, you can serve user-uploaded media files from MEDIA_ROOT using the django.views.static.serve() view.

This is not suitable for production use! For some common deployment strategies, see Deploying static files.

For example, if your MEDIA_URL is defined as /media/, you can do this by adding the following snippet to your urls.py:

This helper function works only in debug mode and only if the given prefix is local (e.g. /media/) and not a URL (e.g. http://media.example.com/).




if settings.DEBUG: #adding this only when we are in debug mode means during production not during deployment
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# ... the rest of your URLconf goes here ...
'''


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
