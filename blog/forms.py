from django import forms
from django.forms import  ModelForm
from .models import  Comments ,Post , ContactMe
from django.forms.widgets import  TextInput, Textarea

class  CommentForm(ModelForm):
    class  Meta:
        model  = Comments
        fields = ['name','body']
        widgets = {
            'title' :TextInput(attrs={'class':'form-control','placeholder':'your name here pleas :'}),
      
            'body': Textarea(attrs={'rows':4,'placeholder':'What is on your mind?'}),
          
        }   


#================================================================================================================

class AddPostform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body','img']

        widgets = {
            'title' :TextInput(attrs={'class':'form-control','placeholder':'here name your subject'}),
      
            'body': Textarea(attrs={'class':'form-control','placeholder':'what in your mind'}),
          
        }    

#==========================================================================================================
class  ContactForm(ModelForm):
    class  Meta:
        model  = ContactMe
        fields = ['name','email','body']
            