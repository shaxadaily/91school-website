from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('single-blog/<int:pk>/', single_blog, name='single-blog'),
    path('save_comment/<int:pk>', save_comment, name='save_comment')
]