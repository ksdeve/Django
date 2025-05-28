from django.urls import path
from sakila.views import status, country_list, city_list, cities_by_country, city_detail

urlpatterns = [
    path('hello/', status, name='banniere'),
    path('countries/', country_list, name='country_list'),
    path('cities/', city_list, name='city_list'),

    path('countries/<int:country_id>/cities/', cities_by_country, name='cities_by_country'),
    path('city/<int:city_id>/', city_detail, name='city_detail'),



]
