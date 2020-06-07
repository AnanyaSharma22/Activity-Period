from django.core.management.base import BaseCommand, CommandError
from app.lib.create_users import PopulateData

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('order_type', nargs='+', type=str)

    def handle(self, *args, **options):
        if 'users' in options['order_type']:
            obj = PopulateData()
            obj.read_file()
        else:
            raise CommandError('Enter "users"')
        self.stdout.write(self.style.SUCCESS(
            'Successfully Added Data %s' % (obj)))
