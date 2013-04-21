from django.shortcuts import render
from django.http import HttpResponseRedirect

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')

	else:
		form = ContactForm()

	return render(request, 'index.html', {
		'form': form,
		})