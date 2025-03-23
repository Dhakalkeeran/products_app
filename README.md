# Products App
### App to manage and search products using Django.

## How to setup the system
```
# create and activate virtual environment
python -m venv projectenv
source projectenv/bin/activate

# install requirements 
pip install -r requirements.txt
```

## create new superuser
```
python manage.py createsuperuser
```
Setup credentials for the superuser

## How to run server and populate data
```
python manage.py runserver
```
Go to localhost:port/admin, e.g. http://127.0.0.1:8000/admin <br>
Login with superuser credentials <br>
add categories, tags and products using the interface in admin dashboard

## How to search using the web interface
Go to localhost:port/search, e.g. http://127.0.0.1:8000/search <br>
Enter description, select category and tag, and click search button <br>
The results will be displayed
