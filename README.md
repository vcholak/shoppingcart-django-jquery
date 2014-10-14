Simple Django application for Python 3.

For data storage it uses MySQL.

MySQLdb driver is not supported for Python 3 yet.

Solution is to use PyMySQL driver, but Django only officially supports MySQLdb.

To allow Django use PyMySQL, make a simple patch to your manage.py file:

#!/usr/bin/env python
+try:
+    import pymysql
+    pymysql.install_as_MySQLdb()
+except ImportError:
+    pass 