from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list') # from mysite.ursl request will be redirected here and then to the views.post_list
]
