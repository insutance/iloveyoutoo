from django.urls import path

from . import views
from .views import *

app_name = 'produce'
urlpatterns = [

    path('', ProduceMain.as_view(), name='produce_main'),

    path('<int:pk>/', ProduceDetail.as_view(), name='produce_detail'),

    path('apply/', ProduceApply.as_view(), name="produce_apply"),

]

