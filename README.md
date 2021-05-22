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


## End User

The End Users are the regular consumers who are eligible/responsible to buy any products.

As soon as you run the system you are redirected to the end user login site `(http://127.0.0.1:8000/login/)`

Here the Navbar has 3 links when you are not logged in. If as an end user you have no account you can sign up from
the `Signup` tab. But you are not allowed to access the home page unless you are logged in. 

    An admin can be a regular/end user while all the regular/end user might not be admins.

Sooner, you log into the system you are redirected to the home page. 
The home page has only one panel that is `Select Products` 
(I had plans to build other pages such as filter by categories and so on).

Clicking the `Select products` Panel will redirect you to the available products.

### Products

From this `Products` page you can Add/ Remove any quantity of products that are available(In Stock) and add them
to cart. After adding/Selecting the products you can click the `cart` link to view the products that have been added to 
the cart. You can't add a product more than it's quantity in the stock.

### Cart

The Cart Page shows the `details` of your shopping i.e. the quantity of different products purchased, Unit and total 
pricing od each individual item. Total summed price of all the products that have been bought without VAT and SD. Finally,
total payable price. if the cart is `empty`, you can not place order as the button is `disabled` in that case. You can also `change` 
the quantity if different items from the shopping cart along with `removing` different items. After successfully choosing items
you can click `Place Order` button to place the order.

## Order Success

After successfully placing the order you will be shown a success message and a link to the actual invoice as per the requirements. The link 
`View Invoice` will show you the `formatted` invoice using `QR Code` and a `table` of the order summary






