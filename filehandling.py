# Function to register a new user
def register():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")
    with open('users.txt', 'a') as f:
        f.write(f"{username},{password}\n")
    print("Registration successful!")

# Function to login a user
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open('users.txt', 'r') as f:
        users = f.readlines()
    for user in users:
        user = user.strip().split(',')
        if user[0] == username and user[1] == password:
            print("Login successful!")
            return username
    print("Invalid username or password.")
    return None

# Function to load quiz questions from a file
def load_questions(subject):
    questions = []
    with open(f'{subject}_quiz.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            question, answer = line.strip().split(',')
            questions.append((question, answer))
    return questions

# Function to take a quiz
def take_quiz(username, subject):
    questions = load_questions(subject)
    score = 0
    for question, answer in questions:
        print(question)
        user_answer = input("Your answer: ")
        if user_answer.lower() == answer.lower():
            score += 1
    with open('results.txt', 'a') as f:
        f.write(f"{username},{subject},{score}\n")
    print(f"Quiz completed! Your score: {score}/{len(questions)}")

# Function to view quiz results
def view_results(username):
    with open('results.txt', 'r') as f:
        results = f.readlines()
    for result in results:
        result = result.strip().split(',')
        if result[0] == username:
            print(f"Subject: {result[1]}, Score: {result[2]}")

# Main function to run the quiz application
def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register()
        elif choice == '2':
            username = login()
            if username:
                while True:
                    print("\n1. Take Quiz\n2. View Results\n3. Logout")
                    choice = input("Enter your choice: ")
                    if choice == '1':
                        print("\nChoose a subject:\n1. Python\n2. Java\n3. C++")
                        subject_choice = input("Enter your choice: ")
                        subjects = { '1': 'python', '2': 'java', '3': 'cpp' }
                        subject = subjects.get(subject_choice)
                        if subject:
                            take_quiz(username, subject)
                        else:
                            print("Invalid subject choice.")
                    elif choice == '2':
                        view_results(username)
                    elif choice == '3':
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
