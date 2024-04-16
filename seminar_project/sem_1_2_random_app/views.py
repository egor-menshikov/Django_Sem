from django.shortcuts import render
import random
from django.http import HttpResponse


# Create your views here.
def coin(request):
    return HttpResponse(random.choice(['Heads', 'Tails']))


def dice(request):
    return HttpResponse(str(random.randint(1, 6)))


def hundred(request):
    return HttpResponse(str(random.randint(0, 100)))
