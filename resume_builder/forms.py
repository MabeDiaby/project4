from django import forms
from .models import Socials, Post, Tag, Project
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = (
            'name',
        )
        widget = {
            'name' : forms.TimeInput(attrs={'class' : 'form-control'}),
        }

class SocialsForm(forms.ModelForm):
    class Meta:
        model = Socials
        fields = (
            'name',
            'image_url',
            'link',
        )
        widget = {
            'name' : forms.TimeInput(attrs={'class' : 'form-control'}),
            'image_url' : forms.TimeInput(attrs={'class' : 'form-control'}),
            'link' : forms.TimeInput(attrs={'class' : 'form-control'}),
        }

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = (
#             'first_name',
#             'last_name',
#             'email',
#             'bio',
#             'socials',
#             'profile_pic'
#         )

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
        "headline",
        "sub_headline",
        "body",
        "intro",
        "language",
        "image_url",
        "resume",
        'match',
        )
        widget = {
            'headline' : forms.TimeInput(attrs={'class' : 'form-control'}),
            'image_url' : forms.TimeInput(attrs={'class' : 'form-control'}),
            'resume' : forms.TimeInput(attrs={'class' : 'form-control'}),
            'match' : forms.TimeInput(attrs={'class' : 'form-control'}),
            'sub_headline' : forms.TimeInput(attrs={'class' : 'form-control'}),
            'body' : forms.TimeInput(attrs={'class' : 'form-control'}),
            'intro' : forms.TimeInput(attrs={'class' : 'form-control'}),
            'language' : forms.TimeInput(attrs={'class' : 'form-control'}),
        }
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
        "name",
        "stack",
        "description",
        "image_url",
        "livelink",
        "gitlink",
        "post",
        )
        widget = {
            'name' : forms.TimeInput(attrs={'class' : 'form-control'}),
            'image_url' : forms.TimeInput(attrs={'class' : 'form-control'}),
            'livelink' : forms.TimeInput(attrs={'class' : 'form-control'}),
            'gitlink' : forms.TimeInput(attrs={'class' : 'form-control'}),
            'post' : forms.TimeInput(attrs={'class' : 'form-control'}),
            'stack' : forms.TimeInput(attrs={'class' : 'form-control'}),
            'description' : forms.TimeInput(attrs={'class' : 'form-control'}),
        }
