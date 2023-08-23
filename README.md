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
