from django.shortcuts import render
import logging

from django.views import View
from django.views.generic import TemplateView

logger = logging.getLogger(__name__)

_ABOUT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About me</title>
</head>
<body>
<p>Меня зовут Егор, я учусь на веб-разработчика.</p>
</body>
</html>
"""


class IndexView(View):
    def get(self, request):
        return render(request, 'personal_info_app')


class AboutTemplate(TemplateView):
    pass
