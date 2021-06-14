from django.core.management import BaseCommand
from mkapi.settings import BASE_DIR
from main.models import BranchModel
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'will load branch data from JSON'

    def handle(self, *args, **options):
        try:
            path = BASE_DIR / 'main/db/load_to_db.py'
            exec(open(path).read())

        except Exception as e:
            logger.warning(e, exc_info=True)