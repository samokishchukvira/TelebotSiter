import os
import time
import telebot
from telebot import types

TOKEN = "8297975325:AAGArbLcJE9dSsMxoZmIzxx41wjBbKwg54I"
ADMIN_IDS = [733841797, 1336042507, 394592253, 527797499, 6334390799, 771177410]
# , 394592253, 1336042507, 6334390799, 527797499, 771177410
# 6334390799, 1336042507, 527797499, 771177410, 394592253, 733841797
bot = telebot.TeleBot(TOKEN)

complexes = [
    # "«Кварлал Липки-2» - вул. Мазепи 168",
    "«Квартал Левада» - Івасюка,19",
    "«Квартал Гімназійний-1» - Горбачевського, 14Г",
    "«Квартал Галицький» - вул. Хіміків 35, 37, 39",
    "«Квартал Галицький 2» - вул. Хіміків, 43",
    "«Левада Дем’янів Лаз» - вул. Демʼянів Лаз 35, 37, 39",
    "«Квартал Галичанка» - вул. Галицька 59А",
    "«Квартал Гімназійний-2» - вул. Горбачевського 14Е",
]

address_files = {
    # "«Кварлал Липки-2»": "kvartal_lipki_2.txt",
    "«Квартал Галицький»": "kvartal_galytskyi.txt",
    "«Квартал Галицький 2»": "kvartal_galytskyi_2.txt",
    "«Левада Дем’янів Лаз»": "levada_demianiv_laz.txt",
    "«Квартал Галичанка»": "kvartal_halychanka.txt",
    "«Квартал Гімназійний»": "kvartal_himnaziinyi.txt",
}

user_data = {}

def ensure_user(chat_id):
    if chat_id not in user_data:
        user_data[chat_id] = {}

def input_validation(chat_id):
    data = user_data.get(chat_id, {})
    if not data.get("complex"):
        send_complex_menu(chat_id)
        return False
    return True


def send_complex_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for c in complexes:
        markup.add(types.KeyboardButton(c))
    bot.send_message(chat_id, "🏢 Оберіть свій житловий комплекс", reply_markup=markup)

def send_main_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Актуальні оголошення", "Мій рахунок")
    markup.add("Залишити звернення", "Загальнобудинковий борг")
    markup.add("Наші контакти")
    markup.add("Обрати іншу адресу 🔙")
    bot.send_message(chat_id, "Оберіть опцію:", reply_markup=markup)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    ensure_user(message.chat.id)
    send_complex_menu(message.chat.id)


@bot.message_handler(func=lambda message: message.text in complexes)
def choose_complex(message):
    ensure_user(message.chat.id)

    if " - " in message.text:
        name, address = message.text.split(" - ", 1)
    else:
        name, address = message.text, ""

    user_data[message.chat.id]["complex"] = name.strip()
    user_data[message.chat.id]["address"] = address.strip()

    bot.send_message(
        message.chat.id,
        f"🏠 Ваша адреса: *{name.strip()}\n{address.strip()}*",
        parse_mode="Markdown",
        # reply_markup=types.ReplyKeyboardRemove()
    )

    user_data[message.chat.id]["waiting_pib"] = True
    bot.send_message(message.chat.id, "👋 Будь ласка, введіть ваше ПІБ:")

MENU_BUTTONS = [
    "Актуальні оголошення", "Мій рахунок",
    "Залишити звернення", "Загальнобудинковий борг",
    "Наші контакти", "Обрати іншу адресу 🔙"
]

IGNORE_BUTTONS_DURING_INPUT = ["Обрати іншу адресу 🔙", "Наші контакти"]

@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("waiting_pib", False))
def get_pib(message): 
    if message.text in MENU_BUTTONS:
        if message.text == "Обрати іншу адресу 🔙":
            send_complex_menu(message.chat.id)
            return
        if message.text == "Наші контакти":
            contacts(message)
            return

        bot.send_message(message.chat.id, "Спочатку введіть свої дані😊")
        return
    
    user_data[message.chat.id]["pib"] = message.text
    user_data[message.chat.id]["waiting_pib"] = False
    user_data[message.chat.id]["waiting_exact_address"] = True

    bot.send_message(message.chat.id, "🚪 Вкажіть, будь ласка, вашу точну адресу та номер квартири:")


@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("waiting_exact_address", False))
def get_exact_address(message):
    if message.text in MENU_BUTTONS:
        if message.text == "Обрати іншу адресу 🔙":
            send_complex_menu(message.chat.id)
            return
        if message.text == "Наші контакти":
            contacts(message)
            return

        bot.send_message(message.chat.id, "Спочатку введіть свої дані😊")
        return
    
    user_data[message.chat.id]["exact_address"] = message.text
    user_data[message.chat.id]["waiting_exact_address"] = False
    user_data[message.chat.id]["waiting_phone"] = True

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("📱 Поділитися номером", request_contact=True)
    markup.add(btn)
    bot.send_message(
        message.chat.id,
        "☎️ Будь ласка, натисніть кнопку нижче👇, щоб поділитися своїм номером телефону:",
        reply_markup=markup
    )


