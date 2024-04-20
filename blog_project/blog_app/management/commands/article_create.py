from django.core.management import BaseCommand

from ...models import Author, Article


class Command(BaseCommand):
    help = 'Create new article.'

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='title')
        parser.add_argument('author', type=int, help='author pk')
        parser.add_argument('category', type=str, help='category')

    def handle(self, *args, **options):
        title = options.get('title')
        author = Author.objects.filter(pk=options.get('author')).first()
        category = options.get('category')

        article = Article(
            title=title,
            content=f'This is an article on {category} by {author.full_name}',
            author=author,
            category=category,
            is_published=True,
        )

        article.save()
        self.stdout.write(f'Article {title} created.')
