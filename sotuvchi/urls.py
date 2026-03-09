from django.urls import path
from .views import mashinalarAPI


urlpatterns =[
    path('', mashinalarAPI.as_view())
]