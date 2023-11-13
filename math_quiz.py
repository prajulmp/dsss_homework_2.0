import random

def generate_random_integer(min_value, max_value): #Selecting a random integer for the quiz
    """
    Generate a random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value) #returing the random integer

def choose_random_operator(): #selecting a random math operator
    return random.choice(['+', '-', '*']) #returning a random math function

def calculate_expression(num1, num2, operator):
    expression = f"{num1} {operator} {num2}"
    if operator == '+': result = num1 + num2 #Addition
    elif operator == '-': result = num1 - num2 #Sutraction
    else: result = num1 * num2 #Multiplication
    return expression, result

def run_math_quiz():
    score = 0
    total_questions = 3 #total question numbers 

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to give the correct answers for the following problem to test your math skills.")

    for _ in range(total_questions): #run loop for total questions
        num1 = generate_random_integer(1, 10) #function to select the random number
        num2 = generate_random_integer(1, 5) #function to select the random number
        operator = choose_random_operator() #function to select the random operator 

        problem, answer = calculate_expression(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")
        user_answer = int(user_answer)

        if user_answer == answer: #Checks the answer is right or wrong
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}") #printing the score

if __name__ == "__main__":
    run_math_quiz()