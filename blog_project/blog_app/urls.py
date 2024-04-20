from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('fullname/', views.author_full_name, name='fullname'),
]
# path('generate/', views.gen, name='generate'),