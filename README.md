# Django_Study

Django_Study

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

# How to run server on our developer side

-   Run `python manage.py runserver` command
-   Then, created a new `db.sqlite3` file
