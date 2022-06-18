from django.core.management.base import BaseCommand
from categories.models import Category


class Command(BaseCommand):
    help = "This command seeds categories"

    def handle(self, *args, **options):
        for genre in Category.all_category(Category.objects):
            Category.objects.get_or_create(
                name=genre,
                kind=Category.KIND_BOTH
            )
        self.stdout.write(self.style.SUCCESS('Categories created!'))
