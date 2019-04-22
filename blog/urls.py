from django.conf.urls import url
from . import views
from .views import PostListView,PostDetailView

urlpatterns = [

    url('events/',views.endure,name='blog-endure'),
    url('events/',views.events,name='blog-events'),
    url('about/',views.about,name="blog-about"),
    url('post/<int:pk>/',views.PostDetailView.as_view(),name='blog-home'),
    url('', views.PostListView.as_view(), name='blog-home'),
    #url('', views.home, name='blog-home'), WE WILL not USE VIEWS.HOME now we will use PostListView
    #url ('register/',users/views.register,name='blog-register'), m just writing this for hit and trial
]
