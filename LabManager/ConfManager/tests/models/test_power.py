import django
from django.test import TestCase
from ConfManager.models import PowerController


class MyTestCase(TestCase):

    def setUp(self) -> None:
        PowerController.objects.create(name='Power 1', url='WTI::123.234.231.221::3001', port_count=5)
        PowerController.objects.create(name='Power 2', url='RACK::120.32.43.23::3001', port_base=5, port_count=8)

    def test_str(self):
        self.assertEqual('Power 1', str(PowerController.objects.get(name='Power 1')))

    def test_port_counts(self):
        self.assertEqual(5, PowerController.objects.get(name='Power 1').ports.count())
        self.assertEqual(8, PowerController.objects.get(name='Power 2').ports.count())

    def test_port_str(self):
        self.assertEqual('Power 1:1', str(PowerController.objects.get(name='Power 1').ports.all()[0]))
        self.assertEqual('Power 2:7', str(PowerController.objects.get(name='Power 2').ports.all()[2]))


if __name__ == '__main__':
    django.test.main()
