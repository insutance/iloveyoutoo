from .forms import MyCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView

#--- TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'

#--- User Creation
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = MyCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


