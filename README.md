Cart Application
================


Implementation
--------------

The application is implemented using Python 3, Django 1.7 and jQuery 2.

Data Storage
------------

For data storage it uses MySQL.

MySQLdb driver is not supported for Python 3 yet.

Solution is to use PyMySQL driver, but Django only officially supports MySQLdb.

To allow Django use PyMySQL, make a simple patch to your manage.py file:

    + try:    
    +     import pymysql    
    +     pymysql.install_as_MySQLdb()    
    + except ImportError:    
    +     pass         


Django admin setup
------------------

To define the superuser, run:

>python manage.py syncdb 