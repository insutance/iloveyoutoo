from django.urls import path
from .views import *
import showme.views



show = showme.views


app_name = 'showme'
urlpatterns = [
    path('',show.content, name='idea_list'),
    path('idea_detail/<int:idea_id>/',show.ideadetail, name='idea_detail'),
    path('idea_detail/<int:idea_id>/delete',show.ideadelete, name='idea_delete'),
    path('add/',show.ideaadd, name='add'),
    path('create/', show.create, name='create'),
]
