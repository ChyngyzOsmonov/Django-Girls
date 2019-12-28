from django.urls import path
from .views import *


urlpatterns = [
    path('', DoList.as_view(), name='list'),
    path('create/', CreateList.as_view(), name='create'),
    path('<int:pk>/delete/', DeleteList.as_view(), name='delete'),
    path('<int:pk>/update/', UpdateList.as_view(), name='update'),
]
