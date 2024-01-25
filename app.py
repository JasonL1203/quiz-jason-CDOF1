import os
def load_questions(file_path):
    questions = []

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        i = 0

        while i < len(lines):
            question_text = lines[i].strip()
            i += 1

            options = []

            # Ajouter cela dans la boucle interne
            while i < len(lines) and not lines[i].startswith("Réponse"):
                options.append(lines[i].strip())
                i += 1
                # Commenter la ligne pour ne pas afficher le traitement des options
                # print("Traitement des options, ligne actuelle :", lines[i-1])

            # Modifier la recherche de la réponse correcte
            correct_answer_lines = [line for line in lines[i:] if line.startswith("Réponse")]

            if correct_answer_lines:
                correct_answer_line = correct_answer_lines[0]
                correct_answer = correct_answer_line.split(":")[1].strip().lower()

                questions.append({"text": question_text, "options": options, "answer": correct_answer})
            else:
                print(f"Aucune réponse trouvée pour la question : {question_text}")

            i += 1  # Passer à la question suivante

    # Commenter cette section pour ne pas afficher les détails des questions
    # for question in questions:
    #     print("Question:", question["text"])
    #     print("Options:", question["options"])
    #     print("Réponse:", question["answer"])
    #     print()

    return questions


def display_question(question):
    print("\nQuestion: {}".format(question["text"]))

    for option in question["options"]:
        print(option)

    user_answer = input("Votre réponse (A, B, C, D) : ").lower()
    return user_answer == question["answer"]

def run_quiz(questions):
    score = 0

    for question in questions:
        if display_question(question):
            print("Correct!")
            score += 1
        else:
            print("Incorrect. La réponse correcte était {}.".format(question["answer"].upper()))

    print("\nFin du quiz. Votre score est {}/{}".format(score, len(questions)))

def main():
    print("Bienvenue dans le Quiz Game!")

    # Charger les questions depuis le fichier unique
    questions = load_questions("questions.txt")  # Utilisez le nom du fichier

    # Exécuter le quiz
    run_quiz(questions)

if __name__ == "__main__":
    main()

