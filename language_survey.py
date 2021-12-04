from survey import AnonymousSurvey

question = 'Which is the first language learned ? '
my_survey = AnonymousSurvey(question)
my_survey.show_question()
print('Enter q anytime to quit! ')
while True:
    response = input('language : ')
    if response == 'q':
        break
    my_survey.store_response(response)

print('Thankyou, everyone for participating in survey!')
my_survey.show_results()