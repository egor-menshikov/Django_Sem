from django.core.management import BaseCommand

from ...models import Author, Article, Comment


class Command(BaseCommand):
    help = 'Create a new comment'

    def add_arguments(self, parser):
        parser.add_argument('author_pk', type=int, help='author primary key')
        parser.add_argument('article_pk', type=int, help='article primary key')
        parser.add_argument(
            '--c',
            action='store',
            dest='comment',
            type=str,
            default='',
            help='Comment message.',
        )

    def handle(self, *args, **options):
        author_pk = options.get('author_pk')
        author = Author.objects.filter(pk=author_pk).first()

        article_pk = options.get('article_pk')
        article = Article.objects.filter(pk=article_pk).first()

        text = options.get('comment')

        comment = Comment(
            author=author,
            article=article,
            commentary=text,
        )
        comment.save()

        self.stdout.write('Commentary post created.')
