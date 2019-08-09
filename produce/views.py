from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Produce, ApplyForm
from django.urls import reverse_lazy
# Create your views here.
class ProduceMain(ListView):
    model = Produce
    context_object_name = 'post_list'

class ProduceDetail(DetailView):
    model = Produce
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        # 기본 구현을 호출해 context를 가져온다.
        context = super(ProduceDetail, self).get_context_data(**kwargs)
        # 모든 책을 쿼리한 집합을 context 객체에 추가한다.
        context['apply'] = ApplyForm.objects.all()
        return context

class ProduceApply(CreateView):           #html : fields를 썼기 떄문에 form(입력공간)을 갖고있는 html : (소문자모델)_form.html
    model = ApplyForm
    fields = ['produce','title', 'video_link']          #입력받고 싶은 것들
    success_url = reverse_lazy('produce:produce_main')  #성공적으로 만들어지면 redirection 시키는 방법 

    