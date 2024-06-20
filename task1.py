import random

def catch_ball(player):
    chance = random.random()
    if chance < 0.7:
        print(f"{player} поймал мяч!")
        return True
    else:
        print(f"{player} не поймал мяч.")
        return False

def main():
    questions = [
        "Какое ваше любимое блюдо?",
        "Какой ваш любимый фильм?",
        "Куда бы вы хотели поехать в отпуск?",
        "Какое ваше хобби?",
        "Какой ваш любимый цвет?"
    ]
    
    answers = [
        "Мое любимое блюдо — пицца.",
        "Мой любимый фильм — 'Остров проклятых'.",
        "Я бы хотел поехать в Японию.",
        "Мое хобби — чтение книг.",
        "Мой любимый цвет — синий."
    ]
    
    players = ["Компьютер", "Вы"]
    current_player = "Компьютер"
    
    while True:
        print(f"\n{current_player} бросает мяч.")
        
        if current_player == "Компьютер":
            if catch_ball("Вы"):
                question = random.choice(questions)
                print(f"Вопрос: {question}")
                answer = input("Ваш ответ: ")
                print(f"Ваш ответ: {answer}")
                current_player = "Вы"
            else:
                print("Компьютер придумывает что-то...")
                current_player = "Вы"
        else:
            if catch_ball("Компьютер"):
                question = random.choice(questions)
                print(f"Вопрос: {question}")
                answer = random.choice(answers)
                print(f"Ответ Компьютера: {answer}")
                current_player = "Компьютер"
            else:
                question = random.choice(questions)
                print(f"Вопрос: {question}")
                answer = input("Ваш ответ: ")
                print(f"Ваш ответ: {answer}")
                current_player = "Компьютер"
        
        if input("\nПродолжить игру? (да/нет): ").strip().lower() != 'да':
            break

if __name__ == "__main__":
    main()
