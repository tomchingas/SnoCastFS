from django.utils import timezone
from podcast_data.models import Avalanche_Accident
import json


with open('/home/tom/SnoCast/SnoCastFS/avalanche_accidents.json') as avalanche_accident_json:
    avalanche_accident_dict = json.load(avalanche_accident_json)


avalanche_number_list = []

for dictionary in avalanche_accident_dict:
    avalanche_number_list.append(dictionary['avalanche_number'])

for number in avalanche_number_list:
    avalanche_accident = Avalanche_Accident.objects.get(avalanche_number = number)
    avalanche_accident.audio_url = f'https://snocast-media.s3-us-west-2.amazonaws.com/accident_audio_{number}.wav'
    avalanche_accident.save()