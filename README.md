Create a virtual environmentusing command
python3 -m venv pari-env

activate the environment
source ../../pari-env/bin/activate

clone the project in your local system

cd taskmanager/taskmanagement
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

Create admin user
python manage.py createsuperuser 

runserver 
python manage.py runserver

login into admin panel using 
http://127.0.0.1:8000/admin/

You may create custom user by adminpanel

For API documents

http://127.0.0.1:8000/swagger/
http://127.0.0.1:8000/redoc/

you may create projects, tasks and collaborator using dummy data by postman but auth required so you need to select basic auth

example API:

curl --location 'http://127.0.0.1:8000/project/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic cGFyaXRvc2gucHVyaUBnbWFpbC5jb206UGFAMTIzNDU2' \
--data '{"name": "paritosh",
"url": "http://www.pari.com",
"description": "my_dummy_project",
"created_by": 1
}'


curl --location 'http://127.0.0.1:8000/collaborator/' \
--header 'Content-Type: application/json' \
--data '{"description": "test 23",
"role": "developer",
"user": 1
}'


curl --location 'http://127.0.0.1:8000/task/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic cGFyaXRvc2gucHVyaUBnbWFpbC5jb206UGFAMTIzNDU2' \
--data '{"title": "pari",
"role": "developer",
"collaborator": [2, 3],
"description": "my_dummy_task",
"owner": 1,
"state":"To Do",
"priority": "Normal",
"created_by": 1
}'
