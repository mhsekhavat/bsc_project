import logging
import importlib
import inspect
from django.apps import AppConfig, apps

from insanity.sanity_check import SanityCheck

logger = logging.getLogger('insanity')

all_checks = []


class InsanityConfig(AppConfig):
    name = 'insanity'

    def ready(self):
        logging.info("Harvesting")
        for _, app in apps.app_configs.items():
            module = app.module
            check_name = module.__name__ + '.checks'
            try:
                checks = importlib.import_module(check_name)

                for name, obj in inspect.getmembers(checks, inspect.isclass):
                    if obj.__module__ == check_name and issubclass(obj, SanityCheck):
                        all_checks.append(obj)
            except:
                pass
