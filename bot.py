import logging
import asyncio
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import psycopg2
import openpyxl
from datetime import datetime
from config import TOKEN, DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
import random
from aiogram.types import FSInputFile

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
cursor = conn.cursor()

user_data = {}

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Доступне навчання"), KeyboardButton(text="🗣️ Про нас")],
        [KeyboardButton(text="❗️ Запитання?"), KeyboardButton(text="🔮 Передбачення")]
    ],
    resize_keyboard=True
)

course_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💻 SMM"), KeyboardButton(text="📱 Блогерство"), KeyboardButton(text="🖥️ Таргет")],
        [KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)

course_info_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📖 Коротка інформація"), KeyboardButton(text="✅ Зареєструватися")],
        [KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)

registration_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Надіслати номер телефону", request_contact=True)],
        [KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)

@router.message(Command("start"))
async def start(message: types.Message):
    cursor.execute("INSERT INTO users (tg_id, username, full_name) VALUES (%s, %s, %s) ON CONFLICT (tg_id) DO NOTHING",
                   (message.from_user.id, message.from_user.username, message.from_user.full_name))
    conn.commit()
    await message.answer("👋 Привіт! Вибери дію:", reply_markup=menu)

@router.message(F.text == "🗣️ Про нас")
async def about_us(message: types.Message):
    await message.answer("ℹ️ Детальніше про нас на сайті: https://www.siter.in.ua/")

@router.message(F.text == "❗️ Запитання?")
async def ask_question(message: types.Message):
    await message.answer("📞 Якщо у вас є запитання, телефонуйте: +38 050 714 45 47")

@router.message(F.text == "🔮 Передбачення")
async def prediction(message: types.Message):
    predictions = [
        "Сьогодні твій день! ✨",
        "Удача на твоєму боці! 🍀",
        "Будь сміливим(ою), і ти переможеш! 🏆",
        "Тебе чекає приємний сюрприз! 🎁",
        "Зосередься на своїх цілях – успіх не за горами! 🚀"
    ]
    await message.answer(random.choice(predictions))

@router.message(F.text == "📚 Доступне навчання")
async def show_courses(message: types.Message):
    await message.answer("🎓 Ось доступні курси:", reply_markup=course_menu)

@router.message(F.text.in_(["💻 SMM", "📱 Блогерство", "🖥️ Таргет"]))
async def course_selection(message: types.Message):
    course_names = {"💻 SMM": "SMM", "📱 Блогерство": "Блогерство", "🖥️ Таргет": "Таргет"}
    course = course_names[message.text]
    user_data[message.from_user.id] = {"course": course}
    await message.answer(f"Курс: **{course}**\nОберіть опцію:", reply_markup=course_info_menu)

@router.message(F.text == "📖 Коротка інформація")
async def show_course_info(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data:
        await message.answer("Спочатку оберіть курс!", reply_markup=course_menu)
        return
    course = user_data[user_id]["course"]
    course_info = {
        "SMM": "Вивчення основ SMM стратегії та аналітики.",
        "Блогерство": "Створення контенту та розвиток особистого бренду в соцмережах.",
        "Таргет": "Основи таргетованої реклами та її оптимізація."
    }
    await message.answer(f"📖 Курс **{course}**\n{course_info[course]}", reply_markup=course_info_menu)

@router.message(F.text == "✅ Зареєструватися")
async def start_registration(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data:
        await message.answer("Спочатку оберіть курс!", reply_markup=course_menu)
        return
    await message.answer("✍️ Введіть ваше ім'я та прізвище:")

@router.message(lambda message: message.from_user.id in user_data and "full_name" not in user_data[message.from_user.id])
async def save_full_name(message: types.Message):
    user_data[message.from_user.id]["full_name"] = message.text
    await message.answer("📞 Надішліть ваш номер телефону:", reply_markup=registration_menu)


@router.message(lambda message: message.contact and message.from_user.id in user_data)
async def save_phone(message: types.Message):
    user = user_data[message.from_user.id]
    full_name = user["full_name"]
    phone = message.contact.phone_number
    course = user["course"]

    cursor.execute("INSERT INTO enrollments (user_id, course_name, full_name, phone_number) VALUES (%s, %s, %s, %s)",
                   (message.from_user.id, course, full_name, phone))
    conn.commit()
    del user_data[message.from_user.id]

    await message.answer(f"✅ {full_name}, ви успішно записані на курс **{course}**!\n🎁 Як подарунок, ось ваш безкоштовний гайд:", reply_markup=menu)
    
    try:
        guide = FSInputFile("guide.pdf")  
        await bot.send_document(message.chat.id, guide)
        await message.answer("📞 Ми з вами зв'яжемося найближчим часом!")
    except FileNotFoundError:
        await message.answer("❌ Вибачте, гайд наразі недоступний.")

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())