from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('equipment.urls')),  # Теперь www не загружается по умолчанию
    path('www/', include('www.urls')),  # Добавьте явный путь для приложения www
]
