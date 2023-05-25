from django.urls import path
from . import views

urlpatterns = [
    
    path ('',views.index,name='index'),
    path('create-destination-api',views.create_destination,name='create-destination-api'),
    path('create-destination',views.create_destination_template,name="create-destination")
]
