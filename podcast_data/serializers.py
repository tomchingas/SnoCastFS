from rest_framework import serializers
from .models import Avalanche_Accident

class Avalanche_AccidentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'avalanche_number',
            'url',
            'location',
            'state',
            'date',
            'summary_description',
            'primary_activity',
            'primary_travel_mode',
            'location_setting',
            'killed',
            'type',
            'latitude',
            'longitude',
            'html',
            'audio_url',
        )
        model = Avalanche_Accident