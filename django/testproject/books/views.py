# Create your views here.

from django.http import HttpResponse
from books.models import Books
from django.template import Context, loader 

from django.shortcuts import render, render_to_response

def index(request):
	books_list = Books.objects.all()
	t = loader.get_template('books/index.html')
	c = Context({'books_list': books_list,})
	return HttpResponse(t.render(c))

def search_form(request):
	return render(request, 'search_form.html')

def add_from_form(request):
	title = request.GET.get('title')
	author = request.GET.get('author')
	pages = request.GET.get('pages')
	newBook = Books(title=title, author=author, pages=pages)
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