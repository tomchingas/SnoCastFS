"""snocast_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from rest_framework import routers
from podcast_data import views

# audio files
from django.conf import settings
from django.conf.urls.static import static

# making call to /api/accidents will return list of all avalanche accidents
router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/accidents/', views.ListAvalanche_Accident.as_view(), name='accidents'),
    #re_path('.*', TemplateView.as_view(template_name='index.html')),
    path('', include('podcast_data.urls')),
]

if settings.DEBUG:
    urlpatterns  += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)

