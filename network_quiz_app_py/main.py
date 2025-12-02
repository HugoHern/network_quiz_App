import json
import random

# Load questions
with open('questions.json') as f:
    questions = json.load(f)

random.shuffle(questions)
score = 0

for q in questions:
    print("\n" + q['question'])
    for i, choice in enumerate(q['choices'], 1):
        print(f"{i}. {choice}")
    
    while True:
        try:
            answer = int(input("Your answer (1-4): "))
            if 1 <= answer <= len(q['choices']):
                break
            else:
                print("Choose a valid number.")
        except:
            print("Please enter a number.")
    
    if q['choices'][answer-1] == q['answer']:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer: {q['answer']}")

print(f"\nYour final score: {score}/{len(questions)}")
