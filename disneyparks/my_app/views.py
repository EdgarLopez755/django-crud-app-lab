from django.shortcuts import render


from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Park
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Disney Parks</h1>')


def about(request):
    return render(request, 'about.html')

def park_index(request):
    parks = Park.objects.all()
    return render(request, 'parks/index.html', {'parks': parks})


def park_detail(request, park_id):
    park = Park.objects.get(id=park_id)
    return render(request, 'parks/detail.html', {'park': park})



class ParkCreate(CreateView):
    model = Park
    fields = ['name', 'location', 'opening_date', 'description']
    seccess_url = '/parks/'


class ParkUpdate(UpdateView):
    model = Park
    fields = ['location', 'opening_date', 'description']


class ParkDelete(DeleteView):
    model = Park
    success_url = '/parks/'