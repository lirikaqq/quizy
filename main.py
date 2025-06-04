import telebot
from telebot import types
from telebot.util import quick_markup
from typing import Dict, List, Any

# Конфигурация
TOKEN = ""
bot = telebot.TeleBot(TOKEN)

# Константы
QUESTIONS_PER_QUIZ = 5
TOPICS = ["📜 История", "🔬 Наука", "🎬 Кино"]

# Типы данных
QuizQuestion = Dict[str, Any]
QuizTopic = Dict[str, List[QuizQuestion]]
UserData = Dict[str, int | str]

# Вопросы по темам
QUIZ_DATA: QuizTopic = {
    TOPICS[0]: [
        {
            "question": "<b>Кто был первым президентом России?</b>",
            "options": ["Борис Ельцин", "Владимир Путин", "Михаил Горбачев"],
            "answer": "Борис Ельцин",
        },
        {
            "question": "<b>В каком году началась Вторая мировая война?</b>",
            "options": ["1939", "1941", "1945"],
            "answer": "1939",
        },
        {
            "question": "<b>Как звали первого царя России?</b>",
            "options": ["Иван Грозный", "Петр I", "Александр I"],
            "answer": "Иван Грозный",
        },
        {
            "question": "<b>Когда распался СССР?</b>",
            "options": ["1991", "1989", "1993"],
            "answer": "1991",
        },
        {
            "question": "<b>Кто написал 'Капитал'?</b>",
            "options": ["Карл Маркс", "Фридрих Ницше", "Ленин"],
            "answer": "Карл Маркс",
        },
    ],
    TOPICS[1]: [
        {
            "question": "<b>Какой газ преобладает в атмосфере Земли?</b>",
            "options": ["Азот", "Кислород", "Углекислый газ"],
            "answer": "Азот",
        },
        {
            "question": "<b>Сколько элементов в таблице Менделеева?</b>",
            "options": ["118", "92", "150"],
            "answer": "118",
        },
        {
            "question": "<b>Как называется самая большая часть клетки?</b>",
            "options": ["Ядро", "Цитоплазма", "Митохондрия"],
            "answer": "Цитоплазма",
        },
        {
            "question": "<b>Кто открыл пенициллин?</b>",
            "options": ["Александр Флеминг", "Луи Пастер", "Илья Мечников"],
            "answer": "Александр Флеминг",
        },
        {
            "question": "<b>Какой элемент обозначается как 'Fe'?</b>",
            "options": ["Золото", "Железо", "Серебро"],
            "answer": "Железо",
        },
    ],
    TOPICS[2]: [
        {
            "question": "<b>Кто режиссер фильма 'Крестный отец'?</b>",
            "options": ["Мартин Скорсезе", "Фрэнсис Форд Коппола", "Стивен Спилберг"],
            "answer": "Фрэнсис Форд Коппола",
        },
        {
            "question": "<b>Какой фильм получил первого 'Оскара'?</b>",
            "options": ["Унесенные ветром", "Крылья", "Метрополис"],
            "answer": "Крылья",
        },
        {
            "question": "<b>Кто играл Нео в 'Матрице'?</b>",
            "options": ["Брэд Питт", "Киану Ривз", "Том Круз"],
            "answer": "Киану Ривз",
        },
        {
            "question": "<b>Сколько 'Оскаров' получил 'Титаник'?</b>",
            "options": ["5", "11", "3"],
            "answer": "11",
        },
        {
            "question": "<b>Какой фильм самый кассовый в истории?</b>",
            "options": ["Аватар", "Мстители: Финал", "Титаник"],
            "answer": "Аватар",
        },
    ],
}

# Хранение данных пользователей
user_data: Dict[int, UserData] = {}


def create_welcome_message() -> str:
    """Создает приветственное сообщение."""
    return (
        "🌟 <b>Добро пожаловать в викторину!</b> 🌟\n\n"
        "Выберите тему, которая вас интересует, и проверьте свои знания!\n\n"
        f"{TOPICS[0]} - проверим знание важных событий\n"
        f"{TOPICS[1]} - вопросы о мире вокруг нас\n"
        f"{TOPICS[2]} - проверьте свою эрудицию в киноискусстве\n\n"
        "👇 <b>Выберите тему:</b>"
    )


