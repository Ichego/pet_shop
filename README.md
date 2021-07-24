# Pet Shop

## this documentation for ubuntu os

### Run Using Docker:

``` sh
- install docker using https://docs.docker.com/engine/install/ubuntu/
- install docker compose using https://docs.docker.com/compose/install/
# after installation reopen terminal if opened
# run in terminal
- docker-compose up -d --build
- docker-compose up
```

### Run Using Venv:

#### inside project use those commands

``` sh
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- pre-commit install
- ./manage.py migrate
- ./manage.py collectstatic
- ./manage.py runserver
```

### - To Have Data On your website you can do 2 things :

``` sh
- ./manage.py loaddata app.json
```

### Or :

``` sh
- ./manage.py createsuperuser
- add user data
- enter  http://127.0.0.1:8000/admin/ or http://localhost:8000/admin/
- add category then pet
```
