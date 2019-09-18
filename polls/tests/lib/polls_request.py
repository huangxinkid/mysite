from rest_framework import status

from lib.lib4test.test_base import TestBase


class PollsRequest(TestBase):
    def create_question(self, question_text, status_code=status.HTTP_201_CREATED):
        url = '/polls/questionv/'
        data = {'question_text': question_text}
        return self.post(url, data=data, status_code=status_code)

    def get_questions(self, status_code=status.HTTP_200_OK):
        url = '/polls/questionv/'
        return self.get(url, status_code=status_code)
