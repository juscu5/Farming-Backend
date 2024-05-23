Create A database
open ./PHFarming/settings.py
update the 'DATABASES' fields based on your system

cmd run:
cd ./PHFarming
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
