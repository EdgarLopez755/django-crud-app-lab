from django.shortcuts import render, redirect


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin



from .models import Park, Ride

# from .forms import RideForm
# from django.http import HttpResponse






def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('park-index')
        else:
            error_message = 'Invalid sign up - try again'
    
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class Home(LoginView):
    template_name = 'home.html'


def about(request):
    return render(request, 'about.html')


@login_required
def park_index(request):
    parks = Park.objects.filter(user=request.user)
    return render(request, 'parks/index.html', {'parks': parks})

@login_required
def park_detail(request, park_id):
    park = Park.objects.get(id=park_id)
    # ride_form = RideForm()
    return render(request, 'parks/detail.html', {'park': park})

# @login_required
# def add_ride(request, park_id):
#     form = RideForm(request.POST)

#     if form.is_valid():

#         new_ride = form.save(commit=False)
#         new_ride.park_id = park_id
#         new_ride.save()
#     return redirect('park-detail', park_id=park_id)



class ParkCreate(LoginRequiredMixin, CreateView):
    model = Park
    fields = ['name', 'location', 'opening_date', 'description']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ParkUpdate(LoginRequiredMixin, UpdateView):
    model = Park
    fields = ['location', 'opening_date', 'description']


class ParkDelete(LoginRequiredMixin, DeleteView):
    model = Park
    success_url = '/parks/'


class RideCreate(CreateView):
    model = Ride
    fields = '__all__'


class RideList(ListView):
    model = Ride

class RideDetail(DetailView):
    model = Ride

class RideUpdate(LoginRequiredMixin, UpdateView):
    model = Ride
    fields = ['name', 'rating']
    # success_url = '/rides/'


class RideDelete(LoginRequiredMixin, DeleteView):
    model = Ride
    success_url = '/rides/'