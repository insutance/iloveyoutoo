from django.shortcuts import render , get_object_or_404, redirect
from .models import Showmethe
from django.utils import timezone

from .models import Showmethe


def content(request):
    items = Showmethe.objects
    return render(request,'idea_list.html', {'items':items})

def ideadetail(request, idea_id):
    id_detail = get_object_or_404(Showmethe, pk=idea_id)
    return render(request, 'idea_detail.html', {'item':id_detail})

def ideadelete(request, idea_id):
    item = Showthe.objects.get(id = idea_id)
    item.delete()
    return redirect('')


def ideaadd(request):
    return render(request,'idea_form.html')


def create(request):
    abc = Showmethe()
    abc.title = request.GET['title']
    abc.body = request.GET['body']
    abc.pub_date = timezone.datetime.now()
    abc.save()
    return redirect('/showme/')