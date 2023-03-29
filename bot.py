import logging
import random
import os
# import requests
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

bot = Bot(os.getenv('BOT_TOKEN'))   # @mystr1c_bot <-- bot in telegram
dp = Dispatcher(bot)


box = ['''- Штирлиц, на вас поступил донос от соседей. Пишут, что вы вчера пили, буянили и ругались по-русски!
Штирлиц молча берёт лист бумаги и пишет ответный донос:
"Группенфюреру СС Генриху Мюллеру. Мои соседи знают русский язык и, что особенно подозрительно, разбираются в 
ненормативной русской лексике!"''', '''Штирлиц вышел к обочине дороги, когда у рядом притормозившей машины приоткрылось
окно, и оттуда высунулась голова Мюллера.
- Тебе куда, дружище? – спросил Мюллер.
- На Унтер ден Линден, группенфюрер! - браво рявкнул Штирлиц, плюхнувшись рядом на сидение, и икнул.
- Семеныч, дуй в Подлипки, - тяжко вздохнув, сказал водителю Броневой.''', '''Курица клевала носом.
"Наверное не выспалась", - подумал Штирлиц''']


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ Эхобот от asnight!\nОтправь мне любое сообщение, а я тебе обязательно отвечу."
                        "\nОзнакомиться с функциями бота /help")

cmdkb = ReplyKeyboardMarkup(row_width=1)
cmdButton = KeyboardButton(text='1')     # /saha24d
cmdButton2 = KeyboardButton(text='2')   # Полезные ссылки
cmdButton3 = KeyboardButton(text='3')   # /мистрик
cmdButton4 = KeyboardButton(text='4')   # /геолокация
cmdButton5 = KeyboardButton(text='5')   # /уроки
cmdButton6 = KeyboardButton(text='6')   # /Никита
cmdButton7 = KeyboardButton(text='7')   # /Штирлиц
cmdButton8 = KeyboardButton(text='8')   # /atc
cmdButton9 = KeyboardButton(text="/help")    # /help
cmdkb.add(cmdButton, cmdButton2, cmdButton3, cmdButton4, cmdButton5, cmdButton6, cmdButton7, cmdButton8, cmdButton9)


@dp.message_handler(commands="help")
async def cmd_help(message: types.Message):
    await message.reply("Команды бота:\n 1. saha24d\n 2. Полезные ссылки 3. мистрик\n 4. Геолокация\n 5. уроки\n 6. Никита "
                        "Субботин\n 7. Штирлиц\n 8. Against The Current", reply_markup=cmdkb)


@dp.message_handler(text="1")
async def cmd1(message: types.Message):
    await message.reply("Александр Лобарев",
                        reply_markup=types.InlineKeyboardMarkup(
                            inline_keyboard=[
                                [types.InlineKeyboardButton("Информация о нем",
                                                            callback_data='ЛООООООООООООХ')]
                            ]
                        ))


@dp.callback_query_handler(lambda call: True)
async def answer_callback_query(callback: types.CallbackQuery):
    await callback.answer(callback.data, show_alert=True)


urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Перейти в tg asnight', url='https://t.me/asnight0')
urlButton2 = InlineKeyboardButton(text='Перейти в VK asnight', url='https://vk.com/asn1ghtnotdead')
urlkb.add(urlButton, urlButton2)


@dp.message_handler(text='2')
async def url_command(message: types.Message):
    await message.answer('Полезные ссылки:', reply_markup=urlkb)


@dp.message_handler(commands="спам")
async def cmd_spam(message: types.Message):
    await message.reply("\n{EQ"*1000)


markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
).add(
    KeyboardButton('Отправить свою локацию 🗺️', request_location=True),
    KeyboardButton(text='/help')
)


@dp.message_handler(commands=['4'])
async def process_hi6_command(message: types.Message):
    await message.reply("Шестое - запрашиваем контакт и геолокацию\nЭти две кнопки не зависят друг от друга",
                        reply_markup=markup_request)


@dp.message_handler(commands=['rm'])
async def process_rm_command(message: types.Message):
    await message.reply("Убираем шаблоны сообщений", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="3")
async def cmd2(message: types.Message):
    await message.reply("Бот мистрик")


@dp.message_handler(text='5')
async def cmd4(message: types.Message):
    await message.answer("""Понедельник: \n1. "Разговоры о важном"\n2. ИЗО\n3. Физкультура\n4. Алгебра\n5. Биология
6. Английский язык\n7. Химия
\nВторник: \n1. Русский язык\n2. Литература\n3. География\n4. Геометрия\n5. История\n6. Физкультура\n7. Физика
\nСреда: \n1. Обществознание\n2. Русский язык\n3. Литература\n4. География\n5. Английский язык\n6. История\n7. Музыка
\nЧетверг: \n1. Русский язык\n2. Химия\n3. Физкультура\n4. Алгебра\n5. Геометрия\n6. Информатика\n7. Физика
\nПятница: \n1. Алгебра\n2. Геометрия\n3. Биология\n4. Музыка\n5. Английский язык\n6. ОБЖ""")


@dp.message_handler(text='6')
async def cmd5(msg: types.Message):
    await msg.reply("Никита Субботин",
                    reply_markup=types.InlineKeyboardMarkup(
                            inline_keyboard=[
                                [types.InlineKeyboardButton("Информация о нем",
                                                            callback_data='Чемпион на пайке (Железо 4)')]
                            ]
                        ))


@dp.message_handler(text='7')
async def cmd6(msg: types.Message):
    await bot.send_message(msg.chat.id, random.choice(box))


@dp.message_handler(text='8')
async def answer_inline(msg: types.Message):
    await msg.answer("Against The Current Tour",
                     reply_markup=types.InlineKeyboardMarkup(
                         inline_keyboard=[
                             [types.InlineKeyboardButton("ATC",
                                                         web_app=types.WebAppInfo(
                                                             url="https://www.atcofficial.com/tour"))]
                         ]
                     ))


@dp.callback_query_handler(lambda call: True)
async def answer_callback_query(callback: types.CallbackQuery):
    await callback.answer(callback.data)


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def echo_photo(msg: types.Message):
    await msg.answer_photo(msg.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def echo_voice(msg: types.Message):
    await msg.answer_voice(msg.voice.file_id)


@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def echo_sticker(msg: types.Message):
    await msg.answer_sticker(msg.sticker.file_id)


@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def echo_video(msg: types.Message):
    await msg.answer_video(msg.video.file_id)


@dp.message_handler(content_types=types.ContentTypes.VIDEO_NOTE)
async def echo_video_note(msg: types.Message):
    await msg.answer_video_note(msg.video_note.file_id)


@dp.message_handler(content_types=types.ContentTypes.ANIMATION)
async def echo_animation(msg: types.Message):
    await msg.answer_animation(msg.animation.file_id)


@dp.message_handler(content_types=types.ContentTypes.DICE)
async def echo_dice(msg: types.Message):
    await msg.answer_dice(msg.dice.emoji)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

#   def get_updates():
#       r = requests.get(f'{bot}/getUpdates')
#   print(r.json()['result'][-1]['message']['chat'])

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    executor.start_polling(dp, skip_updates=True)
