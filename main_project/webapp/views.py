from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from .filmModel import FilmModel


def index( request):

  films = FilmModel.GetAllFilms()

  #return JsonResponse( films, safe=False)

  return render(request, 'index.html', {
    'films': films,
  })

def add(request):

  film_add = FilmModel.AddOneFilm()

  return JsonResponse( film_add, safe=False)

def delete(request):

  film_add = FilmModel.DeleteOneFilm()

  return JsonResponse( film_add, safe=False)