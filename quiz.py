score = 0

Quiz = {
    "question1": {
        "question": "What is the capital of Assryia?",
        "answer": ["Nineveh", "Babylon", "Assur", "Akkad"],
        "correct": "Assur",
    },
    "question2": {
        "question": "What is the capital of Babylonia?",
        "answer": ["Nineveh", "Babylon", "Assur", "Akkad"],
        "correct": "Babylon",
    },
    "question3": {
        "question": "What is the capital of Persia?",
        "answer": ["Nineveh", "Babylon", "Assur", "Akkad"],
        "correct": "Akkad",
    },
    "question4": {
        "question": "What is the capital of Sumeria?",
        "answer": ["Nineveh", "Babylon", "Assur", "Akkad"],
        "correct": "Nineveh",
    },
    "question5": {
        "question": "What is the capital of Egypt?",
        "answer": ["Alexandria", "Luxor", "Port Said", "Minya"],
        "correct": "Assur",
    },
    "question6": {
        "question": "What is the capital of Japan?",
        "answer": ["Tokyo", "Kyoto", "Osaka", "Nagoya"],
        "correct": "Tokyo",
    },
    "question7": {
        "question": "What is the capital of China?",
        "answer": ["Beijing", "Shanghai", "Tianjin", "Guangzhou"],
        "correct": "Beijing",
    },
    "question8": {
        "question": "What is the capital of India?",
        "answer": ["New Delhi", "Mumbai", "Chennai", "Kolkota"],
        "correct": "New Delhi",
    },
    "question9": {
        "question": "What is the capital of Indonesia?",
        "answer": ["Jakarta", "Surabaya", "Bandung", "Medan"],
        "correct": "Jakarta",
    },
    "question10": {
        "question": "What is the capital of Malaysia?",
        "answer": ["Kuala Lumpur", "Kuching", "Kuala Tere"],
        "correct": "Kuala Lumpur",
    },
}

for key, value in Quiz.items():
    print(value["question"])
    answer = input("Enter Answer: ")

    if answer.lower() == value["correct"].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("The correct answer is: " + value["correct"])


print("You got a percentage of: " + str(score / len(Quiz) * 100) + "%")
