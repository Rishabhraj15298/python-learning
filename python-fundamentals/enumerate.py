# MARKING WRONG ANSWERS IN A QUIZ USING ENUMERATE 

answers = ['A', 'C', 'B', 'D', 'A']
student_answers = ['A', 'C', 'D', 'D', 'A']

for index , (correct , student) in enumerate(zip(answers , student_answers) , start=1):
    if(correct == student):
        print(f"Question {index} : Correct")
    else:
        print(f"Question {index} : Wrong  (Your answer : {student} , Correct answer : {correct} )" )
        
