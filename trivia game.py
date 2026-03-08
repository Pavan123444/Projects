# Python Trivia Game
import random
# here we store questions and answers
questions = {
"what is the keyword to define a function in Python?": "def",
"which data type is used to store True or False values?": "boolean",
"what is the correct file extension for Python files?": ".py",
"which symbol is used to comment in Python?": "#",
"what function is used to get input from the user?": "input",
"how do you start a for loop in Python?": "for",
"what is the output of 2 ** 3 in Python?": "8",
"what keyword is used to import a module in Python?": "import",
"what does the len() function return?": "length",
"what is the result of 10 // 3 in Python?": "3"
}
# function to run the game
def python_trivia_game():
    score = 0
    total_questions = 5
    # convert questions to list
    question_list = list(questions.keys())
    # pick 5 random questions
    random_questions = random.sample(question_list, total_questions)
    # ask questions one by one
    for i, q in enumerate(random_questions):
        print(f"\nQuestion {i+1}: {q}")
        # get answer from user
        answer = input("Your answer: ").lower().strip()
        # check correct answer
        if answer == questions[q].lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            print("Correct answer:", questions[q])
    # show final score
    print("\nGame Finished!")
    print("Your score:", score, "/", total_questions)
# start the game
python_trivia_game()