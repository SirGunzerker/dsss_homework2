import random
def Random_max_min_selector(minimum, maximum):
    """
    Generates a random integer between the specified minimum and maximum values (inclusive).
    Parameters:
    - minimum (int): The minimum value for the random integer.
    - maximum (int): The maximum value for the random integer.
    Returns:
    - int: A randomly selected integer between the specified minimum and maximum values.
    """
    try:
        # Attempt to convert minimum and maximum to integers
        minimum = int(minimum)
        maximum = int(maximum)
    except NonIntegerError:
        # Handle the case where the entered values are not an integer
        print("Entered value is not an integer. Please enter an integer value.")
        return None
    # Use the randint function from the random module to generate a random integer
    selected_integer = random.randint(minimum, maximum)
    # Return the randomly selected integer
    return selected_integer



def Random_return_operator():
    """
    Randomly selects and returns one of the arithmetic operators: '+', '-', or '*'.

    Returns:
    - str: A randomly selected arithmetic operator.
    """
    # Use the choice function from the random module to randomly select an operator from the list
    selected_operator = random.choice(['+', '-', '*'])

    # Return the randomly selected operator
    return selected_operator

def perform_math_operation(number1, number2, operator):
    """
    Executes a mathematical operation on two numbers based on the specified operator.

    Parameters:
    - number1 (float or int): The first operand.
    - number2 (float or int): The second operand.
    - operator (str): The arithmetic operator ('+', '-', or '*').

    Returns:
    - tuple: A tuple containing a formatted string representation of the operation
             ("number1 operator number2") and the computed result.
    """
    try:
        # Checking if the entered operator is right and the entries are integer entries
        # Construct a string representation of the mathematical operation
        operation_string = f"{number1} {operator} {number2}"

        # Perform the mathematical operation according to the specified operator
        if operator == '+':
            result = number1 + number2
        elif operator == '-':
            result = number1 - number2
        elif operator == '*':
            result = number1 * number2
        else:
            print("Wrong operator entered. Please enter '+', '-' or '*'")
    except ZeroDivisionError:
        # When dividing by zero, an error occurs
        print("Error: Dividing by zero is not possible")
        return None
        # Return a tuple containing the operation string and the computed result
    return operation_string, result


def run_math_quiz():
    """
    Executes a math quiz game featuring randomly generated arithmetic problems.

    Users are presented with questions and are required to input the correct answers.

    Returns:
    - None
    """
    # Initialize the player's score and set the total number of quiz questions
    player_score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Challenge!")
    print("Prepare to solve math problems and earn points for each correct answer.")

    # Iterate through the specified number of quiz questions
    for _ in range(total_questions):
        # Generate random numbers and an operator for the math problem
        num1 = Random_max_min_selector(1, 10)
        num2 = Random_max_min_selector(1, 5.5)
        operator = Random_return_operator()

        # Get the problem and its correct answer
        math_problem, correct_answer = Math_operator(num1, num2, operator)

        # Display the question and retrieve the user's answer
        print(f"\nQuestion: {math_problem}")
        user_answer = input("Your answer: ")
        user_answer = int(user_answer)

        # Check if the user's answer is correct and update the score
        if user_answer == correct_answer:
            print("Correct! You've earned a point.")
            player_score += 1
        else:
            print(f"Oops! The correct answer is {correct_answer}.")

    # Display the final score
    print(f"\nGame over! Your total score is: {player_score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
