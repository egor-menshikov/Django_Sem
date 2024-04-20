from django.core.management import BaseCommand

from ...models import Article


class Command(BaseCommand):
    help = 'Update an existing article.'

    def add_arguments(self, parser):
        parser.add_argument(
            'pk',
            action='store',
            type=int,
            help='Article id (primary key)',
        )
        parser.add_argument(
            '--content',
            action='store',
            dest='content',
            type=str,
            default='',
            help='Content of the article.',
        )

    def handle(self, *args, **options):
        content = options.get('content')
        pk = options.get('pk')
        article = Article.objects.filter(pk=pk).first()
        article.content = content
        article.save()
        self.stdout.write('Article updated.')
