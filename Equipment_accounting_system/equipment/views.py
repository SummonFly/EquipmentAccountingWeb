from django.views.generic import ListView
from .models import Equipment


class EquipmentListView(ListView):
    model = Equipment
    template_name = 'equipment/equipment_list.html'
