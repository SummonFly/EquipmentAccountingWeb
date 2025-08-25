# equipment/urls.py
from django.urls import path
from .views import EquipmentListView

urlpatterns = [
    path('', EquipmentListView.as_view(), name='equipment-list'),
]
