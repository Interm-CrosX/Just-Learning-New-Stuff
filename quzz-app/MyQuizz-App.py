# Simple Quiz App

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    }
]

score = 0

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()
    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is " + q["answer"])
    print()

print(f"Your final score is {score}/{len(questions)}")
