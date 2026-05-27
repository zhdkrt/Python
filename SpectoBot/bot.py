import os
import telebot
from dotenv import load_dotenv
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

import tmdb

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


GENRE_MAP = {
    "Комедия": 35,
    "Ужасы": 27,
    "Боевик": 28,
    "Фантастика": 878,
    "Драма": 18,
    "Мелодрама": 10749
}


def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("Подобрать фильм", "По жанру")
    kb.row("Популярное", "Топ")
    kb.row("О боте")
    return kb


def genre_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("Комедия", "Ужасы")
    kb.row("Боевик", "Фантастика")
    kb.row("Драма", "Мелодрама")
    kb.row("Назад")
    return kb


def inline_buttons(category, genre_id=None):
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("Еще", callback_data=f"more:{category}:{genre_id}")
    )
    return kb


def build_movie_text(movie):
    return (
        f"*{movie['title']}* ({movie['year']})\n"
        f"Рейтинг: {movie['rating']:.1f}/10\n\n"
        f"{movie['overview']}"
    )


def send_movie(chat_id, category="random", genre_id=None):
    try:
        movie = tmdb.get_random_movie(category=category, genre_id=genre_id)
    except Exception:
        bot.send_message(chat_id, "Ошибка при обращении к TMDB. Проверь API или подключение.")
        return

    if not movie:
        bot.send_message(chat_id, "Не удалось найти фильм.")
        return

    text = build_movie_text(movie)

    if movie.get("poster"):
        bot.send_photo(
            chat_id,
            photo=movie["poster"],
            caption=text,
            parse_mode="Markdown",
            reply_markup=inline_buttons(category, genre_id)
        )
    else:
        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=inline_buttons(category, genre_id)
        )


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет. Я помогу подобрать фильм. Выбери режим работы.",
        reply_markup=main_menu()
    )


@bot.message_handler(func=lambda m: m.text == "Подобрать фильм")
def pick_movie(message):
    send_movie(message.chat.id, category="random")


@bot.message_handler(func=lambda m: m.text == "По жанру")
def choose_genre(message):
    bot.send_message(
        message.chat.id,
        "Выбери жанр.",
        reply_markup=genre_menu()
    )


@bot.message_handler(func=lambda m: m.text == "Популярное")
def popular_movies(message):
    send_movie(message.chat.id, category="popular")


@bot.message_handler(func=lambda m: m.text == "Топ")
def top_movies(message):
    send_movie(message.chat.id, category="top")


@bot.message_handler(func=lambda m: m.text == "О боте")
def about_bot(message):
    bot.send_message(
        message.chat.id,
        "Бот помогает выбрать фильм случайно, по жанру, из популярных или из топа. ZHDK 2026",
        reply_markup=main_menu()
    )


@bot.message_handler(func=lambda m: m.text == "Назад")
def back_main(message):
    bot.send_message(
        message.chat.id,
        "Главное меню.",
        reply_markup=main_menu()
    )


@bot.message_handler(func=lambda m: m.text in GENRE_MAP)
def handle_genre(message):
    genre_id = GENRE_MAP[message.text]
    send_movie(message.chat.id, category="genre", genre_id=genre_id)


@bot.callback_query_handler(func=lambda c: c.data.startswith("more:"))
def more_movie(call):
    _, category, genre_id = call.data.split(":")
    genre_id = None if genre_id == "None" else int(genre_id)

    bot.answer_callback_query(call.id)
    send_movie(call.message.chat.id, category=category, genre_id=genre_id)


@bot.message_handler(func=lambda message: True)
def unknown_message(message):
    bot.send_message(
        message.chat.id,
        "Я не понял команду.\nИспользуй кнопки меню ниже.",
        reply_markup=main_menu()
    )


bot.infinity_polling()