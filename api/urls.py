from django.urls import path
from . import views

urlpatterns = [
    path('',views.overview,name='overview'),
    path('get-data/',views.get_data,name='get-data'),
]