@bot.message_handler(content_types=['contact'])
def get_contact(message):
    if user_data.get(message.chat.id, {}).get("waiting_phone", False):
        user_data[message.chat.id]["phone"] = message.contact.phone_number
        user_data[message.chat.id]["waiting_phone"] = False

        bot.send_message(
            message.chat.id,
            "✅ Дякуємо!\nВаші дані успішно збережено.\n\nТепер ви маєте доступ до головного меню бота 📲",
            # reply_markup=types.ReplyKeyboardRemove()
        )
        send_main_menu(message.chat.id)


@bot.message_handler(func=lambda message: message.text == "Мій рахунок")
def show_account(message):
    # if not input_validation(message.chat.id):
    #     return

    data = user_data.get(message.chat.id, {})
    pib = data.get("pib", "Не введено")
    exact_address = data.get("exact_address", "Не введено")
    phone = data.get("phone", "Не введено")

    admin_text = (
        f"📥 *Запит на перегляд рахунку:*\n\n"
        f"*ПІБ:* {pib}\n"
        f"*ЖК:* {data.get('complex','-')}\n"
        f"*Адреса:* {data.get('address','-')}, {exact_address}\n"
        f"*Телефон:* {phone}\n"
        f"*Telegram ID:* {message.chat.id}\n"
        f"*Username:* @{message.from_user.username or 'Немає'}"
    )
    for admin_id in ADMIN_IDS:
      bot.send_message(admin_id, admin_text, parse_mode="Markdown")

    bot.send_message(
        message.chat.id,
        "✅ Ваш запит прийнято. Найближчим часом ми надішлемо інформацію про ваш рахунок.",
    )


@bot.message_handler(func=lambda message: message.text == "Залишити звернення")
def leave_complaint(message):
    if not user_data.get(message.chat.id, {}).get("complex"):
        bot.send_message(message.chat.id, "Спочатку натисніть /start та оберіть адресу 🏠")
        return
    user_data[message.chat.id]["waiting_complaint"] = True
    bot.send_message(message.chat.id, "Будь ласка, опишіть вашу проблему:")


@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("waiting_complaint", False))
def complaint_text(message):
    # if not input_validation(message.chat.id):
    #     return
    if message.text in MENU_BUTTONS:
        if message.text == "Обрати іншу адресу 🔙":
            send_complex_menu(message.chat.id)
            return
        if message.text == "Наші контакти":
            contacts(message)
            return
        bot.send_message(message.chat.id, "Спочатку опишіть своє звернення 🏠")
        return
        
    user_data[message.chat.id]["waiting_complaint"] = False
    text = message.text

    data = user_data.get(message.chat.id, {})
    pib = data.get("pib", "Не введено")
    exact_address = data.get("exact_address", "Не введено")
    phone = data.get("phone", "Не введено")

    user_data[message.chat.id]["last_complaint_text"] = text
    user_data[message.chat.id]["waiting_photo"] = True

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add("Так 📸", "Ні ❌")
    bot.send_message(message.chat.id, "Бажаєте додати фото до звернення?", reply_markup=markup)


# @bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("waiting_photo", False))
# def complaint_photo_choice(message):
#     user_data[message.chat.id]["waiting_photo"] = False
#     choice = message.text

#     if choice == "Так 📸":
#         user_data[message.chat.id]["waiting_photo_upload"] = True
#         bot.send_message(message.chat.id, "Будь ласка, надішліть фото:", reply_markup=types.ReplyKeyboardRemove())
#     else:
#         send_complaint_to_admin(message.chat.id)
#         bot.send_message(message.chat.id, "✅ Дякуємо за звернення! Ми з вами зв'яжемося найближчим часом.")
#         send_main_menu(message.chat.id)

