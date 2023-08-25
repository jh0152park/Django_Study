# Django_Study

Django_Study

---

# How to create a new Project

0. Create a new Repository
1. Create a new VENV project with `peotry init` command
    - `Author`: `Your Name`
    - `License`: MIT
    - `Would you like to define your main dependencies interactively? (yes/no)`: No
    - `Would you like to define your development dependencies interactively? (yes/no)`: No
    - Other Things: `Yes` or `Just Enter`
2. Install Django with `poetry add django` command (poetry add `package name`)
3. Run `django-admin` command

    - `command not found: django-admin`: Occurrend due to not inside VENV yet, So just run `poetry shell` command as below then retry `django-admin` command

        ```
        parkjaehyeon@bagjaehyeons-MacBook-Pro Django_Study % poetry shell
        Spawning shell within /Users/parkjaehyeon/Library/Caches/pypoetry/virtualenvs/django-study-4K70AHY4-py3.10
        parkjaehyeon@bagjaehyeons-MacBook-Pro Django_Study % emulate bash -c '. /Users/parkjaehyeon/Library/Caches/pypoetry/virtualenvs/django-study-4K70AHY4-py3.10/bin/activate'

        (django-study-py3.10) parkjaehyeon@bagjaehyeons-MacBook-Pro Django_Study %
        ```

4. If you want to go to outside of our VENV, just run `exit` command, then might be located outside from VENV

    - `poetry shell`: go to inside of our VENV
    - If you want to check am I located inside VENV or not, just run `django-admin` command to check

5. Start to project with `django-admin startproject config .` command

---

# How to run server on our developer side

-   Run `python manage.py runserver` command
-   Then, created a new `db.sqlite3` file

---

# How to migrate to apply admin, auth, contenttypes, sesstions

-   Run `python manage.py migrate` command
    ```
    Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying admin.0003_logentry_add_action_flag_choices... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying auth.0009_alter_user_last_name_max_length... OK
    Applying auth.0010_alter_group_name_max_length... OK
    Applying auth.0011_update_proxy_permissions... OK
    Applying auth.0012_alter_user_first_name_max_length... OK
    Applying sessions.0001_initial... OK
    (django-study-py3.10) parkjaehyeon@bagjaehyeons-MacBook-Pro Django_Study %
    ```

---

# How to create a SuperUser

-   Run `python manage.py createsuperuser` command
    -   Django has free validation support!!🔥
    ```
    (django-study-py3.10) parkjaehyeon@bagjaehyeons-MacBook-Pro Django_Study % python manage.py createsuperuser
    Username (leave blank to use 'parkjaehyeon'):
    Email address:
    Password:
    Password (again):
    Superuser created successfully.
    ```
-   Then, we get a new admin panel as below
    ![image](https://github.com/jh0152park/Django_Study/assets/118165975/8656813b-0e8a-4871-8d11-83ccb76bf6fb)

---

# How to change language and time zone

-   Fixed some variables the `settings.py` inside of config folder as below
    ```python
    LANGUAGE_CODE = 'ko-kr'
    TIME_ZONE = 'Asia/Seoul'
    ```

---

# How to create a new Application

-   Run `python manage.py startapp [project name]` this command
    -   Then, literally cratead new project folder
-   Wirtedown something what we need to `models.py` of created project folder

    ```python
    from django.db import models

    # Create your models here.
    class House(models.Model):
        name = models.CharField(max_length=128)
        price = models.PositiveIntegerField()
        description = models.TextField()
        adress = models.CharField(max_length=128)
    ```

-   After that, move to `settings.py` of config folder
-   Add our own new application to `INSTALLED_APPS` as below
    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        "house.apps/HouseConfig"
    ]
    ```
-   Go to `admin.py` or created folder, then import and register our new model

    ```python
    from .models import House

    @admin.register(House)
    class HouseAdmin(admin.ModelAdmin):
        pass
    ```

-   Run `python manage.py makemigrations` command to migrate
    ```
    Migrations for 'house':
    house/migrations/0001_initial.py
        - Create model House
    ```
-   Run `python manage.py migrate` to apply our new application to migrate
    ```
    Operations to perform:
    Apply all migrations: admin, auth, contenttypes, house, sessions
    Running migrations:
    Applying house.0001_initial... OK
    ```

# We have to do `migration` and `migrate` when we fixed or added something

1. Run `python manage.py makemigrations` command
2. Run `python manage.py migrate` command

---

# 🔥🔥🔥Most important thing is create custom `User` application at the beginning🔥🔥🔥

1. Create a new `User` application with `python manage.py startapp [name of user]`
2. Create a new User class at `models.py` of created new folder as belw

    ```python
    from django.db import models
    from django.contrib.auth.models import AbstractUser

    # Create your models here.


    class User(AbstractUser):
        pass

    ```

3. Add AUTH config into `settings.py` of config folder as below
    ```python
    # AUTH
    AUTH_USER_MODEL = "users.User" #my app.my class
    ```
4. Install our new user application at `settings.py` of config folder as below

    ```python
    # Application definition

    CUSTOM_APPS = [
        "house.apps.HouseConfig",
        "users.apps.Userconfig"
    ]
    ```

5. Delete `db.sqlite3` to restart our project and turn off the server
6. Delete every migration files inside of `migrations` folder, also do not touch the `__init__.py`
7. Run `python manage.py makemigrations` command to restart server
8. Run `python manage.py migrate` command
9. Register new application to `admin.py` as below

    ```python
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin
    from .models import User

    # Register your models here.
    @admin.register(User)
    class CustomUserAdmin(UserAdmin):
        pass
    ```

10. Create a new `superuser` again with `python manage.py createsuperuser` command

---

# How to run black

-   Run `poetry run black .` command
