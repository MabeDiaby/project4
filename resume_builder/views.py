from django.shortcuts import render, redirect
from .models import Socials, Post, Tag, Project
from .forms import SocialsForm, PostForm, TagForm, ProjectForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    return render(request, 'resume_builder/home.html')

# def homePage(req):
#     return render(req, 'resume_builder/home.html')

#---list---
def socials_list(req):
    socials = Socials.objects.all()
    return render(req, 'resume_builder/socials_list.html', {'socials': socials})

# def profile_list(req):
#     profile = Profile.objects.all()
#     return render(req, 'resume_builder/profile_list.html', {'profile': profile})

@login_required
def post_list(req):
    post = Post.objects.all()
    return render(req, 'resume_builder/post_list.html', {'post': post})

def project_list(req):
    projects = Project.objects.all()
    return render(req, 'resume_builder/project_list.html', {'projects': projects})

def tag_list(req):
    tag = Tag.objects.all()
    return render(req, 'resume_builder/tag_list.html', {'tag': tag})

#----Read----
def socials_info(req, pk):
    socials = Socials.objects.get(id=pk)
    return render(req, 'resume_builder/socials_info.html', {'socials': socials})

# def profile_info(req, pk):
#     profile = Profile.objects.get(id=pk)
#     return render(req, 'resume_builder/profile_info.html', {'profile': profile})

def post_info(req, pk):
    post = Post.objects.get(id=pk)
    return render(req, 'resume_builder/post_info.html', {'post': post})

def tag_info(req, pk):
    tag = Tag.objects.get(id=pk)
    return render(req, 'resume_builder/tag_info.html', {'tag': tag})

def project_info(req, pk):
    project = Project.objects.get(id=pk)
    return render(req, 'resume_builder/project_info.html', {'project': project})

#---Create---
def socials_create(req):
    if req.method == 'POST':
        form = SocialsForm(req.POST)
        if form.is_valid():
            socials = form.save()
            return redirect('/', pk=socials.pk)
    else:
        form = SocialsForm()
    return render(req, 'resume_builder/socials_form.html', {'form': form})

def project_create(req):
    if req.method == 'POST':
        form = ProjectForm(req.POST)
        if form.is_valid():
            project = form.save()
            return redirect('/', pk=project.pk)
    else:
        form = ProjectForm()
    return render(req, 'resume_builder/project_form.html', {'form': form})

# def socials(req):
#     form = SocialsForm()
#     context = {'form' : form}
#     return render(req, 'resume_builder/socials_form.html', context)

# def profile_create(req):
#     if req.method == 'POST':
#         form = ProfileForm(req.POST)
#         if form.is_valid():
#             profile = form.save()
#             return redirect('profile_info', pk=profile.pk)
#     else:
#         form = ProfileForm()
#     return render(req, 'resume_builder/profile_form.html', {'form': form})

def post_create(req):
    if req.method == 'POST':
        form = PostForm(req.POST)
        if form.is_valid():
            post = form.save()
            return redirect('/', pk=post.pk)
    else:
        form = PostForm()
    return render(req, 'resume_builder/post_form.html', {'form': form})

def tag_create(req):
    if req.method == 'POST':
        form = TagForm(req.POST)
        if form.is_valid():
            tag = form.save()
            return redirect('/post/new', pk=tag.pk)
    else:
        form = TagForm()
    return render(req, 'resume_builder/tag_form.html', {'form': form})

#---Edit---
def socials_edit(req, pk):
    socials = Socials.objects.get(pk=pk)
    if req.method == "POST":
        form = SocialsForm(req.POST, instance=socials)
        if form.is_valid():
            socials = form.save()
            return redirect('/', pk=socials.pk)
    else:
        form = SocialsForm(instance=socials)
    return render(req, 'resume_builder/socials_form.html', {'form': form})

def project_edit(req, pk):
    project = Project.objects.get(pk=pk)
    if req.method == "POST":
        form = ProjectForm(req.POST, instance=project)
        if form.is_valid():
            project = form.save()
            return redirect('/', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(req, 'resume_builder/project_form.html', {'form': form})

# def profile_edit(req, pk):
#     profile = Profile.objects.get(pk=pk)
#     if req.method == "POST":
#         form = ProfileForm(req.POST, instance=profile)
#         if form.is_valid():
#             profile = form.save()
#             return redirect('profile_info', pk=profile.pk)
#     else:
#         form = ProfileForm(instance=profile)
#     return render(req, 'resume_builder/profile_form.html', {'form': form})

def post_edit(req, pk):
    post = Post.objects.get(pk=pk)
    if req.method == "POST":
        form = PostForm(req.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('/', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(req, 'resume_builder/post_form.html', {'form': form})

def tag_edit(req, pk):
    tag = Tag.objects.get(pk=pk)
    if req.method == "POST":
        form = TagForm(req.POST, instance=tag)
        if form.is_valid():
            tag = form.save()
            return redirect('/post/new', pk=tag.pk)
    else:
        form = TagForm(instance=tag)
    return render(req, 'resume_builder/tag_form.html', {'form': form})

#---Delete---
def socials_delete(req, pk):
    Socials.objects.get(id=pk).delete()
    return redirect('/')

def project_delete(req, pk):
    Project.objects.get(id=pk).delete()
    return redirect('/')

# def profile_delete(req, pk):
#     Profile.objects.get(id=pk).delete()
#     return redirect('profile_list')

def post_delete(req, pk):
    Post.objects.get(id=pk).delete()
    return redirect('/')

def tag_delete(req, pk):
    Tag.objects.get(id=pk).delete()
    return redirect('/')
