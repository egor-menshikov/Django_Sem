from django.urls import path
from .views import CoinTemplate, DiceTemplate, HundredTemplate

urlpatterns = [
    path('coin/<int:count>/', CoinTemplate.as_view(), name='coin'),
    path('dice/<int:count>/', DiceTemplate.as_view(), name='dice'),
    path('hundred/<int:count>/', HundredTemplate.as_view(), name='hundred'),
    # path('stats/', views.stats, name='stats'),
]