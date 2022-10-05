import django
from django.test import TestCase
from ConfManager.models import BackplaneGroup


class BackplaneGroupTest(TestCase):

    def setUp(self) -> None:
        BackplaneGroup.objects.create(name='bkp-1')
        BackplaneGroup.objects.create(name='bkp-2')

    def test_str(self):
        self.assertEqual('bkp-1', str(BackplaneGroup.objects.get(name='bkp-1')))

    def test_port_counts(self):
        self.assertEqual(8, BackplaneGroup.objects.get(name='bkp-1').ports.count())

    def test_port_str(self):
        self.assertEqual('bkp-1:5', str(BackplaneGroup.objects.get(name='bkp-1').ports.all()[5]))
        self.assertEqual('bkp-2:3', str(BackplaneGroup.objects.get(name='bkp-2').ports.all()[3]))

    def test_new(self):
        bkpl = BackplaneGroup()
        self.assertEqual(8, bkpl.port_count)
        self.assertEqual(0, bkpl.port_base)


if __name__ == '__main__':
    django.test.main()
