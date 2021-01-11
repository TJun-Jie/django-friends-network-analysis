from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm
from .generateGraph import create_graph
from .tables import create_table

# Create your views here.

image_bytes = create_graph()

def index(request):
    context_dict = { 'data' : image_bytes}
    return render(request, 'index.html', context_dict )


def get_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InputForm()

    return render(request, 'forms.html', {'form': form})

def tables(request):
    context_tables = {'tables':create_table()}
    return render(request, 'tables.html',context = context_tables)