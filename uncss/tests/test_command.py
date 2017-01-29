from django.test import TestCase, override_settings
from django.conf import settings
from uncss.management.commands.uncss import Command
from django.template.loaders.filesystem import Loader


class CommandTest(TestCase):

    def test_get_loaders(self):
        command = Command()
        templates = settings.TEMPLATES[0]
        templates['OPTIONS']['loaders'] = [
            'django.template.loaders.filesystem.Loader',
        ]

        del templates['APP_DIRS']

        with override_settings(TEMPLATES=[templates]):
            self.assertEqual(1, len(command.get_loaders()))
            self.assertTrue(isinstance(command.get_loaders()[0], Loader))
