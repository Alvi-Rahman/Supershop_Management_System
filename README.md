# SuperShop Management User Manual

This is the user guide about how to use the project `locally`. 
This project is only for `practical` usage not for any professional
use.

## Dependencies

* It is recommended that you have python 3.9.x installed locally in 
  your machine for running this Project.
* Similarly, it is recommended that you have pip version > 20.0 installed for this project
  to run.
* Again installing `virtualenv` (python library) is preferred so that
you do not face any difficulties while activating the virtual environment.

## Installations

* After fulfilling the dependencies first clone the project from GitHub Repo
* Then go to the supershop_management directory from the root.
* Here you will find `supershop_app` and `supershop_management` sub-directories
  along with `db.sqlite3` `manage.py` and `requirements.txt` files.
* Create a Virtual Environment in this directory using `virtualenv <env-name>` command
  in the command line(Windows) and terminal(Mac/Linux) where `env-name` refers to your 
  preferred environment name.
* Create and activate your virtual environment using `source <env-name>/bin/activate` (Mac/Linux terminal) `<env-name>\Scripts\activate` (Windows cmd)
* Now use `pip install -r requirements.txt` command in terminal/cmd to install all packages/libraries and dependencies.


## Running The System

* Now run `python manage.py runserver` in cmd/terminal to start the server from root directory (where the manage.py is).
* Running the command will show `Starting development server at http://127.0.0.1:8000/`
* Copying the `http://127.0.0.1:8000/` url in the browser will start the website in real time.



