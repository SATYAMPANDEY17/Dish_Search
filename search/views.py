from django.shortcuts import render
from .models import Dish
from .forms import SearchForm
from django.db.models import Q
# Create your views here.
def search_view(request):
    form = SearchForm()
    results = []
    if request.method == 'GET' and 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Dish.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'search.html', {'form': form, 'results': results})
