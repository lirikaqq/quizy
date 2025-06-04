

<div align="center">
  <h1>🎮 QuizMaster Bot</h1>
  <p>Умный телеграм-бот для увлекательных викторин с разными темами</p>
  
  [![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
  [![Telegram](https://img.shields.io/badge/Telegram-Bot%20API-blue?logo=telegram)](https://core.telegram.org/bots/api)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdW5wZXNvZDR2d2g0d2V2d2J5dXl6b2J5cHd3Z3E1d3VhZ2F2cDZxZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7qE1YN7aBOFPRw8E/giphy.gif" width="400">
</div>

---

## ✨ Особенности

- 🧠 **3 интеллектуальные категории**: История, Наука, Кино
- ⚡️ Динамические квизы по 5 вопросов
- 🌈 Интерактивные кнопки и клавиатуры
- 📊 Автоматический подсчет результатов
- 🏆 Мотивационные сообщения в зависимости от результата
- 💾 Сессионное хранение данных пользователей

## 🚀 Как начать

### Предварительные требования
- Python 3.10+
- Активный Telegram бот ([@BotFather](https://t.me/BotFather))

### Установка
```bash
# Клонировать репозиторий
git clone https://github.com/yourusername/quizmaster-bot.git

# Перейти в директорию проекта
cd quizmaster-bot

# Установить зависимости
pip install -r requirements.txt
```

### Настройка
1. Создайте `.env` файл:
```env
BOT_TOKEN=ваш_токен_бота
```

### Запуск
```bash
python bot.py
```

## 🎮 Использование
1. Отправьте боту команду `/start`
2. Выберите тему викторины
3. Отвечайте на вопросы с помощью интерактивных кнопок
4. Получите персональную статистику в конце

<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGx4c3VkY3R4dW1zZ2VpN2t0Y2d5d3V4c2N5c3F0Z2UwemQ1c2V4eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QUO6UUV7UZq4c2p0u4/giphy.gif" width="300">

## 🧩 Структура проекта
```
.
├── bot.py                - Основной код бота
├── .env                  - Конфигурация окружения
├── requirements.txt      - Зависимости
├── README.md             - Документация
└── LICENSE               - Лицензия
```

## 🌟 Особенности реализации
```python
# Интеллектуальная генерация интерфейса
def create_result_message(topic: str, score: int) -> str:
    """Создает персонализированное сообщение с результатами"""
    return (
        f"🎉 <b>Викторина завершена!</b> 🎉\n"
        f"Тема: <i>{topic}</i>\n"
        f"Результат: <b>{score}/{QUESTIONS_PER_QUIZ}</b>\n\n"
        f"{get_result_emoji(score)} {get_result_comment(score)}"
    )
```

## 🤝 Как внести вклад
1. Форкните репозиторий (`https://github.com/yourusername/quizmaster-bot/fork`)
2. Создайте новую ветку (`git checkout -b feature/amazing-feature`)
3. Сделайте коммит изменений (`git commit -m 'Add some amazing feature'`)
4. Запушьте ветку (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

## 📜 Лицензия
Распространяется под лицензией MIT. См. [LICENSE](LICENSE) для подробностей.

---

<div align="center">
  <p>Сделано с ❤️ для любителей викторин</p>
  <img src="https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif" width="100">
</div>
