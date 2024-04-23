from django.urls import path
from .views import IndexView, AboutTemplate

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutTemplate.as_view(), name='about'),
]
