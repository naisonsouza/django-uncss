import os
from django.test import TestCase, override_settings
from django.conf import settings
from uncss.management.commands.uncss import Command
from django.template.loaders.filesystem import Loader


class CommandTest(TestCase):

    def setUp(self):
        self.command = Command()

    def test_get_loaders(self):
        templates = settings.TEMPLATES[0]
        templates['OPTIONS']['loaders'] = [
            'django.template.loaders.filesystem.Loader',
        ]

        del templates['APP_DIRS']

        with override_settings(TEMPLATES=[templates]):
            self.assertEqual(1, len(self.command.get_loaders()))
            self.assertTrue(isinstance(self.command.get_loaders()[0], Loader))

    def test_get_templates(self):
        templates = self.command.get_templates(['html'])
        templates_test = [
            'base.html',
            'content.html',
        ]
        self.assertEqual(2, len(templates))
        self.assertTrue(all([os.path.basename(path) in templates_test for path in templates]))
