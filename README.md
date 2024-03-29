# ehprimo-api
API for EhPrimo APP coded with Django and Djang REST Framework.

## Setting up venv
To be able to start the project, you must install it's dependencies. To do so, it is recomended to set a venv (Virtual Enviroment for Python).
To do it you must run the following commands:

### Linux
```
python -m venv .venv
```

### Windows
```
python -m venv venv
```

After that, you can use your venv running the command:

### Linux
```
source venv/bin/activate
```

### Windows
```
venv/Scripts/activate
```

## Installing dependencies
To install the dependecies of the project, run the following command with your venv activated:
```
pip install -r requirements.txt
```

## Running the server
To run the server, you must set up the database:
```
python manage.py makemigrations
python manage.py migrate
```

Then, you create a super user:
```
python manage.py createsuperuser
```

Finally, you can run the server:
```
python manage.py runserver
```

## Accessing admin pannel:
Access http://localhost:8000/admin/ with your browser and use the superuser you just created to log in.

<!-- ## Documentation
Accessing http://localhost:8000/docs/ will show the api's documentation. This documentation shows all endpoints, the params needed on each url and the body of the requisition needed to run some function. This documentation must be accessed using an authorized user, such as administratior user. -->