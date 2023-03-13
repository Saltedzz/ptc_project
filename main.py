from responses import *

# Variables
user_answer = ""
question_mapping = {'1': [q1, q1_answer], '2': [q2, q2_answer], '3': [q3, q3_answer]}

# Introduction
print(opener, end = "\n\n")

# Main Menu with Questions
def main_menu():
    print(menu, end = "\n\n")
    user_answer = input(menu_options)
    # Invalid input error handling
    while user_answer not in ['1', '2', '3', 'exit']:
        print("Invalid input:")
        user_answer = input(menu_options)

    if user_answer == "exit":
        quit()

    handle_question(user_answer)


# Helper function to answer questions
def handle_question(q):
    question, answer = question_mapping[q]
    print()
    print(question + '\n' + sep + '\n' + answer + '\n' + sep + '\n')
    user_answer = input("Return to main menu? [y/n]: ")
    if user_answer.lower() == 'y':
        print()
        main_menu()
    else:
        quit()

main_menu()

