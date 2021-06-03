to run the server type:

python manage.py runserver



api server:

localhost:8000/api/accidents



to download audio file locally from django server:
-save audio files in the media folder in the main project directory

localhost:8000/media/"filename"



changed fields and added field names to database:
- the field names match the names on the US Avalance accident report website
- list of fields:

    avalanche_number
    url
    location
    state
    date
    summary_description
    primary_activity
    primary_travel_mode
    location_setting
    killed
    type
    latitude
    longitude
    html
    pub_date

