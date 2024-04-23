from django.db.models import QuerySet
from django.shortcuts import render
import random
from django.http import HttpResponse
import logging

from django.views.generic import TemplateView
from sem_1_2_random_app.models import CoinToss

logger = logging.getLogger(__name__)


# Create your views here.


class CoinTemplate(TemplateView):
    template_name = 'sem_1_2_random_app/results.html'

    def get_context_data(self, count, **kwargs):
        context = super().get_context_data(**kwargs)
        res = [random.choice(['Heads', 'Tails']) for i in range(count)]
        context['game'] = 'CoinGame'
        context['results'] = res
        return context


class DiceTemplate(TemplateView):
    template_name = 'sem_1_2_random_app/results.html'

    def get_context_data(self, count, **kwargs):
        context = super().get_context_data(**kwargs)
        res = [str(random.randint(1, 6)) for i in range(count)]
        context['game'] = 'DiceGame'
        context['results'] = res
        return context


class HundredTemplate(TemplateView):
    template_name = 'sem_1_2_random_app/results.html'

    def get_context_data(self, count, **kwargs):
        context = super().get_context_data(**kwargs)
        res = [str(random.randint(0, 100)) for i in range(count)]
        context['game'] = 'HundredGame'
        context['results'] = res
        return context


def coin(request):
    try:
        result = random.choice(['Heads', 'Tails'])
    except Exception as e:
        logger.exception(f'Error in coin toss: {e}')
        return HttpResponse('Something went wrong.')
    else:
        logger.debug('Coin toss page accessed.')
        logger.info(f'Coin выброшено: {result}')
        try:
            toss = CoinToss(
                result=result
            )
            toss.save()
            logger.debug('Coin toss saved to database.')
        except Exception as e:
            logger.exception(f'Error saving to database {e}')
        return HttpResponse(result)


# def stats(request):
#     statistics = CoinToss.statistics()
#     response = '<br>'.join([f'{pk} {result}' for pk, result in sorted(statistics.items())])
#     return HttpResponse(response)
#
#
# def dice(request):
#     try:
#         result = str(random.randint(1, 6))
#     except Exception as e:
#         logger.exception(f'Error in dice throw: {e}')
#         return HttpResponse('Something went wrong.')
#     else:
#         logger.debug('Dice throw page accessed.')
#         logger.info(f'Dice выброшено: {result}')
#         return HttpResponse(result)
#
#
# def hundred(request):
#     try:
#         result = str(random.randint(0, 100))
#     except Exception as e:
#         logger.exception(f'Error in hundred roll: {e}')
#         return HttpResponse('Something went wrong.')
#     else:
#         logger.debug('Hundred roll page accessed.')
#         logger.info(f'Hundred выброшено: {result}')
#         return HttpResponse(result)
