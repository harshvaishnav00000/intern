from django.shortcuts import render
from .models import Batch

# Create your views here.


def index(request):
    return render(request, "index.html")


def join(request):
    id = request.GET.get('joinid')
    sid = request.GET.get('studentid')
    # print(id, sid)
    a = Batch()
    a.batchid = id
    a.studentid = sid
    a.save()

    all = Batch.objects.all()

    p = {'item':all}
    return render(request, "join.html", p)
