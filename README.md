# django-api

### create & activate virtual environment (linux)

    virtualenv venv --python=python3
    source venv/bin/activate

### create & activate virtual environment (windows)

    python -m virtualenv venv
    venv/Scripts/activate

### Install requirements

    pip install -r requirements.txt

### Apply Migrations

    python manage.py makemigrations
    python manage.py migrate

### Create Super user

    python manage.py createsuperuser

### Start the server

    python manage.py runserver
