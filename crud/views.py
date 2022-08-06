from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PegawaiudbForm
from .models import Pegawaiudb

# Create your views here.
def add(request):
    form = PegawaiudbForm(request.POST or None)
    # pegawaiudb = Pegawaiudb.objects.all()
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'add.html', {'form': form })

def show(request):
    pegawaiudb = Pegawaiudb.objects.all()
    return render(request, 'show.html', {'pegawaiudb' : pegawaiudb} )

def update(request, id):
    pegawaiudb = Pegawaiudb.objects.get(id=id)
    form = PegawaiudbForm(request.POST, instance=pegawaiudb )
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'update.html', {'pegawaiudb' : pegawaiudb} )

def delete(request, id):
    form = Pegawaiudb.objects.get(id=id)
    form.delete()
    return HttpResponseRedirect('/')