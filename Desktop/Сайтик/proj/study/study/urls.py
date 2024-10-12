
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    #http://127.0.0.1:8000/app
    path("app/", include(("app.urls"), namespace= "app"))
]
