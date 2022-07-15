from dataclasses import fields
from django import forms
from froala_editor.widgets import FroalaEditor
from .models import *

class Add_Form(forms.ModelForm):
    class Meta:
        model = Blog_post
        #fields = ['content','title']
        fields = ('title','content','image')
        widgets = {
            'title': forms.TextInput(attrs = {"class": 'form-control'}),
            #'image': forms.FileInput(attrs = {"class": 'form-control'})
        }