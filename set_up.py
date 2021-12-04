import unittest
from survey import AnonymousSurvey
class TestSurvey(unittest.TestCase):
    """ Testing survey.py """
    def setUp(self):
        """ Testing single and multiple responses is stored correctly """
        question = 'Which language did you learned to speak first .'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Hindi','English','Marathi']
    
    def test_store_singleresponse(self):
        """ test single response is stored correctly """
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    def test_store_threeresponse(self):
        """ test multiple response is stored correctly """
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()