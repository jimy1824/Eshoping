from django.urls import path
from .views import *
urlpatterns = [
    path('blog/', Blog.as_view(),
         name='blog'),
    path('single/blog/', SingleBlog.as_view(),
         name='single_blog'),
    path('regular/blog/', RegularBlog.as_view(),
         name='regular_blog'),
]