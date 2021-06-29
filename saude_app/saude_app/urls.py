"""saude_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('profissionais_saude/', include('health_professionals.urls', namespace='health_professionals')),
    path('autenticacao/', include('auth_users.urls', namespace='auth_users')),
    path('anamnese/', include('anamnesis.urls', namespace='anamnesis')),
    path('patients/', include('patients.urls', namespace='patients')),
    path('medicines/', include('medicines.urls', namespace='medicines')),
    path('categorias/', include('categories.urls', namespace='categories')),
    path('sinais_vitais/', include('vital_signs.urls', namespace='vital_signs')),
    path('medicamentos_ministrados/', include('ministered_medicines.urls', namespace='ministered_medicines')),
    path('evolucao_paciente/', include('patient_evolution.urls', namespace='patient_evolution')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
