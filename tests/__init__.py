from django.test import TestCase
from django.utils import timezone


class BaseTestCase(TestCase):
    def setUp(self):
        self.data_set = {'title': 'A Snippet', 'code': 'print "Hello World!"',
                         'linenos': True, 'language': 'python', 'rating': 0.0,
                         'posted_date': timezone.now(), 'comment': 'Comment',
                         'watermark': 'TEST'}
