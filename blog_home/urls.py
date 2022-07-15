from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_auth, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('logout/', views.logout_auth, name='logout_auth'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('blogDetail/<slug>', views.blogDetail, name='blogDetail'),
    path('editBlog', views.editBlog, name='editBlog'),
    path('blogDelete/<id>', views.blogDelete, name='blogDelete'),
    path('blogUpdate/<slug>', views.blogUpdate, name='blogUpdate'),
]