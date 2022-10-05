## About the coding exercise
This coding exercise is about ingesting weather data and yield data, design a database schema, and expose the data through a REST API. Django is used.

## Steps to run
- Clone the repo
  - `git clone https://github.com/ShreyasArthur/coding-exercise.git`
  - `cd coding-exercise`
- Create and activate the virtual environment
  - `python -m venv <venv_name>`
  - `./<venv_name>/Scripts/activate`
- Install required packages
  - `pip install -r requirements.txt`
- Make new migrations and create database
  - `cd src`
  - `python manage.py makemigrations` 
  - `python manage.py migrate`
- Create a superuser
  - `python manage.py createsuperuser`
  - Enter username, email, and password
- Injest weather data and yield data
  - `python manage.py injest_data -w` or `python manage.py injest_data --weather_data`
  - `python manage.py injest_data -y` or `python manage.py injest_data --yield_data`
- Analyse weather data
  - `python manage.py analyse_weather_data`
- Make sure you are in src folder to run the server
  - `cd src`
- Run the server
  - `python manage.py runserver`
- Paste the following url in your browser
  - `http://127.0.0.1:8000/admin/`
- Login with the superuser account created in previous steps
- Here you can click and view all the weather data, yield data, statistics data as well
- Endpoints 
  - `http://127.0.0.1:8000/api/weather` 
  - `http://127.0.0.1:8000/api/yield`
  - `http://127.0.0.1:8000/api/weather/stats`
- Filters can be applied using station_id and/or year
- Default pagination applied is 50