def create_quiz_start_message(topic: str) -> str:
    """Создает сообщение о начале викторины."""
    return (
        f"📯 <b>Начинаем викторину по теме: {topic}</b> 📯\n\n"
        f"Будет {QUESTIONS_PER_QUIZ} вопросов с вариантами ответов. "
        "Выбирайте внимательно!\n\n"
        "➖➖➖➖➖➖➖➖➖"
    )


def create_question_text(question_num: int, question: str) -> str:
    """Форматирует текст вопроса."""
    return (
        f"<b>Вопрос {question_num}/{QUESTIONS_PER_QUIZ}</b>\n"
        f"{question}\n\n"
        "➖➖➖➖➖➖➖➖➖"
    )


def create_result_message(topic: str, score: int) -> str:
    """Создает сообщение с результатами викторины."""
    return (
        f"🎉 <b>Викторина завершена!</b> 🎉\n\n"
        f"Тема: <i>{topic}</i>\n"
        f"Ваш результат: <b>{score}/{QUESTIONS_PER_QUIZ}</b>\n\n"
        f"{get_result_emoji(score)} {get_result_comment(score)}"
    )


def get_result_emoji(score: int) -> str:
    """Возвращает эмодзи в зависимости от результата."""
    if score == QUESTIONS_PER_QUIZ:
        return "🏆"
    if score >= 3:
        return "👍"
    return "😕"


def get_result_comment(score: int) -> str:
    """Возвращает комментарий в зависимости от результата."""
    if score == QUESTIONS_PER_QUIZ:
        return "Отличный результат! Вы настоящий эксперт!"
    if score >= 3:
        return "Хороший результат! Можно еще немного подтянуть знания."
    return "Попробуйте еще раз, у вас обязательно получится!"


@bot.message_handler(commands=['start'])
def start(message: types.Message) -> None:
    """Обработчик команды /start."""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [types.KeyboardButton(topic) for topic in QUIZ_DATA]
    markup.add(*buttons)

    bot.send_message(
        message.chat.id,
        create_welcome_message(),
        reply_markup=markup,
        parse_mode='HTML'
    )


@bot.message_handler(func=lambda message: message.text in QUIZ_DATA)
def start_quiz(message: types.Message) -> None:
    """Начинает викторину по выбранной теме."""
    topic = message.text
    user_data[message.chat.id] = {
        "topic": topic,
        "score": 0,
        "current_question": 0,
    }

    bot.send_message(
        message.chat.id,
        create_quiz_start_message(topic),
        reply_markup=types.ReplyKeyboardRemove(),
        parse_mode='HTML'
    )

    ask_question(message.chat.id)


def ask_question(chat_id: int) -> None:
    """Задает пользователю следующий вопрос."""
    user = user_data[chat_id]
    topic = user["topic"]
    question_data = QUIZ_DATA[topic][user["current_question"]]

    buttons = {
        option: {'callback_data': option}
        for option in question_data["options"]
    }
    markup = quick_markup(buttons, row_width=1)

    bot.send_message(
        chat_id,
        create_question_text(
            user["current_question"] + 1,
            question_data["question"]
        ),
        reply_markup=markup,
        parse_mode='HTML'
    )


@bot.callback_query_handler(func=lambda call: True)
def handle_answer(call: types.CallbackQuery) -> None:
    """Обрабатывает ответ пользователя."""
    chat_id = call.message.chat.id
    user = user_data.get(chat_id)

    if not user:
        return

    topic = user["topic"]
    question_data = QUIZ_DATA[topic][user["current_question"]]

    if call.data == question_data["answer"]:
        user["score"] += 1
        feedback = "✅ <b>Правильно!</b>"
    else:
        feedback = (
            f"❌ <b>Неправильно!</b>\n"
            f"Правильный ответ: <i>{question_data['answer']}</i>"
        )

    bot.delete_message(chat_id, call.message.message_id)
    bot.send_message(chat_id, feedback, parse_mode='HTML')

    user["current_question"] += 1

    if user["current_question"] < QUESTIONS_PER_QUIZ:
        ask_question(chat_id)
    else:
        bot.send_message(
            chat_id,
            create_result_message(topic, user["score"]),
            parse_mode='HTML'
        )
        del user_data[chat_id]


if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling()