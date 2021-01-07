from django.shortcuts import render
from .generateGraph import create_graph
# Create your views here.

image_bytes = create_graph()
def index(request):
    context_dict = { 'data' : image_bytes}
    return render(request, 'main_app/index.html', context_dict )