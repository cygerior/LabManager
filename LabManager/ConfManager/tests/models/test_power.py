import django
from django.test import TestCase
from ConfManager.models import PowerController


class MyTestCase(TestCase):

    def setUp(self) -> None:
        PowerController.objects.create(name='Power 1', url='WTI::123.234.231.221::3001')
        PowerController.objects.create(name='Power 2', url='RACK::120.32.43.23::3001')

    def test_str(self):
        self.assertEqual('Power 1', str(PowerController.objects.get(name='Power 1')))


if __name__ == '__main__':
    django.test.main()
