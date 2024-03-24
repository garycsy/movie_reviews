# django_projects

## Dependencies

pillow - image processing


## Commands

Each time you create an app

    python manage.py startapp

Each time you make changes to a model file, you have to run

    python manage.py makemigrations
    python manage.py migrate

## Documentation

Django documentation

[Django Template Language](https://docs.djangoproject.com/en/5.0/ref/templates/language/)

[Model field reference](https://docs.djangoproject.com/en/5.0/ref/models/fields/)

[Database Query Functions](https://docs.djangoproject.com/en/5.0/topics/db/queries/)


## Tailwind + Flowbite

Install NodeJS v20 (LTS) using NVM Package Manager

```
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
nvm install 20
```

Install Tailwind CSS + Flowbite 

```
npm install -D tailwindcss
npx tailwindcss init
npm install flowbite
# follow rest of the steps in https://flowbite.com/docs/getting-started/django/
```
