import django
from django.test import TestCase
from ConfManager.models import UartServer


class UartServerTest(TestCase):

    def setUp(self) -> None:
        UartServer.objects.create(name='uart-2', url='telnet://123.123.234.234', port_count=16)

    def test_str(self):
        self.assertEqual('uart-2', str(UartServer.objects.get(name='uart-2')))

    def test_port_counts(self):
        self.assertEqual(16, UartServer.objects.get(name='uart-2').ports.count())

    def test_port_str(self):
        ports = UartServer.objects.get(name='uart-2').ports.all()
        self.assertEqual('uart-2:5', str(ports[4]))
        self.assertEqual('uart-2:3', str(ports[2]))

    def test_new(self):
        srv = UartServer()
        self.assertEqual(1, srv.port_count)
        self.assertEqual(1, srv.port_base)


if __name__ == '__main__':
    django.test.main()
