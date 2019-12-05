from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    context = {
          "string": get_random_string(length=14)
      }
    return render(request,'word_counter_app/index.html')


def string(request):
    if 'counter' not in request.session:
         request.session['counter'] = 0
    else:
        request.session['counter'] += 1
    context = {
          "string": get_random_string(length=14)
      }
    return render(request,'word_counter_app/index.html', context)

def clear(request):
    request.session.clear()
    return redirect('/')









