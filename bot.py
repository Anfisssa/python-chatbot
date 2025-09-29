import datetime

def get_bot_response(user_input):
    """
    Анализирует ввод пользователя и возвращает ответ бота.
    """
    # Приводим ввод пользователя к нижнему регистру для простоты сравнения
    user_input = user_input.lower()

    if "привет" in user_input:
        return "Привет! Чем могу помочь?"
    elif "как дела" in user_input:
        return "Отлично! Я готов к работе. А у тебя как?"
    elif "который час" in user_input or "время" in user_input:
        now = datetime.datetime.now()
        return f"Текущее время: {now.strftime('%H:%M:%S')}."
    elif "пока" in user_input or "выход" in user_input:
        return "exit"
    else:
        return "Я тебя не понимаю. Попробуй спросить что-нибудь другое, например 'привет' или 'который час'."

def main():
    """
    Главная функция для запуска бота.
    """
    print("🤖 Чат-бот запущен! Напиши 'пока' или 'выход', чтобы завершить.")
    
    while True:
        user_text = input("Вы: ")
        response = get_bot_response(user_text)
        
        if response == "exit":
            print("Бот: До скорой встречи!")
            break
        
        print(f"Бот: {response}")

if __name__ == "__main__":
    main()
