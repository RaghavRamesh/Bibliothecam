# Create your views here.

from django.http import HttpResponse
from books.models import Books
from django.template import Context, loader 

from django.shortcuts import render, render_to_response

from django.db.models import Q

def index(request):
	books_list = Books.objects.all()
	t = loader.get_template('books/index.html')
	c = Context({'books_list': books_list,})
	return HttpResponse(t.render(c))

def search_from_form(request):
	books_list = Books.objects.all()
	searchString = request.GET.get('search')
	error = "Nothing to display"
<<<<<<< HEAD
	search_list = Books.objects.filter(Q(title__contains = searchString) | Q(author__contains = searchString) | Q(pages__contains = searchString) | Q(genre__contains = searchString)) 
=======
	search_list = Books.objects.filter(Q(title__contains = searchString) | Q(author__contains = searchString) | Q(pages__contains = searchString)) 
>>>>>>> origin/master
	if len(searchString) > 0:
		
		c = Context({'books_list': books_list, 'search_list': search_list})
		t = loader.get_template('books/index.html')
		return HttpResponse(t.render(c))	
	else:
		c = Context({'books_list': books_list, 'error' : error})
		t = loader.get_template('books/index.html')
		return HttpResponse(t.render(c))


def add_from_form(request):
	message = "Enter data for all fields"
	title = request.GET.get('title')
	author = request.GET.get('author')
	pages = request.GET.get('pages')
	genre = request.GET.get('genre')
	newBook = Books(title=title, author=author, pages=pages, genre=genre)
	newBook.save()
	books_list = Books.objects.all()
	t = loader.get_template('books/index.html')
	c = Context({'books_list': books_list,})
	return HttpResponse(t.render(c))

def delete_from_form(request):
	id = request.GET.get('id')
	deleteBook = Books.objects.get(id=id)
	deleteBook.delete()
	books_list = Books.objects.all()
	t = loader.get_template('books/index.html')
	c = Context({'books_list': books_list,})
	return HttpResponse(t.render(c))

def update_from_form(request):
	id = request.GET.get('id')

	newTitle = request.GET.get('title')
	newAuthor = request.GET.get('author')
	newPages = request.GET.get('pages')
	newGenre = request.GET.get('genre')
	updateBook = Books.objects.get(id=id)
	if len(newTitle) == 0:
		newTitle = updateBook.title
	if len(newAuthor) == 0:
		newAuthor = updateBook.author
	if len(newPages) == 0:
		newPages = updateBook.pages
	if len(newGenre) == 0:
		newPages = updateBook.genre
	updateBook.title = newTitle
	updateBook.author = newAuthor
	updateBook.pages = newPages
	updateBook.genre = newGenre
	updateBook.save()
	books_list = Books.objects.all()
	t = loader.get_template('books/index.html')
	c = Context({'books_list': books_list,})
	return HttpResponse(t.render(c))