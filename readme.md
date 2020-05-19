# Welcome to my blog project

## Project description
+ multiple users
+ more complex than just function views
+ single app this time

## Project history
+ pull repo
+ run `gitk --all`
+ project history = git logs/commits/branches/ et c.

## How to run this stuff


## Required packages
+ everything is listed in requirements.txt

+ how to ... 
++ activate virtual environment
++`pip install -r requirements.txt`

# additional info
+ it's a good idea to start with setting up models.py first, because they're going to dictate the whole projects run setups
+ once models are set up, it's time to set up forms
+ this includes widgets to handle css classes
+ third step - create views, templates and connecting it all in urlpatterns
+ view -> template -> url
+ templates are the next to go, once models, views and urls are set up
+ medium style editor added via pip, registered in INSTALLED_APPS

# Work Log
- [x] git init
- [x] set up virtualenv, project and app folders
- [x] settings.py
- [x] folder structure
- [x] blog app models, widgets
- [x] CRUD class-bsed views
- [x] function views
- [X] authentication system, on top of superuser
- [x] medium style editor
- [ ] next best feature?!