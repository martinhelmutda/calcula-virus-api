from django.core.management.base import BaseCommand
from calculavirus.insumos.models import *
import random

# python manage.py seed --mode=refresh

""" Clear all data and creates Lugares """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    print("Delete Lugares instances")
    LugarCompra.objects.all().delete()


def create_lugares():
    """Creates an Lugares object combining different elements from the list"""
    print("Creating Lugares")

    lugar = LugarCompra(
    nombre='Mercado',
    descripcion='Lugar para comprar productos locales',
    img='http://localhost:8000/media/market.jpg'
    )
    lugar.save()
    print("{} place created.".format(lugar))

    lugar = LugarCompra(
    nombre='Super',
    descripcion='Lugar para comprar productos de empresas',
    img='http://localhost:8000/media/super.jpg'
    )
    lugar.save()
    print("{} place created.".format(lugar))

    lugar = LugarCompra(
    nombre='Otro',
    descripcion='Lugar para comprar otros productos',
    img='http://localhost:8000/media/store.png'
    )
    lugar.save()
    print("{} place created.".format(lugar))

def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    create_lugares()
