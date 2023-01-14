import telebot
from telebot import types
import threading
import os
from mutagen.mp3 import MP3
import flask_get_handler
import bit_receiver
from config import *


threading.Thread(target=lambda: flask_get_handler.keep_alive()).start()


bot = telebot.TeleBot(token=token)

def keyboard_crate():
    keyboard = types.InlineKeyboardMarkup()
    keyboard = keyboard.add(types.InlineKeyboardButton(text="Изменить название", callback_data="change song name"))
    return keyboard

def audio_b(message):
    bot_message = bot.send_message(message.from_user.id, text="<b>Обработка файла...</b>", parse_mode="html")

    file_id = message.audio.file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    if file_info.file_path.endswith(".mp3"):
        for i in os.listdir("custom music/"):
            if str(message.from_user.id) in i:
                os.rename(f"custom music/{i}", f"custom music/{message.from_user.id}.mp3")
                try:
                    os.remove(f"custom music/{i[:-4]}.txt")
                except:
                    pass
                break

        with open(f"custom music/{message.from_user.id}.mp3", 'wb') as f:
            f.write(downloaded_file)

        with open(f"custom music/{message.from_user.id}.txt", "w") as f:
            try:
                f.write(f'{bit_receiver.main_song_handler(f"custom music/{message.from_user.id}.mp3")}\n')
                f.write(f'"{f"{message.from_user.id}.mp3"}"\n')  # ToDo: убрать два форматирования и убрать замену ковычек при обработке информации в music_data.py
                f.write(f'{round(MP3(f"custom music/{message.from_user.id}.mp3").info.length)}')
            except:
                for i in os.listdir("custom music/"):
                    if str(message.from_user.id) in i:
                        os.remove(f"custom music/{message.from_user.id}.mp3")
                        try:
                            os.remove(f"custom music/{message.from_user.id}.txt")
                        except:
                            pass
                        break
                bot.edit_message_text(message_id=bot_message.id, chat_id=message.chat.id, text=f"<b>Произошла ошибка</b> при обработке музыки\n<b>Попробуйте другой файл</b>", parse_mode="html")
                return

        bot.edit_message_text(message_id=bot_message.id, chat_id=message.chat.id, text=f"<b>Ваша музыка успешно добавлена\n\nНазвание</b>: <i>{message.from_user.id}</i>", reply_markup=keyboard_crate(), parse_mode="html")
    else:
        bot.edit_message_text(message_id=bot_message.id, chat_id=message.chat.id, text="<b>Неверный формат файла!</b>\n<u>Поддерживается только .mp3<u>", parse_mode="html")


def get_new_name(message):
    song_file_path = f"custom music/{message.from_user.id}.mp3"
    text_file_path = f"custom music/{message.from_user.id}.txt"
    os.rename(song_file_path, f"custom music/{message.text} by {message.from_user.id}.mp3")
    os.rename(text_file_path, f"custom music/{message.text} by {message.from_user.id}.txt")
    bot.send_message(message.from_user.id, text=f"<b>Название музыки изменено на </b><i>{message.text} by {message.from_user.id}</i>", parse_mode="html")


@bot.message_handler(commands=["start"])
def main_handler(message):
    bot.send_message(message.from_user.id, text=start_text, parse_mode="html")


@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    threading.Thread(target=audio_b, args=(message,)).start()

@bot.callback_query_handler(func=lambda call: True)
def change_filename(call):
    file_path = f"custom music/{call.from_user.id}.mp3"
    if os.path.exists(file_path):
        message = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"<b>Ваша музыка успешно добавлена\n\nНазвание: </b><i>{call.from_user.id}</i>\n\n<b>Введите новое название</b>", parse_mode="html")
        bot.register_next_step_handler(message, get_new_name)
    else:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"<b>Ваша музыка успешно добавлена\n\nНазвание: </b><i>{call.from_user.id}</i>\n\n<b>Файл не существует</b>", parse_mode="html")



bot.polling(True)
