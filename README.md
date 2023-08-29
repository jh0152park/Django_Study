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

-   Run `poetry add black` first
-   Run `poetry run black .` command

---

# 🔥🔥🔥When you need some picutre🔥🔥🔥 

-   Shoutdown server first
-   Run `poetry add Pillow` command

---

# ORM 관계 정리
-   1:1 관계 = OneToOneField
-   1:Many 관계 = ForeignKey (Many쪽에서 설정함)
-   Many:Many 관계 = ManyToManyField

---

# ORM (Object Relational Mapping)
## By default, Django adds a `Manager` with the name `objects` to every Django model class.
### First run `python manage.py shell` command, if you want to test

## How to get data from our `Room` model?
```python
from rooms.models import Room

Room.objects.all()
=> then, show you entire rooms

Room.objects.get([propertys]="")
room = Room.objects.get(name="Django Room")
=> then, show you room data if you put correct data

also we can use like below too
room.[name of property]
room.name or
room.country or
room.owner or
room.amenity or
room.pk => pk mean is primary key

room.save() => can update imformation what you want like below
room.price = 9999
room.save()
```

## .all()
Literally bring me all data

```python
from rooms.models import Room

Room.objects.all()
=> then, show you entire rooms
```

## .get()
Should only return a one data of model, gonna return `error` when we request more than one results

```python
Room.objects.get(pk=1)
```

## .filter()
Lterally filter, also very similar with filter of JS, but we got a `error` when we search with does not exist property

```python
Room.objects.filter(pet_allow=True)
Room.objects.filter(price_per_night__gt=15) # results of price per night over that 15
Room.objects.filter(price_per_night__gte=15) # results of price per night over that 15 or equal with 15
Room.objects.filter(price_per_night__lte=15) # results of price per night less that 15 or equal with 15
Room.objects.filter(name__contain="서울") # Houses whose house names include 서울
Room.objects.filter(name__startswith="서울") # Houses whose names start with 서울
```

## .create()
Literally create some new data

```python
from rooms.models import Amenity

Amenity.objects.create(name="amenity from console", description="wow")
```

## .delete()
Literally delete some data

```python
from rooms.models import Amenity

Amenity.objects.get(pk=2).delete()
(1, {'rooms.Amenity': 1})
```

## QuerySet
QuerySet은 연산자를 함께 묶어주는 역할을 함, filter를 연속으로 2개, 3개 사용하고 싶다면?
그리고 QuerySet은 실제로 구체적인 데이터를 요청할때에만 데이터를 넘겨줌(그렇지 않으면 너무 많은 부하가 생김)

- `exclude`: 제외하고 싶을때 사용, 아래와 같은 경우 가격이 15보다 아래인것은 제외

```python
Room.objects.filter(pet_allow=True).exclude(price__lt=15).filter(name__contaions="제주")
Room.objects.filter(pet_allow=True, name__contains="제주", price__gt=15)
```

# Django REST Framework🔥

## How to install DRF!?
```
poetry shell
poetry add djangorestframework
```
Because we using `poetry` to separate our development environment from the other projects.


If you dont using `peotry`, then just try to install with `pip`

## After install done, what should id do?
1. go to `setting.py` of `config folder`
2. put `rest_framework` into `INSTALLED_APPS` list

## Homepage
https://www.django-rest-framework.org/
