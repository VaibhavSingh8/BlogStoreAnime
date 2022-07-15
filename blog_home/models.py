from django.db import models
# import auth user
from django.contrib.auth.models import User
# import froala editor
from froala_editor.fields import FroalaField
#import utility functions
from .utilities import *

#model class for blog app
class Blog_post(models.Model):
    title = models.CharField(max_length=300)
    content = FroalaField()
    slug = models.SlugField(max_length=200, null= True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True,  on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'blog_uploads/')
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add only executes once, when the instance is created 
    updated_at = models.DateTimeField(auto_now=True) #auto_now executes whenever the field is updated

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Blog_post, self).save(*args, **kwargs)