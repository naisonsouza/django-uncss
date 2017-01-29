from __future__ import unicode_literals
# flake8: noqa
import os
import sys
from fnmatch import fnmatch

from importlib import import_module

import django
from django.core.management.base import BaseCommand, CommandError
from django.template import Context
from django.utils import six
from django.utils.encoding import smart_text
from django.template.loader import get_template  # noqa Leave this in to preload template locations
from django.template import engines


class Command(BaseCommand):
    help = "Compress content outside of the request/response cycle"

    def add_arguments(self, parser):
        parser.add_argument(
            '--extension',
            '-e',
            action='append',
            default=['html'],
            dest='extensions',
            help='The file extension(s) to examine (default: ".html"), '
        )

    def get_loaders(self):
        template_source_loaders = []
        for e in engines.all():
            if hasattr(e, 'engine'):
                template_source_loaders.extend(
                    e.engine.get_template_loaders(e.engine.loaders)
                )

        loaders = []

        for loader in template_source_loaders:
            if hasattr(loader, 'loaders'):
                loaders.extend(loader.loaders)
            else:
                loaders.append(loader)

        return loaders

    def get_templates(self, extensions):
        templates = set()
        paths = []

        for loader in self.get_loaders():
            try:
                module = import_module(loader.__module__)
                get_template_sources = getattr(module, 'get_template_sources', None)
                if get_template_sources is None:
                    get_template_sources = loader.get_template_sources

                paths.extend(smart_text(origin) for origin in get_template_sources(''))

                for path in paths:
                    for root, dirs, files in os.walk(path, followlinks=True):
                        templates.update(
                            os.path.join(root, name) for name in files
                            if not name.startswith('.')
                            and any(fnmatch(name, "*%s" % glob) for glob in extensions)
                        )
            except (ImportError, AttributeError, TypeError):
                # Yeah, this didn't work out so well, let's move on
                pass

        return templates

    def handle(self, **kwargs):
        extensions = kwargs.get('extensions')
        templates = self.get_templates(extensions)

        for template in templates:
            print(template)


Command.requires_system_checks = False