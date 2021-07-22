# Pet Shop
## this documentation for ubuntu os
### - Run those commands after cloning app:
``` sh
- First enter app
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- pre-commit install
- ./manage.py migrate
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
