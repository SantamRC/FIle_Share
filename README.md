# Fileshare

## Configuration

0. Install system requirements:
    - `python3.6` or higher;
    - `postgresql` database engine, create user for app and database;
    - `virtualenv` for installed `python3.6`.

1. Create virtualenv:
```bash
virtualenv -p python3.6 env
. env/bin/activate
```
2. Install requirements:
```bash
pip install -r requirements.txt
```
3. Create `files/settings.py` and edit it to your needs (before
that install postgresql database and user for it):
```bash
cp files/settings_example.py files/settings.py
nano files/settings.py
```
4. Run migrations:
```bash
python manage.py migrate
```
You have to have no errors.
5. Run server to check if everything works:
```bash
python manage.py runserver
```
6. Press Ctrl+C to terminate the server and create super user for your
instance:
```bash
python manage.py createsuperuser
```
And answer all the questions.

7. Go to `localhost:8000/admin` in your browser to log into django admin
system.

You're finished configuring.