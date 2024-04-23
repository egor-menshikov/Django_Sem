from django.shortcuts import render
import logging

from django.views import View
from django.views.generic import TemplateView

logger = logging.getLogger(__name__)


class IndexView(View):
    def get(self, request):
        return render(request, 'personal_info_app/index.html')


class AboutTemplate(TemplateView):
    template_name = 'personal_info_app/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Егор'
        return context
