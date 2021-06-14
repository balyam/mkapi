from django.core.management import BaseCommand
from mkapi.settings import BASE_DIR
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'will load branch data from JSON'