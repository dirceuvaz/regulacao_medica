from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/users/', include('core.urls')),  # Inclua as URLs da sua aplicação
    path('admin/', admin.site.urls),  # URLs do sistema de administração do Django
    path('', include('core.urls')),  # Inclua as URLs da sua aplicação principal
]