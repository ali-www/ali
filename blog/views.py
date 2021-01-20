from datetime import datetime
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from .models import  Comments, Post ,Like,Video ,Subscribe,AboutMe ,ContactMe
from .forms import  CommentForm ,AddPostform , ContactForm
from django.views.generic import  CreateView ,DeleteView
from django.views.generic.edit import CreateView
from django.urls.base import reverse, reverse_lazy

#=========================================================== start addpost=========
class PostCreate(CreateView):  
    model = Post
    form_class = AddPostform
    #fields = ['title', 'body','img'] 
    template_name = 'add_post.html'
  #  success_url = 'home' 

     
#============================================================= end addpost===

def Home(request):
    video   = Video.objects.all()
    qu      = Post.objects.all()
    user    = request.user
    if request.method == 'POST':
        email = request.POST['email']
        new_email = Subscribe()
        new_email.email = email
        new_email.save()
    context = {
        'qu':qu,
        'user':user ,'video':video 
    }
    return render(request,'home.html',context)

#========================================================= start like =====

def Like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id  = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        if user in post_obj.liked.all():
          post_obj.liked.remove(user)
        else:
          post_obj.liked.add(user)
        like,created = Like.objects.get_or_create(user=user,post_id=post_id)
        if not created:
         if like.value == 'Like':
            like.value = 'Unlike'             
         else:
            like.value = 'Like'
        like.save()       


    return redirect('home')
#========================================================= end like =====  
def Detail_iew(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj =form.save(commit=False)
            obj.post = post
            obj.save()
            return redirect('detail',pk=pk)
    else:
        form = CommentForm()        
    context = {
        'post':post,
        'form':form
    }
    return render(request,'detail.html',context) 

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html' 
    success_url = reverse_lazy('home') 
class DeleteCommentView(DeleteView):
    model = Comments
    template_name = 'delete_comment.html' 
    success_url = reverse_lazy('home')     


#================================================0
def card(request):

    context = {
   
    }
    return render(request,'card.html',context)
#==========================================================
def like_or_unlike(request,pk):
    post = Post.objects.get(pk=pk)

    if request.user in post.heart.all():
        post.heart.remove(request.user)
    
    else:
        post.heart.add(request.user)
    
    return redirect('detail',pk=pk)   

#==========================================
def about_me(request):
    about_me = AboutMe.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            obj =form.save(commit=False)
           # obj.post = post
            obj.save()
            return redirect('about_me')
    else:
        form = ContactForm()

    return render(request,'about_me.html',{'about_me':about_me,'form':form})
#=====================================================================
   