from django.shortcuts import render
from datetime import datetime
from sakila.models import Country
from sakila.models import City
from django.shortcuts import render, get_object_or_404


def status(request):
    h = datetime.now().strftime("%Y-%m- %d - %H:%M:%S")
    cname = "Kévin Salmon, Bradley Mutima"
    return render(request, 'banniere.html', {'hours': h, 'cname': cname})

def country_list(request):
    countries = Country.objects.all()
    return render(request, 'country_list.html', {'countries': countries})


def city_list(request):
    show_capitals = request.GET.get('capital', '0')  # '0' = toutes, '1' = capitales uniquement
    if show_capitals == '1':
        cities = City.objects.select_related('country').filter(capital=1)
    else:
        cities = City.objects.select_related('country').all()
    return render(request, 'city_list.html', {'cities': cities, 'show_capitals': show_capitals})


def cities_by_country(request, country_id):
    cities = City.objects.filter(country_id=country_id)
    country = Country.objects.get(pk=country_id)
    return render(request, 'cities_by_country.html', {'cities': cities, 'country': country})

