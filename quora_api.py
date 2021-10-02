#pip install quora
from quora import User, Quora

user = User('Christopher-J-Su')
activity = user.activity
print(activity)

question = Quora.get_question_stats('what-is-python')
print(question)

answer = Quora.get_one_answer('http://qr.ae/6hARL')
answer = Quora.get_one_answer('6hARL')
latest_answers = Quora.get_latest_answers('what-is-python')