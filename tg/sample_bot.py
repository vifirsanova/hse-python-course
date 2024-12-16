#!/usr/bin/env python3

import json
import spacy

from telethon import TelegramClient, events, sync

# Telegram API
api_id = # получаем у @BotFather
api_hash = # ищем в my.telegram.org
bot_token = # ищем в my.telegram.org

# Инициализация клиента Telegram
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

nlp = spacy.load("ru_core_news_sm")

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Привет! Отправь мне JSON-файл с данными о канале Telegram.')

@bot.on(events.NewMessage)
async def handle_message(event):
    if event.message.media and event.message.media.document.mime_type == 'application/json':
        # Скачивание JSON-файла
        file_path = await bot.download_media(event.message.media)

        # Загрузка JSON-данных
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Извлечение текста из JSON-данных
        text = data.get('messages', '')  # Предполагается, что текст находится в поле 'text'
        text = [elem['text_entities'] for elem in text]
        text_ = ''
        for elem in text:
            if len(elem) > 0:
                for i in elem:
                    text_ += i['text']

        # Обработка текста с помощью spaCy
        doc = nlp(text_)[:512]

        # Извлечение именованных сущностей
        named_entities = [(ent.text, ent.label_) for ent in doc.ents]

        # Создание ответного сообщения
        response = "Именованные сущности:\n"
        for entity in named_entities:
            response += f"{entity[0]} ({entity[1]})\n"

        # Отправка ответа
        await event.respond(response)
    else:
        await event.respond('Пожалуйста, отправьте JSON-файл с данными о канале Telegram.')


# Запуск бота
bot.run_until_disconnected()
