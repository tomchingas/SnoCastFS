from django.shortcuts import render
from rest_framework import generics
from .models import Avalanche_Accident
from .serializers import Avalanche_AccidentSerializer
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound
import os

class ListAvalanche_Accident(generics.ListCreateAPIView):
    queryset = Avalanche_Accident.objects.all()
    serializer_class = Avalanche_AccidentSerializer

class DetailAvalanche_Accident(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avalanche_Accident.objects.all()

# load static files (frontend react app)
class Assets(View):

    def get(self, _request, filename):
        path = os.path.join(os.path.dirname(__file__), 'static', filename)

        if os.path.isfile(path):
            with open(path, 'rb') as file:
                return HttpResponse(file.read(), content_type='application/javascript')
        else:
            return HttpResponseNotFound()

def index(request):
    avalanche_accidents = Avalanche_Accident.objects.all()
    return render(request, 'index.html', {'avalanche_accidents': avalanche_accidents})