from django.contrib import admin

# Register your models here.
from .models import Blog_post

#class Blog_postAdmin(admin.ModelAdmin):
    #list_display = ('title','content','slug','user')

admin.site.register(Blog_post)#, Blog_postAdmin)
