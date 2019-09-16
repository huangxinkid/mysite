from django.test import TestCase

from .lib.polls_request import PollsRequest

class PollsMng(TestCase):
    def setUp(self):
        self.polls_user = PollsRequest(self, 'user1')

    def test_polls_mng(self):
        r = self.polls_user.get_questions()
        print(r)