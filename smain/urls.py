from . import views
from django.urls import path, include

app_name = 'smain'

urlpatterns = [
    path('',views.index, name = "shore"),
]
