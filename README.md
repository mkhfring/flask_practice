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

