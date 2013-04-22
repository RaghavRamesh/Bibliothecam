Shelf
=====

Bibliothecam - The Library
==========================

What is it?
-----------
This is a simple web-based application that implements CRUD with a separate management interface.
Bibliothecam is a library system that contains a database of books which can be manipulated.


What can you do with this app?
------------------------------
This app allows you to 
- Add a book to the database with all the essential attributes of the book.
- Search for a particular book identified by its ISBN.
- Update the details of a book in the database given its ISBN.
- Delete a book from the database.
In addition, the app also allows you to search for a book
- Based on a category, for e.g. Author.
- Given a word in the title of the book.
- Given any substring that is a part of the details of a book, say title, author etc.


Frameworks and libraries used:
------------------------------
The backend of this app is built using Django, a framework of Python. Hence, it implements MVC style. 
Django framework, is written in Python and eases the creation of complex database systems managed web applications. 
It is also used by famous websites including Firefox, Instagram. 

The front end is coded in HTML and Bootstrap framework is used to aid in the design of the management interface.
Bootstrap framework is an intuitive and a powerful tool for fast web development. 

SQLite3 is used for creating the schema for the database as it comes alongwith django and did not require the installation
of localhost servers like xampp for its working. 


Directories and their uses:
---------------------------

- The models/database schema of this app is defined in the models.py file which can be found in: 
Shelf\django\testproject\books\models.py

- The views or the UI and the functionality of the app is defined in views.py:
Shelf\django\testproject\books\views.py

- The source code of the website can be found in:
Shelf\django\templates\books\index.html








