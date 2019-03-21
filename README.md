# Django Angular CRUD application

This application represents a communication between an application server, web server and database server.

The application server is written in Angular 7 and consists of one component which represents a list of movies and makes it possible to add, update, delete the list's elements.
The web server is written in Django 2.1 with Django Rest Framework, it has the special app called api that accepts requests from the application server, works with the database and returns responds back, respectively.
The database (in my case) is hosted on Heroku and all it needs to work with Django is a URL address that can be specified in Django's settings file.

![alt text](https://pp.userapi.com/c851024/v851024276/e7e32/wse7ev20xME.jpg)
