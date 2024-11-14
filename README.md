# Practice Implementing a Flask Application Using MVC

This project aims to implement a Flask application using the MVC architecture.

## How to Install the Project

Make sure that Python 3 is installed on your system. Create a Python virtual environment using the following command:

```
python3 -m venv venv
```
Then, activate the virtual environment using the following command:

```
source venv/bin/activate
```
After activating the virtual environment, install the project and its requirements:

```
pip install -e .
```

```
pip install -r requirements-dev.txt
```

Set the environment variable:

```
export FLASK_APP=flasker
```
execute the following commands to create the database and add some values to it

```
flask init_db
```
```
flask add_members
```
run the project:

```
flask run
```
## The structure of the project (In the following tree, only important entities are listed)
```
├── flasker
│   ├── cli
│   ├── controllers
│   ├── models
│   ├── templates
│   ├── websoket_handlers
│   ├── __init__.py
│   ├── config.py
├── tests
├── .gitignore
├── setup.py
├── requirements-dev.txt

```
In the current directory, you can find the files required to install the project, such as `requirements-dev.txt`, `setup.py`, etc., as well as two directories: `tests` and `flasker`. The tests directory is a package designed to implement test-driven development. You can use the examples in this package to implement your own tests. The main Flask application is implemented inside the flasker package. The structure of the flasker package is as follows:
```
├── flasker
│   ├── cli
│   ├── controllers
│   ├── models
│   ├── templates
│   ├── websoket_handlers
│   ├── __init__.py
│   ├── config.py
```
Inside the `__init__.py` file, the Flask application is configured. In this file, you need to import and register your controllers (routes).
