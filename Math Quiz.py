import random
import time

def generate_problem(level):
    if level == 1:
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        operator = random.choice(['+', '-'])
    elif level == 2:
        num1, num2 = random.randint(1, 20), random.randint(1, 20)
        operator = random.choice(['+', '-', '*'])
    else:
        num1, num2 = random.randint(1, 50), random.randint(1, 50)
        operator = random.choice(['+', '-', '*', '/'])
        # Ensure no division by zero and integer division for level 3
        if operator == '/':
            while num2 == 0 or num1 % num2 != 0:
                num1, num2 = random.randint(1, 50), random.randint(1, 50)

    return num1, num2, operator

def calculate_answer(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 // num2

def math_quiz_adventure():
    lives = 3
    level = 1
    score = 0

    print("Welcome to the Math Quiz Adventure Game!")
    
    # Ask the user if they want to start the game
    start_game = input("Do you want to start the game? (yes/no): ").lower()
    
    if start_game != 'yes':
        print("Maybe next time! Goodbye!")
        return
    print("Solve math problems to advance levels. Each incorrect answer costs a life!")

    while lives > 0:
        print(f"\n--- Level {level} ---")
        num1, num2, operator = generate_problem(level)
        correct_answer = calculate_answer(num1, num2, operator)
        
        # Display the problem
        print(f"Solve: {num1} {operator} {num2}")
        
        # Timer starts
        start_time = time.time()
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # Timer ends
        end_time = time.time()
        time_taken = end_time - start_time

        if user_answer == correct_answer:
            print("Correct! Well done.")
            score += 10 * level - int(time_taken)  # Bonus points for faster answers
            print(f"Time taken: {round(time_taken, 2)} seconds. Your score: {score}")
            level += 1  # Progress to the next level
        else:
            lives -= 1
            print(f"Incorrect! The correct answer was {correct_answer}. Lives remaining: {lives}")
    
    print("\nGame over! Final score:", score)

#Run the game
math_quiz_adventure()
