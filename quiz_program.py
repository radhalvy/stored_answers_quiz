def get_answer():
    user_answer = input("\nAnswer: ")
    return user_answer


def get_name():
    name = input("\nEnter your full name: ")
    return name


def exam():
    name = get_name()
    questions = ["What's your favorite color?", "What's the color of the sky?",
                 "How do you feel about the war?"]
    for question in questions:
        print(f"\n{question}")
        user_answer = get_answer()
        with open("answers.txt", "a") as answers:
            answers.write(f"{name} || {question} --> {user_answer}\n")
    with open("answers.txt", "a") as answers:
        answers.write("\n\n")


exam()
