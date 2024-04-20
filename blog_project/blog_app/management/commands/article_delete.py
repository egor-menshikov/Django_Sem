from django.core.management import BaseCommand

from ...models import Article


class Command(BaseCommand):
    help = 'Delete an article.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Primary key of the article')

    def handle(self, *args, **options):
        if article := Article.objects.filter(pk=options.get('pk')).first():
            self.stdout.write(f'Deleting {article.title}..')
            article.delete()
            self.stdout.write('OK.')
        else:
            self.stdout.write('No article under such primary key.')
