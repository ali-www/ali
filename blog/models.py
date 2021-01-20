from django.db import models
from django.contrib.auth.models import  User
from django.urls import reverse
# Create your models here.
class  Post(models.Model):
    title   = models.CharField(max_length=100)
    body    = models.TextField()
    liked   = models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    img     = models.ImageField(upload_to ='img/',blank=True,null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author  = models.ForeignKey(User,on_delete=models.CASCADE,related_name='author',null=True)
    heart   = models.ManyToManyField(User ,related_name='heart', blank=True)

    def __str__(self):
        return self.title
    @property
    def num_likes(self):
        return self.liked.all().count()
    def get_absolute_url(self):
            #return reverse('articale-detail',args=(str(self.id))) 
        return reverse('home')     

#=======================================================================================
LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)
class  Like(models.Model):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    post  = models.ForeignKey(Post,on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default='Like',blank=True,max_length=10) 
    def __str__(self):
        return str(self.post)          

#================================================================================================
class Comments(models.Model):
    post       = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name       = models.CharField(max_length=255)
    body       = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name) 
#=======================================================================
class Video(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
     
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
         
    def __str__(self):
        return self.title
#=============================================================================
class Subscribe(models.Model):
    email = models.EmailField()
    date  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email     

#=============================================================
class AboutMe(models.Model):
    
    first_name  = models.CharField(max_length=100) 
    last_name   = models.CharField(max_length=100) 
    photo       = models.ImageField(upload_to ='about/',blank=True,null=True) 
    phone       = models.CharField(max_length=100) 
    email       = models.EmailField()
    body        = models.TextField() 

    def __str__(self):
        return self.first_name
#=============================================================
class ContactMe(models.Model):
      
    name = models.CharField(max_length=100) 
    email = models.EmailField()
    date  = models.DateTimeField(auto_now_add=True)
    body = models.TextField() 

    def __str__(self):
        return self.name        

