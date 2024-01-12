from django.test import TestCase
from writers.models import writer

class writerTestCase(TestCase):
    def setUp(self):
        writer.objects.create(first_name='Aman',email='helloaman404@gmail.com',password='dora',writer_id='aman')
        writer.objects.create(first_name='admin',email='admin@gmail.com',password='cdac123',writer_id='admcda')
    
    def test_correct_writer_id(self):
        w=writer.objects.get(writer_id='admcda')
