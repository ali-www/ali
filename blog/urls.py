from  django.urls import path
from  .views import   DeletePostView ,DeleteCommentView , PostCreate , like_or_unlike , about_me
from  . import views




urlpatterns = [
     path('',views.Home,name='home'),
     path('addpost/',PostCreate.as_view(),name='addpost' ),
     path('about_me/',about_me,name='about_me'),

   
    
     path('product/<int:pk>/like_or_dislike',like_or_unlike , name='like'),

     path('articale/<int:pk>/remove/',DeletePostView.as_view(),name='delete_post'), 
     path('deletecoomet/<int:pk>/remove/',DeleteCommentView.as_view(),name='delete_comment'), 

     path('like/',views.Like_post,name='like_post'),

     path('list/<int:pk>/detail/',views.Detail_iew,name='detail'),

     
]
