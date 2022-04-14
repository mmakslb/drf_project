# Support App
## Installation Guide
Clone this project to  your local machine with installed Docker.
</br> Execute next commands to create and run Docker containers:
* docker-compose build
* docker-compose run web python manage.py migrate
* docker-compose run web python manage.py createsuperuser
* docker-compose up

## Sign Up and Log In User
To **Sign Up** new user you should send POST request to *http://127.0.0.1:8000/auth/users/*
</br>Requirement fields: username, email, password, re_password.

Before the **Log In** you should activate this user on Django Admin Panel.

To **Log In** user you should send POST request to *http://127.0.0.1:8000/auth/jwt/create/*
</br>Requirement fields: username, password.
</br>After that you will get access token, that you can use it to authorization.

## Add new Question and get List of actual questions
To create new question you should send POST request to *http://127.0.0.1:8000/questions/all/*
</br>Requirement fields: text, title.

If you want to get list of actual questions, you should send GET request to *http://127.0.0.1:8000/questions/all/* 
</br>(For **admin** user this link will show all types of questions. For **authenticated user** this link will show only actual questions)

## Add answer to question
To send an answer to a question you should send POST request to *http://127.0.0.1:8000/questions/all/pk/* 
</br>Requirement fields: text.


If you want to see details of question send GET request to *http://127.0.0.1:8000/questions/all/pk/*

## Get list of solved and frozen questions
If you want to see solved or frozen questions send GET request to:
- Solved questions: *http://127.0.0.1:8000/questions/solved/*
- Frozen questions: *http://127.0.0.1:8000/questions/frozen/*

## Change status of question(only for admin user)
If you want to change status of question send PATCH request to:
- *http://127.0.0.1:8000/questions/all/pk/*
- *http://127.0.0.1:8000/questions/solved/pk/*
- *http://127.0.0.1:8000/questions/frozen/pk/*
</br>Requirement field: status.
