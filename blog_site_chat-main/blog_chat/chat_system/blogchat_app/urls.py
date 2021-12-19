from os import name
from django.urls import path
from .views import about_view, comment_reply, index_view, contact_view, my_blog_view,register_request,login_request,logout_request,edit_profile_view,post_detail_view

urlpatterns = [
    path('',index_view,name='index_page'),
    path('post-detail/<int:post_id>/',post_detail_view,name='detail_page'),
    path("register", register_request, name="register_page"),
    path("login", login_request, name="login_page"),
    path("logout", logout_request, name="logout_page"),
    path('about',about_view,name='about_page'),
    path('contact-us',contact_view,name='contact_page'),
    path('edit-profile',edit_profile_view, name='edit_profile_page'),
    path('my-blogs',my_blog_view,name='my_blog_page'),
    path('comment-reply',comment_reply,name='comment_reply_page'),
    
]


