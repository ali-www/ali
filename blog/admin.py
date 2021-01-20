from django.contrib import admin
from .models import  Post,Like,Comments,Video ,Subscribe , AboutMe,ContactMe

# Register your models here.
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comments)
admin.site.register(Video)
admin.site.register(Subscribe)
admin.site.register(AboutMe)
admin.site.register(ContactMe)
