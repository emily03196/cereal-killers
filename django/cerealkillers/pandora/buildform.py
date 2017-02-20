from pandora.models import Question, MCChoice
from django.utils import timezone

Question_1 = Question(question_text="What restaurants have you been to previously and liked?", pub_date=timezone.now())
Question_1.save()
Question_2 = Question(question_text="What cuisine would you like to eat now?", pub_date=timezone.now())
Question_2.save()
Question_3 = Question(question_text="What price range would you like to get now?", pub_date=timezone.now())
Question_3.save()
Question_4 = Question(question_text="What rating would you like to get now?", pub_date=timezone.now())
Question_4.save()
Question_5 = Question(question_text="What is your current location?", pub_date=timezone.now())
Question_5.save()
Question_6 = Question(question_text="How far would you be willing to travel?", pub_date=timezone.now())
Question_6.save()
Question_7 = Question(question_text="What is your arrival time?", pub_date=timezone.now())
Question_7.save()