from django.contrib import admin
from django.urls import path


urlpatterns = [
path('admin/', admin.site.urls),
path('', wordcount.views.home, name="home"),
path('about/', wordcount.views.about, name="about"),
path('result/', wordcount.views.result, name = "result"),

]
