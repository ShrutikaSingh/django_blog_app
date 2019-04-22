#if we actually want to see the posts of the database in admin page too we actually have to register it so we if look in th eapp directory
#we will see admin.py file

from django.contrib import admin
# Register your models here so that they get visible on admin page


from .models import Post #so we have to first import the Post class from models.py ,since the models.py in the blog directory therfore .models (only one dot)
admin.site.register(Post) #now to register this model wd  our admin site and now if we reload the admin page the posts from database will get visible there also
#and now if we update anything from admin page it will get update on the website page
