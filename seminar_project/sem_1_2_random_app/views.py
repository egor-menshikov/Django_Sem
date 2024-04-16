from django.shortcuts import render
import random
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def coin(request):
    try:
        result = random.choice(['Heads', 'Tails'])
    except Exception as e:
        logger.exception(f'Error in coin toss: {e}')
        return HttpResponse('Something went wrong.')
    else:
        logger.debug('Coin toss page accessed.')
        logger.info(f'Coin выброшено: {result}')
        return HttpResponse(result)


def dice(request):
    try:
        result = str(random.randint(1, 6))
    except Exception as e:
        logger.exception(f'Error in dice throw: {e}')
        return HttpResponse('Something went wrong.')
    else:
        logger.debug('Dice throw page accessed.')
        logger.info(f'Dice выброшено: {result}')
        return HttpResponse(result)


def hundred(request):
    try:
        result = str(random.randint(0, 100))
    except Exception as e:
        logger.exception(f'Error in hundred roll: {e}')
        return HttpResponse('Something went wrong.')
    else:
        logger.debug('Hundred roll page accessed.')
        logger.info(f'Hundred выброшено: {result}')
        return HttpResponse(result)
