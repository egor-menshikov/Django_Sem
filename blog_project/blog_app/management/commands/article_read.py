from django.core.management import BaseCommand

from ...models import Article


class Command(BaseCommand):
    help = 'Read an article.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Primary key of the article')

    def handle(self, *args, **options):
        pk = options.get('pk')
        article = Article.objects.filter(pk=pk).first()
        self.stdout.write(f'{article}')
