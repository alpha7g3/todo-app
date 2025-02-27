#python basic calculator, countdown timer,math quiz
print("-----------------")
print("WELCOME TO THE MATH QUIZ")
question = (f"{1}.what is five(5) multiply by three(3)? ",
            f"{2}. what is the addition of ten(10) and seven(7)?",
            f"{3}. divide twenty-five(25) by five(5).")

option=(("A.2","B.15","C.19","D.5"),
        ("A.17","B.12","C.15","D.4"),
        ("A.7","B.16","C.41","D.5"))

ans= ("B","A","D")
score = 0
que_num = 0
for que in question:
   print("-----------------")
   print(que)
   for opt in option[que_num]:
       print(opt)

   guess = input("Enter (A,B,C,D):").upper()
   if guess in ['A','B','C','D'] :
       if guess == ans[que_num]:
           score += 1
           print("CORRECT!!")
       else:
           print("INCORRECT")
           print(f"{ans[que_num]} is the correct ans ")

   que_num += 1
score =round((score/len(question)) * 100,  2)
print("-" *15)
print(f"YOUR FINAL ANSWER IS {score}%")
print("-" *15)

import time
timee = int(input("enter the time in seconds: "))

for x in range(timee, 0, -1):
     seconds = x % 60
     minutes =int (x / 60) % 60
     hours = int (x / 3600)
     print(f"{hours:02},{minutes:02},{seconds:02}")
     time.sleep(1)
print("TIMES UP!!")

#fist step, users interface
while True:
    operator = input("enter an operator;  + - * / or press 'Q' to quit :")
    if operator.upper()== "Q":
        print("HAVE A NICE DAY ")
        break
    try:
     no_one = float(input("enter any digits :"))
     no_one2 =float(input("enter any digits "))
     if operator == "+":
        result = no_one + no_one2
        print(f"your ans is {result}")
     elif operator == "-":
         result = no_one - no_one2
         print(f"your ans is {result}")
     elif operator == "*":
         result = no_one * no_one2
         print(f"your ans is {result}")
     elif operator == "/":
         if no_one2 != 0:
           result= round(no_one / no_one2, 2)
           print(f"your ans is {result}")
         else :
           print("error:division by zero is not allowed")
     else :
        print(f"{operator} is not a valid ")
    except ValueError:
        print("Invalid input ! please enter a digit or number ")








