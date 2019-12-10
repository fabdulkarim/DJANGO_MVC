from django.urls import path
from . import views

app_name = 'profileata'
urlpatterns = [
    path('', views.index, name='home'),
    path('blog', views.blog ,name='blog'),
    path('mentee', views.mentee ,name='mentee'),
    path('mentor', views.mentor ,name='mentor'),
    path('author', views.author ,name='author'),
]