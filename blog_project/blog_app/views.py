from django.shortcuts import render
from django.http import HttpResponse
import datetime

from blog_app.models import Author


# Create your views here.
def index(request):
    return HttpResponse('test')


# def gen(request):
#     for i in range(1, 10):
#         author = Author(
#             name=f'name{i}',
#             surname=f'surname{i}',
#             email=f'email{i}@gmail.com',
#             bio=f'This is bio number {i}',
#             birthday=datetime.date(1986, 3, 1 + i),
#         )
#         author.save()
#     return HttpResponse('generation complete')


def author_full_name(request):
    author = Author.objects.filter(pk=1).first()
    fn = author.name
    print(type(fn))
    return HttpResponse(fn)