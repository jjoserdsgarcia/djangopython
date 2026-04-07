"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from core.views import criarchamado, home

from core.views import chamados
from core.views import novo, sobre, bemvindo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('novo/<str:lab>/<str:problema>/<str:prioridade>/', novo, name='novo'),
    path('bemvindo/', bemvindo, name='BemVindo'), 
    path('sobre/', sobre, name='sobre'),
    path('criarchamado/', criarchamado, name='criarchamado'),
]