@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("waiting_photo", False))
def complaint_photo_choice(message):
    chat_id = message.chat.id
    data = user_data.get(chat_id, {})

    user_data[chat_id]["waiting_photo"] = False

    choice = message.text.strip()

    if choice == "Так 📸":
        user_data[chat_id]["waiting_photo_upload"] = True
        bot.send_message(
            chat_id,
            "Будь ласка, надішліть фото:",
            reply_markup=types.ReplyKeyboardRemove()
        )
        return

    elif choice == "Ні ❌":
        send_complaint_to_admin(chat_id)
        bot.send_message(
            chat_id,
            "✅ Дякуємо за звернення! Ми з вами зв'яжемося найближчим часом.",
            reply_markup=types.ReplyKeyboardRemove()
        )
        send_main_menu(chat_id)
        return

    bot.send_message(
        chat_id,
        "Будь ласка, оберіть один із варіантів нижче 👇"
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add("Так 📸", "Ні ❌")
    bot.send_message(chat_id, "Бажаєте додати фото до звернення?", reply_markup=markup)

    user_data[chat_id]["waiting_photo"] = True

@bot.message_handler(content_types=['photo'])
def complaint_photo_upload(message):
    if user_data.get(message.chat.id, {}).get("waiting_photo_upload", False):
        user_data[message.chat.id]["waiting_photo_upload"] = False
        send_complaint_to_admin(message.chat.id, photo_id=message.photo[-1].file_id)
        bot.send_message(message.chat.id, "✅ Дякуємо за звернення! Ми з вами зв'яжемося найближчим часом.")
        send_main_menu(message.chat.id)


def send_complaint_to_admin(chat_id, photo_id=None):
    data = user_data.get(chat_id, {})
    text = data.get("last_complaint_text", "-")
    pib = data.get("pib", "Не введено")
    exact_address = data.get("exact_address", "Не введено")
    phone = data.get("phone", "Не введено")

    admin_text = (
        f"📥 *Звернення:*\n\n"
        f"*ПІБ:* {pib}\n"
        f"*ЖК:* {data.get('complex','-')}\n"
        f"*Адреса:* {data.get('address','-')}, {exact_address}\n"
        f"*Телефон:* {phone}\n"
        f"*Telegram ID:* {chat_id}\n"
        f"*Username:* @{data.get('username','Немає')}\n\n"
        f"*Опис проблеми:* {text}"
    )

    for admin_id in ADMIN_IDS:
        if photo_id:
            bot.send_photo(admin_id, photo_id, caption=admin_text, parse_mode="Markdown")
        else:
            bot.send_message(admin_id, admin_text, parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == "Актуальні оголошення")
def announcements(message):
    complex_name = user_data.get(message.chat.id, {}).get("complex")
    if not complex_name:
        bot.send_message(message.chat.id, "Спочатку натисніть цю команду /start, щоб обрати адресу😊")
        return

    base_name = complex_name.split(" - ")[0].strip()
    file_name = address_files.get(base_name)

    if not file_name:
        bot.send_message(message.chat.id, "📭 Оголошень для вашої адреси поки немає.\nСлідкуйте за оновленнями 😊")
        return

    file_path = os.path.join("advertisement", file_name) 

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
        if content:
            bot.send_message(message.chat.id, f"📢 *Актуальні оголошення:*\n\n{content}", parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, "📭 Оголошень для вашої адреси поки немає.\nСлідкуйте за оновленнями 😊")
    else:
        bot.send_message(message.chat.id, "📭 Оголошень для вашої адреси поки немає.\nСлідкуйте за оновленнями 😊")


@bot.message_handler(func=lambda message: message.text == "Загальнобудинковий борг")
def house_debt(message):
    complex_name = user_data.get(message.chat.id, {}).get("complex")
    if not complex_name:
        bot.send_message(message.chat.id, "Спочатку натисніть цю команду /start, щоб обрати адресу😊")
        return

    base_name = complex_name.split(" - ")[0].strip()
    file_name = address_files.get(base_name)

    if not file_name:
        bot.send_message(message.chat.id, "📭 Інформації про борг для вашої адреси поки немає.")
        return

    file_path = os.path.join("debt", file_name)

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
        if content:
            bot.send_message(message.chat.id, f"💰 *Загальнобудинковий борг:*\n\n{content}", parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, "📭 Інформації про борг для вашої адреси поки немає.")
    else:
        bot.send_message(message.chat.id, "📭 Інформації про борг для вашої адреси поки немає.")


@bot.message_handler(func=lambda message: message.text == "Наші контакти")
def contacts(message):
    contacts_text = (
        "📍 *Адреса головного офісу:*\n"
        "вул. Хіміків, 37\nм. Івано-Франківськ\n\n"
        "——\n\n"
        "🏢 *ЖЕО ПП \"Рідний дім\":*\n"
        "Бухгалтерія: +38 (066) 368 33 26, \n"
        "+38 (050) 197 24 85\n"
        "Техвідділ: +38 (067) 128 37 38"
    )
    markup = types.InlineKeyboardMarkup()
    # markup.add(types.InlineKeyboardButton("📘 Facebook", url="https://www.facebook.com/%D0%9B%D0%B5%D0%B2%D0%B0%D0%B4%D0%B0-213141559222862/"))
    # markup.add(types.InlineKeyboardButton("📹 YouTube", url="https://www.youtube.com/channel/UCBxxdQ10jUh2EXib2ibcUKA?disable_polymer=true"))
    # markup.add(types.InlineKeyboardButton("📸 Instagram", url="https://www.instagram.com/levada.if?igsh=MWhqa2xwMHUzNGRkNw=="))
    bot.send_message(message.chat.id, contacts_text, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Обрати іншу адресу 🔙")
def change_address(message):
    send_complex_menu(message.chat.id)

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    data = user_data.get(message.chat.id, {})

    if data.get("waiting_pib", False):
        get_pib(message)
        return
    if data.get("waiting_exact_address", False):
        get_exact_address(message)
        return
    if data.get("waiting_complaint", False):
        complaint_text(message)
        return

    bot.send_message(message.chat.id, "Оберіть опцію з меню 👇")

if __name__ == "__main__":
    while True:
        try:
            bot.infinity_polling(timeout=60, long_polling_timeout=5)
        except Exception as e:
            print(f"Polling помилка: {e}")
            time.sleep(5)




















