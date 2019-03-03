from django.shortcuts import render,redirect
from .models import List,Developer
from .forms import ListForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items  = List.objects.all
            messages.success(request,('Item Has Been Aded To List'))
            return render(request , 'form/index.html', { 'all_items' : all_items})
    else:
        all_items = List.objects.all
        return render(request, 'form/index.html', {'all_items' : all_items })


def delete(request,list_id):
    item = List.objects.get(pk = list_id)
    item.delete()
    messages.success(request,('Item Has Been Delete'))
    return redirect('index')

def cross_off(request,list_id):
    item = List.objects.get(pk = list_id)
    item.compelet = True
    item.save()
    return redirect('index')

def uncross(request,list_id):
    item = List.objects.get(pk = list_id)
    item.compelet = False
    item.save()
    return redirect('index')

def about(request):#,list_id
    all = Developer.objects.all
    context = {
    "data" : all
    }
    #item = Developer.objects.get(pk = list_id)
    return render(request, 'form/about.html', context)
