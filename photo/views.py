from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Album, Photo
from freeboard.models import Freeboard



class AlbumLV(ListView):
    model = Album
    context_object_name = 'album'

class AlbumDV(DetailView):
    model = Album

    def get_context_data(self, **kwargs):
        # 기본 구현을 호출해 context를 가져온다.
        context = super(AlbumDV, self).get_context_data(**kwargs)
        # 모든 책을 쿼리한 집합을 context 객체에 추가한다.
        context['album'] = Album.objects.all()
        return context

class AlbumDV2(DetailView):
    model = Album
    template_name = 'photo/album_detail2.html'

    def get_context_data(self, **kwargs):
        # 기본 구현을 호출해 context를 가져온다.
        context = super(AlbumDV2, self).get_context_data(**kwargs)
        # 모든 책을 쿼리한 집합을 context 객체에 추가한다.
        context['album'] = Album.objects.all()
        return context


class PhotoDV(DetailView):
    model = Photo

    def get_context_data(self, **kwargs):
        context = super(PhotoDV, self).get_context_data(**kwargs)
        context['album'] = Album.objects.all()
        return context

#--- Add/Change/Update/Delete for Photo
class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['album', 'title', 'image', 'video_link', 'description']
    success_url = reverse_lazy('photo:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PhotoCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PhotoCreateView, self).get_context_data(**kwargs)
        context['album'] = Album.objects.all()
        return context


class PhotoChangeLV(LoginRequiredMixin, ListView):
    template_name = 'photo/photo_change_list.html'

    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(PhotoChangeLV, self).get_context_data(**kwargs)
        context['freeboard'] = Freeboard.objects.filter(owner=self.request.user)
        return context

class PhotoChangeLV2(LoginRequiredMixin, ListView):
    template_name = 'photo/photo_change_list_2.html'

    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)

class PhotoUpdateView(LoginRequiredMixin, UpdateView) :
    model = Photo
    fields = ['album', 'title', 'image', 'video_link', 'description']
    success_url = reverse_lazy('photo:index')

    def get_context_data(self, **kwargs):
        context = super(PhotoUpdateView, self).get_context_data(**kwargs)
        context['album'] = Album.objects.all()
        return context


class PhotoDeleteView(LoginRequiredMixin, DeleteView) :
    model = Photo
    success_url = reverse_lazy('photo:index')




