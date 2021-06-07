to run the server type:

python manage.py runserver



api server:

localhost:8000/api/accidents



to download audio file locally from django server:
-save audio files in the media folder in the main project directory

localhost:8000/media/"filename"



to download audio file from AWS S3:
- use the URL in the database for the avalanche accident from the 'audio_url' field
     - exampe 'https://snocast-media.s3-us-west-2.amazonaws.com/accident_audio_2.wav'



SQLite database:
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
    audio_url
    pub_date

