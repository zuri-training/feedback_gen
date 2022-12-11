from django.urls import path
from .views import FormList

urlpatterns = [
    path('', FormList.as_view(), name='dashboard'),
]