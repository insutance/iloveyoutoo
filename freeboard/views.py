from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Freeboard
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from photo.models import Album


class FreeboardLV(ListView):
    model = Freeboard

    def get_context_data(self, **kwargs):
        context = super(FreeboardLV, self).get_context_data(**kwargs)
        context['album'] = Album.objects.all()
        return context

class FreeboardDV(DetailView):
    model = Freeboard

    def get_context_data(self, **kwargs):
        context = super(FreeboardDV, self).get_context_data(**kwargs)
        context['album'] = Album.objects.all()
        return context

#--- Add/Change/Update/Delete for Freeboard
class FreeboardCreateView(LoginRequiredMixin, CreateView):
    model = Freeboard
    fields = ['title', 'body']
    success_url = reverse_lazy('freeboard:freeboard_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(FreeboardCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(FreeboardCreateView, self).get_context_data(**kwargs)
        context['album'] = Album.objects.all()
        return context    


class FreeboardChangeLV(LoginRequiredMixin, ListView):
    template_name = 'freeboard/freeboard_change_list.html'

    def get_queryset(self):
        return Freeboard.objects.filter(owner=self.request.user)


class FreeboardUpdateView(LoginRequiredMixin, UpdateView):
    model = Freeboard
    fields = ['title', 'body']
    success_url = reverse_lazy('freeboard:freeboard_list')

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.owner != request.user:
            messages.info(request, '수정할 권한이 없습니다!')
            return HttpResponseRedirect('/freeboard/')
        else:
            return super(FreeboardUpdateView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(FreeboardUpdateView, self).get_context_data(**kwargs)
        context['album'] = Album.objects.all()
        return context 


class FreeboardDeleteView(LoginRequiredMixin, DeleteView):
    model = Freeboard
    success_url = reverse_lazy('freeboard:freeboard_list')
    
    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.owner != request.user:
            messages.info(request, '삭제할 권한이 없습니다!')
            return HttpResponseRedirect('/freeboard/')
        else:
            return super(FreeboardDeleteView, self).dispatch(request, *args, **kwargs)




