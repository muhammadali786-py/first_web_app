import operator
from django.http import HttpResponse
from django.shortcuts import render
from . import counter_app

def home(request):
    return render(request, 'home.html',)
def portfolio(request):
    return render(request, 'portfolio.html')
def result(request):
    article = request.GET['article']
    words_count,sorted_dict = counter_app.count(article)
    return render(request, 'result.html', {'article': article , 'words_count' : words_count, 'words_dict' : sorted_dict})


