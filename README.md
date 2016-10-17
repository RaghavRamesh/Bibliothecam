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
The backend of this app is built using Django, a framework of Python. 

Bootstrap framework is used to aid in the design of the management interface.

SQLite3 is used as the db. 


Directories and their uses:
---------------------------

- The models are defined in the models.py file which can be found in: 
Shelf\django\testproject\books\models.py

- The views and the functionality of the app is defined in views.py:
Shelf\django\testproject\books\views.py








