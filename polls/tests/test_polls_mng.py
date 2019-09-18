from django.test import TestCase

from .lib.polls_request import PollsRequest


class PollsMng(TestCase):
    def setUp(self):
        self.polls_user = PollsRequest(self, 'user1')

    def test_polls_mng(self):
        print('*** test create question***')
        r = self.polls_user.create_question("what's up?")
        self.assertEqual(r['question_text'], "what's up?")

        r = self.polls_user.get_questions()
        self.assertEqual(len(r), 1)
        print(r)
