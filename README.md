# Marriage Moments - A website for hiring photographers

### Introduction
This is a **web based application** named **Marriage Moments**. This project is created in order to create a marketplace for both photographers and customers, where photographers are able to showcase their portfolio and customers can hire them by previewing their portfolio and package details.

### Insight
---
This project initally works upon ***4 pages*** 
1. ***Sign Up*** : The signup page takes necessary informations from a new user and sets up their account. Based on the user type of customer and photographer, we have two kinds of sign up page.
2. ***Log In*** :   This page page does whatever it expects it to do. This page logs in the user to their corresponding module. *The customers and photographers have different types of home page based on their account type*
3. ***Home*** : This the home page of the customer panel. It can perform **four** main tasks.
    * Get an overview of the existing photographers on the website
    * View the details of a particular photographer
    * Take a look at their portfolio and package details
    * Select a package and **Hire** the team
4. ***Photographer Dashboard*** : This page is used to show the necessary informations for a photographer. Features that this page include
    * Uploading photos in the portfolio
    * Update and delete photography package info
    * View and manage existing orders from different clients
    * Update Bio



### Creation
---
This project is created with **Django** in the backend along with **Bootstrap** at the frontend. For the database, **SQLite** is used as the default database of the **Django**. Hence the following are used to create this project :

1. **Django**
2. **Bootstrap**
3. **SQLite**


## **Installation**
---
In order to install the project in the local machine. At first the code needs to be cloned to the local machine.

This can be done using the following command.
``` bash
git clone https://github.com/muhammadnasif/Hotel-Management-System.git
```

After cloning from the remote-repo in the local machine. The next step is to install the requirements in the machine. It is generally **RECOMMENDED** to install the requirements in a *VIRTUAL ENVIRONMENT*. At first open a terminal inside the directory of the cloned repo.

Now we need to install the virtual environment if its not installed. 
``` bash
pip install virtualenv
```
After successfully installing the virtual enviroment. Now its time to create avirtual environment

``` bash
virtualenv venv
```

Now lets activate the virtual environment

**FOR WINDOWS USERS**
``` bash
source venv\Scritps\activate
```

**FOR OTHER USERS**
``` bash
source venv/bin/activate
```
Now install thre requirements from the requirements.txt file.
``` bash
pip install -r requirements.txt
```

Now you've successfully installed the requirements in your virtual environment. Finally run the file in the local machine using the following command

``` bash
python manage.py runserver
```