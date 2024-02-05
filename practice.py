total_point = 0
question = input ("What is my favorite food? ")
if question.lower ()== 'pasta': 
    total_point = total_point + 1
    print ('Correct')
else:
    print ('No point for you')

question = input ("How many days in a week? ")
if question == '7':
    total_point = total_point + 1
    print ('Correct')
else:
    print ('No point for you')

question = input ("How hour in a days? ")
if question == '24':
    total_point = total_point + 1
    print ('Correct')
else:
    print ('No point for you')

question = input ("How mintues in an hour? ")
if question == '60':
    total_point = total_point + 1
    print ('Correct')
else:
    print ('No point for you')

question = input ("How many meals a day? ")
if question == '3':
    total_point = total_point + 1
    print ('Correct')
else:
    print ('No point for you')

print (f"Your total point is: {int(total_point/5*100)}%")
