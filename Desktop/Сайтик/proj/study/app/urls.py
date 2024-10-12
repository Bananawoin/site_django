from django.urls import path
from app.views import index, indexItem

app_name="app"


urlpatterns = [
    #http://127.0.0.1:8000/app/sosi
    path('', index),
    path("<int:my_id>/", indexItem, name='detail'),

   
    #http://127.0.0.1:8000/app/contacts
]