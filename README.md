# python-django-weather-app

## Stpes
- pip install -r requirements.txt

- django-admin startproject weather

### To run server
- cd weather

- python manage.py runserver

### To migrate db
- python manage.py migrate

- python manage.py createsuperuser


### Create App lookup
- python manage.py startapp lookup
- Each app needs to have it urls file. Create quotes/urls.py

### Run Migrations
- Create Migrations
python manage.py makemigrations
- Push Migration to DB
python manage.py migrate


### References
- [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
- [AirAPI](https://docs.airnowapi.org/)
