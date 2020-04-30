from django.urls import path
from app.views import CarList

app_name = 'app'

urlpatterns = [
    path('index/', CarList.as_view(), name = 'index-car-list'),
]