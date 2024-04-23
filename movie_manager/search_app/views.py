from django.shortcuts import render
from movies.models import MovieInfo
from django.db.models import Q

def SearchResult(request):
    movies=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        movies = MovieInfo.objects.filter(Q(title__contains=query) | Q(actors__contains=query))
        return render(request,'search.html',{'query':query,'movies':movies})



