
def mini_quiz_game():

    questions = [
        {
            "question": "Which language is used for Android development?",
            "options": ["C", "Java", "HTML", "SQL"],
            "answer": 2
        },
        {
            "question": "Who developed Python?",
            "options": ["James Gosling", "Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup"],
            "answer": 2
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["function", "define", "def", "fun"],
            "answer": 3
        },
        {
            "question": "Which symbol is used for comments in Python?",
            "options": ["//", "#", "/*", "$"],
            "answer": 2
        },
        {
            "question": "Which data type stores True or False?",
            "options": ["int", "str", "bool", "float"],
            "answer": 3
        },
        {
            "question": "Which loop is used to iterate over a sequence?",
            "options": ["for", "switch", "do-while", "case"],
            "answer": 1
        },
        {
            "question": "Which function is used to display output?",
            "options": ["input()", "print()", "show()", "display()"],
            "answer": 2
        },
        {
            "question": "Which data structure stores key-value pairs?",
            "options": ["List", "Tuple", "Set", "Dictionary"],
            "answer": 4
        },
        {
            "question": "Which operator is used for exponentiation?",
            "options": ["*", "**", "//", "%"],
            "answer": 2
        },
        {
            "question": "Which function is used to find the length of a list?",
            "options": ["size()", "count()", "len()", "length()"],
            "answer": 3
        }
    ]

    score = 0

    print("\n================================")
    print("       MINI QUIZ GAME")
    print("================================")
    print("Answer the following questions!")

    for i, q in enumerate(questions, start=1):

        print(f"\nQuestion {i}: {q['question']}")

        for j, option in enumerate(q["options"], start=1):
            print(f"{j}. {option}")

        while True:
            try:
                answer = int(input("Enter your answer (1-4): "))

                if 1 <= answer <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")

            except ValueError:
                print("Invalid input! Enter a number.")

        if answer == q["answer"]:
            print("Correct Answer!")
            score += 1
        else:
            print("Wrong Answer!")
            print("Correct answer:", q["options"][q["answer"] - 1])

    total = len(questions)
    percentage = (score / total) * 100

    print("\n================================")
    print("          QUIZ RESULT")
    print("================================")
    print("Total Questions :", total)
    print("Correct Answers :", score)
    print("Wrong Answers   :", total - score)
    print(f"Percentage      : {percentage:.2f}%")

    if percentage >= 80:
        print("Grade: Excellent!")
    elif percentage >= 60:
        print("Grade: Very Good!")
    elif percentage >= 40:
        print("Grade: Good!")
    else:
        print("Grade: Keep Practicing!")

    print("================================")


while True:

    mini_quiz_game()

    choice = input("\nDo you want to play again? (yes/no): ").strip().lower()

    if choice != "yes":
        print("\nThank you for playing!")
        print("Have a great day!")
        break
        