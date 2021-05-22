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


## Users

There are mainly two kind of users

* ### Admin
* ### End User


## Admin

The admin can be created using the command `python manage.py createsuperuser` and then providing the necessary credentials.

In this simple site the role of the admin is to add different `categories` and the `products` for End Users.

* At first, Admin can log in to the admin panel from `(http://127.0.0.1:8000/supershop_admin)` url.
* Then providing the username and password he can Login to the Custom Admin Panel for adding different products and categories.
* The admin `Home` is basically a blank page at this stage while we need to bring focus to the `Navbar`
* The Navbar Has 3 Links (`Home` `Category` `Product`) and a logout button.
* Undoubtedly, the logout button Logs the User out of the panel.
* Similarly, The `Home` link redirects the user to the Home page of Admin Panel.

The other Two links `Product` and `Category` has the most important feature in this case. 

-   ### Category

    The Category Page has two tabs that are `Add a Category` and `View Category`.

    - From `Add a Category` panel you can add each category of products under which different 
      products might be available.
    - Similarly, from `View Category` panel you can view all the categories that have been added
      so far by the admin.
        - From this page(`View Category`) an admin can `Edit` and/or `Delete` the relevant information of 
          each of the category.



-   ### Product

    On the other hand, Product Page has two tabs as well naming `Add a Product` and `View Products`.

    - From `Add a Product` you can add different products same as the Category panel but with some 
      more information regarding each product. Nevertheless, each of the products must belong to a 
      category that have been added so far by the admin.
    - Similarly, from `View Products` panel and admin can view all the products that the admin have added.
        - From this page(`View Products`) an admin can `Edit` and/or `Delete` the relevant information of 
          each of the product.




