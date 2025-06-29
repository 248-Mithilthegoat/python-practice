questions = {
    "How many eyes do spiders have?":['a. 92', 'b. 8', 'c. 45', 'd. 1002', 'b'],
    "How fast is Usain Bolt?":['a. 27 mph', 'b. 26 mph', 'c. 25 mph', 'd. 28 mph', 'a'],
    "What is five factorial?":['a. 125', 'b. 130', 'c. 120', 'd. 140', 'c'],
    "How many exact days are in a year?":['a. 365', 'b. 365 1/8', 'c. 365 1/2', 'd. 365 1/4', 'd'],
    "How tall is the Eiffel Tower?":['a. 350m', 'b. 465m', 'c. 765ft', 'd. 1150ft', 'a' ],
    "What year was the NBA founded?":['a. 1946', 'b. 1949', 'c. 1943', 'd. 1941', 'a'],
    "Which national team has the most cricket ODI championships?":['a. India', 'b. Australia', 'c. West Indies', 'd. England', 'b'],
    "What year did the Berlin Wall fall?":['a. 1990', 'b. 1987', 'c. 1989', 'd. 1991', 'c'],
    "Which ancient civilization is credited with the invention of the wheel around 3500 B.C.?":['a. The Sumerians', 'b. The Romans', 'c. The Egyptians', 'd. The Assyrians', 'a'],
    "Who was the first woman to win the Nobel Prize, and in which field did she win it?":['a. Toni Morrison - Literature', 'b. Malala Yousafzai - Peace', 'c. Wangari Maathai - Peace', 'd. Marie Curie - Physics', 'd']
}

score = 0
for question_number,question in enumerate(questions):
    print("Question", question_number+1)
    print(question)
    for options in questions[question][:-1]:
        print(options)
    user_choice = input("Make your choice: ")
    if user_choice == questions[question][-1]:
        print("CORRECT!!!!!")
        score += 1
    
    else:
        print("WRONG!!!!!")

print(str(score) + "/" + str(question_number + 1))
if score == 10:
    print("You got a 100%, A+")
elif score == 9:
    print("You got a 90%, A")
elif score == 8:
    print("You got a 80%, B")
elif score == 7:
    print("You got a 70%, C")
elif score == 6:
    print("You got a 60%, D")
elif score == 5:
    print("You got a 50%, F")
elif score == 4:
    print("You got a 40%, F")
elif score == 3:
    print("You got a 30%, F")
elif score == 2:
    print("You got a 20%, F")
elif score == 1:
    print("You got a 10%, F")
elif score == 0:
    print("You got a 0%, F-")