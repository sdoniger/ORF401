from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Person
from .forms import RideForm, NewRideForm


def index(request):
    context = {}
    form = RideForm(request.GET or None)

    if request.method == 'GET' and form.is_valid():
        origination_city = form.cleaned_data.get('origination_city')
        origination_state = form.cleaned_data.get('origination_state')
        destination_city = form.cleaned_data.get('destination_city')
        destination_state = form.cleaned_data.get('destination_state')

        query = Person.objects.all()

        if origination_city or origination_state:
            origination_filters = Q()
            if origination_city:
                origination_filters |= Q(origination_city__iexact=origination_city)
            if origination_state:
                origination_filters |= Q(origination_state__iexact=origination_state)
            query = query.filter(origination_filters)

        if destination_city or destination_state:
            destination_filters = Q()
            if destination_city:
                destination_filters |= Q(destination_city__iexact=destination_city)
            if destination_state:
                destination_filters |= Q(destination_state__iexact=destination_state)
            query = query.filter(destination_filters)

        if destination_city and destination_state:
            destination_filters = Q(destination_city__iexact=destination_city) & Q(
                destination_state__iexact=destination_state)
            query = query.filter(destination_filters)

        if origination_city and origination_state:
            origination_filters = Q(origination_city__iexact=origination_city) & Q(
                origination_state__iexact=origination_state)
            query = query.filter(origination_filters)

        context['people'] = query
    else:
        context['people'] = Person.objects.none()
        if not form.is_valid():
            print("Form is not valid.")
            print(form.errors)

    context['form'] = form
    return render(request, 'index_view.html', context)


def about(request):
    return render(request, 'about.html')


def create(request):
    if request.method == "POST":
        new_ride = NewRideForm(request.POST)
        new_ride.save()
    return redirect("/rides")


def form(request):
    context = {}
    context["new_ride_form"] = NewRideForm()
    return render(request,"form.html", context)
