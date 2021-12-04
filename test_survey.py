import unittest
from survey import AnonymousSurvey

class TestSurvey(unittest.TestCase):
    """ Testing survey.py """
    def test_store_singleresponse(self):
        """ Testing weather single response is stored """
        question = 'Which language did you learned first ? '
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
    
    def test_store_threeresponse(self):
        """ Testing weather three response is stored"""
        question = 'Which language did you learned first ? '
        my_survey = AnonymousSurvey(question)
        responses = ['Hindi','English','Marathi']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main()