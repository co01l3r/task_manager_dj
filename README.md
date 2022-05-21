# README FILE

# Task Manager

**Version 1.0**

## Installation

You need a python and django installed on your machine, recommend virtual env as well.
 
for debian in terminal:
1. sudo apt update
2. sudo apt install python3-django
-----
to check if everything installed properly type:
1. python3 -V
for checking a python version
2. django-admin --version
    in both cases you should see the version prompted back to you.

## Usage

Run app:
1. in terminal navigate to project folder /task_manager
run django server by typing
2. python3 manage.py runserver
3. copy or ctrl/click on server address and open it in browser.
4. to run admin site just add /admin after server address in your browser.

Operate app:
4. Login with your credentials or create a new account by clicking on 'create new'
5. by clicking on + symbol you can add new tasks, title is required description and complete is option. By clicking on add, task will be created
6. by clicking 'show' button beside the task you will be redirected to detail page about the task
7. by clicking on 'edit' button, a prefilled form will be loaded for you to modify existing data in the dask
8. by clicking on 'delete' button, task will be deleted


