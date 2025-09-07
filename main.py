# import telebot
# from telebot import types

# TOKEN = '7830126067:AAGrCc8L8cukK2yMJTMpalsXm-_6xKJne1w'
# bot = telebot.TeleBot(TOKEN)

# # головне меню
# main_menu = [
#     ["Котеджне містечко Westhills"],
#     ["Котеджі/апартаменти", "Ресторан Westhill"],
#     ["Pool & Aquazone", "Pool bar"],
#     ["SPA – центр", "PRIVATE SPA"],
#     ["Додаткові послуги", "Масаж"],
#     ["Дитяче дозвілля", "Спортивний майданчик"],
#     ["Акції та пропозиції", "Події"],
#     ["Залишити відгук", "Контакти та інформація"]
# ]

# # меню Котеджі/апартаменти
# cottages_apartments_menu = [
#     ["Котеджі", "Апартаменти"],
#     ["Додаткове розміщення", "Розміщення з тваринами"],
#     ["⬅️ Назад"]
# ]

# # меню Ресторан Westhill 
# restaurant_westhills_menu = [
#     ["Кухня", "Бар"],
#     ["Винна карта", "Room service"],
#     ["Контакти", "⬅️ Назад"]
# ]

# # меню Pool & Aquazone 
# pool_aquazone_menu = [
#     ["Вартість", "Фото"],
#     ["⬅️ Назад"]
# ]

# # меню Poll bar
# pool_bar_menu = [
#     ["Бар", "Кухня"],
#     ["⬅️ Назад"]
# ]

# # меню Private spa
# private_spa_menu = [
#     ["Фото та вартість"],
#     ["⬅️ Назад"]
# ]

# # меню Додаткові послуги
# additional_services_menu = [
#     ["Прокат велосипедистів", "Зарядка електромобіля"],
#     ["Оренда зони BBQ", "⬅️ Назад"]
# ]

# # меню Масаж
# massage_menu = [
#     ["Вартість", "⬅️ Назад"]
# ]

# # меню Дитяче дозвілля
# kids_menu = [
#     ["Дитяча кімната", "Дитячий майданчик"],
#     ["Майстер класи, аніматори", "⬅️ Назад"]
# ]

# # меню Акції та пропозиції
# promotions_offers_menu = [
#     ["Іменна карта -10%", "Знижка від кількості"],
#     ["Щасливий іменинник", "Подарунковий сертифікат"],
#     ["Знижка для УБД -10%", "⬅️ Назад"]
# ]

# # меню Контакти та інформація
# contacts_information_menu = [
#     ["Тік Ток", "Інстаграм"],
#     ["Сайт", "Рецепція Котеджів"],
#     ["Рецепція Апартаментів", "Відділ бронювання"],
#     ["Ресторан", "Наша Локація"],
#     ["⬅️ Назад"]
# ]

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in main_menu:
#         buttons = [types.KeyboardButton(text) for text in row]
#         markup.add(*buttons)

#     bot.send_message(
#         message.chat.id,
#         "🏡 *Ласкаво просимо до котеджного містечка Westhills!*\n"
#             "Ми пропонуємо сучасну територію з розвиненою інфраструктурою.\n\n"
#             "Westhills ідеально підходить для відпочинку на природі, активних розваг, сімейного відпочинку, корпоративів, свят та спортивних зборів.  "
#             "Незалежно від пори року, ми забезпечимо вам чудовий настрій і незабутні враження. Завдяки кваліфікованому персоналу та індивідуальному підходу, "
#             "ваше перебування в Westhills буде комфортним і приємним.\n\n"
#             "*Контакти:*\n"
#             "+38 (067) 777 81 44 — рецепція котеджів\n"
#             "+38 (066) 777 81 44 — рецепція апартаментів\n"
#             "+38 (068) 777 81 44 — ресторан\n\n"
#             "*Команда котеджного містечка Westhills бажає Вам приємного перебування!*",
#         parse_mode="Markdown",
#         reply_markup=markup
#     )

# @bot.message_handler(func=lambda message: True)
# def menu_handler(message):
#     if message.text == "Котеджне містечко Westhills":
#         bot.send_message(message.chat.id, 
#             "🏡 *Ласкаво просимо до котеджного містечка Westhills!*\n"
#             "Ми пропонуємо сучасну територію з розвиненою інфраструктурою.\n\n"
#             "Westhills ідеально підходить для відпочинку на природі, активних розваг, сімейного відпочинку, корпоративів, свят та спортивних зборів.  "
#             "Незалежно від пори року, ми забезпечимо вам чудовий настрій і незабутні враження. Завдяки кваліфікованому персоналу та індивідуальному підходу, "
#             "ваше перебування в Westhills буде комфортним і приємним.\n\n"
#             "*Контакти:*\n"
#             "+38 (067) 777 81 44 — рецепція котеджів\n"
#             "+38 (066) 777 81 44 — рецепція апартаментів\n"
#             "+38 (068) 777 81 44 — ресторан\n\n"
#             "*Команда котеджного містечка Westhills бажає Вам приємного перебування!*",
#             parse_mode="Markdown"
#         )
#     elif message.text == "Котеджі/апартаменти":
#         cottages_apartments_menu_handler(message)
#     elif message.text == "Ресторан Westhill":
#         restaurant_handler(message)
#     elif message.text == "Pool & Aquazone":
#         pool_aquazone_handler(message)
#     elif message.text == "Pool bar":
#         pool_bar_handler(message)
#     elif message.text == "SPA – центр":
#         spa_center_handler(message)
#     elif message.text == "PRIVATE SPA":
#         private_spa_handler(message)
#     elif message.text == "Додаткові послуги":
#         additional_services_handler(message)
#     elif message.text == "Масаж":
#         massage_handler(message)
#     elif message.text == "Дитяче дозвілля":
#         kids_handler(message)
#     elif message.text == "Спортивний майданчик":
#         sports_ground_handler(message)
#     elif message.text == "Акції та пропозиції":
#         promotions_offers_handler(message)
#     elif message.text == "Події":
#         offers_handler(message)
#     elif message.text == "Залишити відгук":
#         reviews_handler(message)
#     elif message.text == "Контакти та інформація":
#         contacts_information_handler(message)
#     elif message.text == "Котеджі":
#         cottages_handler(message)
#     elif message.text == "Апартаменти":
#         apartments_handler(message)
#     elif message.text == "Додаткове розміщення":
#         additional_accommodation_handler(message)
#     elif message.text == "Розміщення з тваринами":
#         pets_accommodation_handler(message)
#     elif message.text == "Кухня":
#         restaurant_kitchen_handler(message)
#     elif message.text == "Бар":
#         restaurant_bar_handler(message)
#     elif message.text == "Винна карта":
#         wine_menu_handler(message)
#     elif message.text == "Room service":
#         room_service_handler(message)
#     elif message.text == "Контакти":
#         restaurant_contacts_handler(message)
#     elif message.text == "Фото":
#         restaurant_photos_handler(message)
#     elif message.text == "Вартість":
#         restaurant_prices_handler(message)
#     elif message.text == "Фото та вартість":
#         photos_prices_handler(message)
#     elif message.text == "Прокат велосипедистів":
#         bike_rental_handler(message)
#     elif message.text == "Зарядка електромобіля":
#         ev_charging_handler(message)
#     elif message.text == "Оренда зони BBQ":
#         bbq_zone_rental_handler(message)
#     elif message.text == "Дитяча кімната":
#         kids_room_handler(message)
#     elif message.text == "Дитячий майданчик":
#         playground_handler(message)
#     elif message.text == "Майстер класи, аніматори":
#         activities_handler(message)
#     elif message.text == "Іменна карта -10%":
#         name_card_handler(message)
#     elif message.text == "Знижка від кількості":
#         quantity_discount_handler(message)
#     elif message.text == "Щасливий іменинник":
#         happy_noun_handler(message)
#     elif message.text == "Подарунковий сертифікат":
#         gift_certificate_handler(message)
#     elif message.text == "Знижка для УБД -10%":
#         discount_handler(message)
#     elif message.text == "Тік Ток":
#         tiktok_handler(message)
#     elif message.text == "Інстаграм":
#         instagram_handler(message)
#     elif message.text == "Сайт":
#         website_handler(message)
#     elif message.text == "Рецепція Котеджів":
#         phone_cottages_handler(message)
#     elif message.text == "Рецепція Апартаментів":
#         phone_apartments_handler(message)
#     elif message.text == "Відділ бронювання":
#         phone_booking_handler(message)
#     elif message.text == "Ресторан":
#         phone_restaurant_handler(message)
#     elif message.text == "Наша Локація":
#         location_handler(message)
#     elif message.text == "⬅️ Назад":
#         send_main_menu(message)
#     else:
#         bot.send_message(message.chat.id, f"🔎 Інформація про *{message.text}* оновлюється!"
#                          "Ми працюємо над оновленням даних для вас! Дякуємо за розуміння.", parse_mode="Markdown")
                

# def send_main_menu(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in main_menu:
#         buttons = [types.KeyboardButton(text) for text in row]
#         markup.add(*buttons)

#     bot.send_message(
#         message.chat.id,
#         text="Оберіть опцію:", 
#         reply_markup=markup 
#     )


# @bot.message_handler(func=lambda message: message.text == "Котеджі/апартаменти")
# def cottages_apartments_menu_handler(message):

#     texts = [
#         "🏘Містечко в Карпатах поєднує відновлювальну енергію та сучасну природну архітектуру. "
#         "Тут розташовано 11 будинків, побудованих з дерева та каменю, що гармонійно вписуються в навколишній ландшафт. "
#         "Окрім цього, є окремий корпус з 22 сучасними та просторими апартаментами, які забезпечують комфортне проживання.\n\n"
#         "——\n\n"
#         "🛏 *Проживання та інфраструктура:*\n\n"
#         "• SPA-зона: 10:00 – 22:00\n"
#         "• Відкритий панорамний басейн 29° та дитяча аквазона 32°: 09:00 – 21:00\n"
#         "• Критий SPA-центр: 2 басейни (30°), хамам, парна, 2 джакузі (35°), кімната з карпатським чаєм\n"
#         "• Панорамна зона з шезлонгами\n\n"
#         "——\n\n"
#         "🍳 *Харчування:*\n\n"
#         "Сніданки включені у вартість проживання (шведська лінія з 8:00 до 11:00 у ресторані Westhill).\n"
#         "Обіди та вечері — ресторан Westhill (13:00–22:30) або Pool bar (10:00–21:00).\n"
#         "Доступний room service (13:00–22:30).\n"
#         "_Рекомендуємо бронювання столиків заздалегідь._\n\n"
#         "——\n\n"
#         "🦌 *Заповідник з оленями:*\n\n"
#         "Поруч із готелем розташований парк, де мешкають олені та косулі. "
#         "Прогулянки безкоштовні, а тварин можна побачити з різних куточків містечка.\n\n"
#         "——\n\n"
#         "👧 *Для найменших гостей:*\n\n"
#         "• Дитячий майданчик\n• Ігрова кімната\n• Аніматори\n• Майстер-класи\n"
#         "Westhills — справжній рай для дітей, де вони завжди знайдуть щось цікаве!\n\n"
#         "——\n\n"
#         "🅿️ *Паркінг:*\n\n"
#         "Паркінг на території містечка під охороною і з відеоспостереженням — безпечно та зручно.\n\n"
#         "——\n\n"
#         "💪 *Спортивний майданчик:*\n\n"
#         "Вуличні тренажери доступні для всіх гостей, тож спорт і свіже повітря завжди поруч.\n\n"
#         "——\n\n"
#         "📞 *Контакти:*\n"
#         "+38 (067) 777 81 44 — рецепція котеджів\n"
#         "+38 (066) 777 81 44 — рецепція апартаментів\n"
#         "+38 (068) 777 81 44 — ресторан\n\n"
#         "_Інформацію про послуги та розваги шукайте у розділах цього бота або звертайтеся на рецепцію._\n\n"
#         "*Команда котеджного містечка Westhills бажає Вам приємного перебування!*"
#     ]
#     for text in texts:
#         bot.send_message(message.chat.id, text, parse_mode="Markdown")

#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in cottages_apartments_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Котеджі")
# def cottages_handler(message):
#     bot.send_message(message.chat.id, "Програму вашого вікенду, інформацію про послуги та розваги дізнавайтеся у розділах нашого чат-боту. " 
#     "У разі додаткових запитань звертайтеся на рецепцію – будемо раді зробити ваш візит комфортним.\n\n"
#     "https://westhills.com.ua/cottages")
#     # send_cottages_apartments_menu(message)

# @bot.message_handler(func=lambda message: message.text == "Апартаменти")
# def apartments_handler(message):
#     bot.send_message(message.chat.id, "Програму вашого вікенду, інформацію про послуги та розваги дізнавайтеся у розділах нашого чат-боту. " 
#     "У разі додаткових запитань звертайтеся на рецепцію – будемо раді зробити ваш візит комфортним.\n\n"
#     "https://westhills.com.ua/cottages/cottage ")

# @bot.message_handler(func=lambda message: message.text == "Додаткове розміщення")
# def additional_accommodation_handler(message):
#     bot.send_message(message.chat.id, "У апартаментах 50м2 - можливе розміщення однієї дитини до 3-х років  безкоштовно, " 
#     "або за додаткову плату в залежності від віку:\n\n"
#     "*• 4-6 р. - 800 грн/доба,*\n"
#     "*• 7-11 р. - 1200 грн/доба,*\n"
#     "*• 12+ - 1900 грн/доба.*\n\n"
#     "У котеджах можливе розміщення 1 додаткового місця (для дорослого) – 1900 грн/доба, при умові, якщо відсутні діти старші 3-х років.\n"
#     "❗Діти віком від 12 років вважаються дорослими.\n"
#     "Розміщення у вітальні на дивані.",parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Розміщення з тваринами")
# def pets_accommodation_handler(message):
#     bot.send_message(message.chat.id, "*🐾Умови проживання з домашніми улюбленцями:*\n\n"
#     "- вага до 7 кг:\n"
#     "- дозволене розміщення тільки однієї тваринки в номері;\n"
#     "- вигул відбувається тільки у спеціально призначених для цього місцях. Забороняється вигул тваринок на газонах території;\n"
#     "- у місця загального користування (ресторан, SPA-центр, басейн, дитячу кімнату та інші) не дозволено брати з собою домашніх тварин у зв’язку з санітарно-епідеміологічними вимогами;\n"
#     "- забороняється залишати улюбленця самого в номері більше ніж на 1,5 годин;\n"
#     "- у вартість перебування тваринки входить прибирання апартаментів/котеджу після виїзду паровим обладнанням;\n"
#     "- у вартість не входить компенсація у разі пошкодження майна готелю тваринкою. Збиток, нанесений готелю тваринами, компенсується окремо від вартості проживання повною мірою згідно з виставленим рахунком;\n"
#     "- у разі порушення цих умов проживання з домашніми улюбленцями, готель залишає за собою права виселити Гостей з тваринкою без повернення оплати.",
#     parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Ресторан Westhill")
# def restaurant_handler(message):

#     texts = [
#         "🍽 Ресторан Westhill — це справжня перлина котеджного містечка Westhills, де естетика та кулінарне мистецтво зливаються в одне ціле." 
#         " Сучасний інтер’єр ресторану, витриманий у стилі розкоші та комфорту, створює неповторну атмосферу." 
#         " Панорамні вікна відкривають захоплюючий вигляд на величний карпатський ліс та закритий вольєр з косулями, що додає ще більше магії цьому місцю." 
#         " У ресторані ви також зможете насолодитися стравами, приготованими в печі, а на відкритій терасі — відпочити та насолодитися атмосферою природи." 
#         " Авторська кухня, бездоганна професійність та висока якість обслуговування залишать у вас незабутні враження та подарують справжнє гастрономічне задоволення." 
#         " Кожна деталь нашого ресторану відображає вишуканий смак і неперевершену майстерність.\n\n\n"

#         "🏠 Ресторан знаходиться в окремій будівлі на початку містечка.\n\n"
#          "🕰 **Графік роботи**:\n"
#         "13:00 - 23:00\n"
#         "Приймаємо замовлення за основним меню до 22:30.\n\n"
        
#         "📞 **Контакти**:\n"
#         "Бронюйте ваш столик за телефоном: +38068 777 81 44\n\n"
#         "https://westhills.com.ua/services/restaurant"
#     ]

#     for text in texts:
#         bot.send_message(message.chat.id, text, parse_mode="Markdown")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in restaurant_westhills_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)  

# @bot.message_handler(func=lambda message: message.text == "Кухня")
# def restaurant_kitchen_handler(message):
#     bot.send_message(message.chat.id, "[📖Переглянути меню](https://expz.menu/3d04ea14-c177-4b8c-a4a8-e83c337aed6d/menu?menuId=18922)", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Винна карта")
# def wine_menu_handler(message):
#     bot.send_message(message.chat.id, "[🍇Переглянути винну карту](https://expz.menu/3d04ea14-c177-4b8c-a4a8-e83c337aed6d/menu?menuId=19407)", parse_mode="Markdown")
    
# @bot.message_handler(func=lambda message: message.text == "Бар")
# def restaurant_bar_handler(message):
#     bot.send_message(message.chat.id, "[🍷Переглянути бар ресторану](https://expz.menu/3d04ea14-c177-4b8c-a4a8-e83c337aed6d/menu?menuId=19409)", parse_mode="Markdown")
    
# @bot.message_handler(func=lambda message: message.text == "Room service")
# def room_service_handler(message):
#     bot.send_message(message.chat.id, "🛎 Смакуйте вишукані страви, не виходячи з котеджу чи апартаментів!\n\n" 
#     "Наш рум сервіс створений для тих, хто бажає насолодитися комфортом та смачною кухнею прямо в номері. " 
#     "Від класичних європейських страв до авторських шедеврів від шефа — ми забезпечимо вам незабутні гастрономічні враження будь-якої миті." 
#     " Оберіть улюблені страви з нашого меню та замовляйте прямо до вашого котеджу чи апартаментів!\n\n" 
#     "📞Кнопка виклику подзвонити на +380687778144", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Контакти")
# def restaurant_contacts_handler(message):
#     bot.send_message(message.chat.id, "📞Забронювати столик можна за телефоном: +380687778144 ")
    

# @bot.message_handler(func=lambda message: message.text == "Pool & Aquazone")
# def pool_aquazone_handler(message):
#     texts = [
#         "🌞Ідеальний відпочинок для всієї родини з дітьми?"
#         " У Westhills це абсолютно реально!\n\n"
#         "- Відкритий басейн з підігрівом, та зоною джакузі для вашого комфорту;\n"
#         "- Водяні гірки та дитячий басейн з підігрівом для маленьких гостей;\n"
#         "- POOL BAR для приємного відпочинку біля води.\n\n"
#         "Ваші діти не будуть нудьгувати, і ви зможете насолоджуватись спокоєм.\n"
#         "А після активного дня — солодкий та спокійний сон гарантовано! Найголовніше — у Westhills ми завжди піклуємось про безпеку наших гостей.\n"
#         "Що може бути важливіше за такі незабутні спогади? Розваги для дітей, комфорт для батьків.\n\n"
#         "*Чекаємо на вас у Westhills, де природа і сучасний комфорт відпочинку створюють ідеальну гармонію!🌿*"
#     ]

#     for text in texts:
#         bot.send_message(message.chat.id, text, parse_mode="Markdown")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in pool_aquazone_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Фото")
# def restaurant_photos_handler(message):
#     bot.send_message(message.chat.id, "[📸Переглянути фото](https://westhills.com.ua/services/pool)", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Вартість")
# def restaurant_prices_handler(message):
#     bot.send_message(message.chat.id, "[💰Переглянути вартість](https://westhills.com.ua/prices)", parse_mode="Markdown")

        
# @bot.message_handler(func=lambda message: message.text == "Pool bar")
# def pool_bar_handler(message):
#     texts = [
#        "🍹На нашому басейні працює Pool Bar, де ви зможете насолодитися різноманітними напоями — від освіжаючих безалкогольних до вишуканих алкогольних коктейлів, що створять ідеальну атмосферу для вашого відпочинку.\n\n "
#        "Для тих, хто любить солодке, ми пропонуємо смачне морозиво, а також широкий вибір страв на кухні, де ви зможете скуштувати піцу чи бургери, приготовані з найкращих інгредієнтів. \n\n"
#        "Усе це забезпечить вам комфорт та насолоду протягом часу, проведеного біля басейну.☀️🏖️"
#     ]

#     for text in texts:
#         bot.send_message(message.chat.id, text, parse_mode="Markdown")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in pool_bar_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "PRIVATE SPA")
# def private_spa_handler(message):
#     texts = [
#         "🌲<b>Карпатська баня</b> \n\n"
#         "Відвідування сауни в котеджному містечку Westhills — це гарантований шлях до ідеального релаксу та відновлення сил!\n\n"
#         "• Басейн 5*4 м з температурою води 25-26°C та глибиною 1,5 м;\n"
#         "• Баня на дровах з традиційною пропаркою віниками, послуги банщика включені у вартість;\n"
#         "• На терасі ви зможете освіжитися в діжці з крижаною водою або розслабитися в гарячому джакузі;\n"
#         "• Хамам (турецька парова сауна);\n"
#         "• Кімната, наповнена ароматами карпатських трав;\n"
#         "• Масажний кабінет для додаткового розслаблення;\n"
#         "• Зона відпочинку біля каміну для затишного часу.\n\n"
#         "Це приватна зона, де ви та ваша компанія відпочиваєте наодинці, без сторонніх. "
#         "Під час бронювання ви маєте можливість насолоджуватися цією атмосферою в повній приватності. "
#         "Також ви можете замовляти смачні страви та напої з нашого ресторану або приносити свої для ще більшого комфорту.\n\n"
#         "🍵 А ще, наш банщик приготує для вас смачний трав’яний карпатський чай з медом, щоб ваш відпочинок став ще приємнішим!\n\n"
#         "https://westhills.com.ua/services/karpatska_banya "
#     ]

#     for text in texts:
#       bot.send_message(message.chat.id, text, parse_mode="HTML")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in private_spa_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])
    
#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Бар")
# def photos_prices_handler(message):
#     bot.send_message(message.chat.id, "[🌲Фото та вартість Карпатської бані](https://westhills.com.ua/services/karpatska_banya )", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "SPA – центр")
# def spa_center_handler(message):
#     texts = [
#         "🌿 <b>SPA-центр у Westhills — це місце, де кожна мить відчувається по-новому.</b> \n\n"
#         "Відпочивайте та відновлюйтесь у нашій SPA-зоні, де кожна деталь створена для вашого комфорту.\n\n"
#         "• 2 сауни: хамам та парна;\n"
#         "• Басейн з підігрівом 8x4 м, глибина 1,25 м;\n"
#         "• Басейн-джакузі з виходом на вулицю 7x3x1,3 м, глибина 1,3 м;\n"
#         "• 2 панорамних гарячих джакузі, глибина 0,8-0,9 м;\n"
#         "• Кімната відпочинку з карпатським чаєм;\n"
#         "• Панорамна зона з шезлонгами для вашого релаксу.\n\n"
#         "✨ <b>Особливістю нашого SPA є унікальна процедура в парній, яку можна отримати лише в Westhills.</b>\n\n"
#         "Залиште всі турботи позаду і створюйте незабутні моменти для себе та своїх близьких у Westhills Cottage Town!"
#     ]

#     for text in texts:
#       bot.send_message(message.chat.id, text, parse_mode="HTML")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in pool_aquazone_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Додаткові послуги")
# def additional_services_handler(message):
#     texts = [
#        "🚴‍♂️ Активний відпочинок у Westhills – це незабутній час, сповнений приємних вражень, що залишаться з вами назавжди. "
#        "Ми пропонуємо різноманітні види активностей для всіх:\n\n"
#        "• оренда мангалу з альтанкою;\n"
#        "• прокат велосипедів;\n"
#        "• відкритий дитячий майданчик;\n"
#        "• тренажерний майданчик на відкритому повітрі;\n"
#        "• прогулянки до лісових мешканців (косуль та оленів), що живуть у нашому заповіднику;\n"
#        "• велика територія для прогулянок і відпочинку.\n\n"
#        "<b>Запрошуємо вас до Westhills – тут ви поринете у справжній відпочинок, ближче до природи і подалі від міського шуму!</b>"
#     ]

#     for text in texts:
#       bot.send_message(message.chat.id, text, parse_mode="HTML")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in additional_services_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Зарядка електромобіля")
# def ev_charging_handler(message):
#     bot.send_message(message.chat.id, "🔌*Включення/відключення зарядки за допомогою картки ТОКА :*\n\n" 
#     "Наявні два типи портів Type 1, Type 2. \n\n" 
#     "• Під’їхавши до зарядної станції мережі «ТОКА», Вам необхідно вставити зарядний кабель у відповідний  роз’єм  електромобіля;\n" 
#     "• Для запуску процесу зарядки, піднесіть картку мережі «ТОКА» до зчитувача на станції;\n" 
#     "• Для припинення процесу зарядки, дістаньте зарядний кабель із зарядної станції.\n\n" 
#     "Станція знаходиться у внутрішньому дворі, на паркінгу.\n\n" 
#     "💲Вартість послуги  – 17 грн -1 кВт, розрахунок відбувається на центральній рецепції Westhills", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Оренда зони BBQ")
# def bbq_zone_rental_handler(message):
#     bot.send_message(message.chat.id, "🍖*Запрошуємо вас насолодитися чудовим відпочинком на свіжому повітрі з орендою зони BBQ у Westhills.*\n\n " 
#     "Насолоджуйтесь смачними стравами, приготованими на мангалі, в затишній альтанці серед природи. " 
#     "Усе необхідне для приготування барбекю – мангал, інвентар та комфортна альтанка – вже підготовлено для вас. " 
#     "Створіть незабутні спогади, насолоджуючись природою та смачними стравами на свіжому повітрі!\n\n" 
#     "💲Вартість послуги – 900 грн за 2 години,  оренда здійснюється за попереднім замовленням.", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Прокат велосипедів")
# def bike_rental_handler(message):
#     bot.send_message(message.chat.id, "🚴‍♂️*Прокат велосипедів у Westhills – ідеальний спосіб активно провести час на свіжому повітрі!*\n\n" 
#     "У нас є велосипеди для дорослих і для дітей, а також дитячі крісла та замочки для вашої зручності. \n\n" 
#     "Відправляйтесь на велопрогулянку по мальовничих стежках та насолоджуйтесь красою природи Карпат.\n\n" 
#     "Вартість прокату  велосипеду: \n\n" 
#     "1️⃣ година - 200 грн\n"
#     "2️⃣ години - 300 грн\n"
#     "3️⃣ години - 400 грн\n"
#     "⏩ Кожна наступна година після третьої - 100 грн", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Масаж")
# def massage_handler(message):
#     texts = [
#         "💆‍♀️Запрошуємо вас поринути у світ розкоші та релаксу, де кожен дотик створює атмосферу гармонії і відновлення. "
#         "Наш масажний кабінет — це місце, де ви зможете відчути справжню силу карпатських гір, занурюючись у відчуття спокою та енергії природи. "
#         "Ми поєднуємо традиційні методи масажу з авторськими техніками, що розроблені спеціально для того, щоб кожен сеанс приносив максимальний ефект відновлення.\n\n"
#         "Наші майстри використовують тільки найкращу преміальну косметику, яка дарує вашій шкірі ніжний догляд та живлення, сприяючи глибокому розслабленню. "
#         "Від класичного масажу до комплексних процедур, ми пропонуємо широкий спектр послуг для тих, хто прагне відновити сили, покращити самопочуття та отримати незабутні враження.\n\n"
#         "<b>Завітайте до нас і насолоджуйтесь не тільки висококласним обслуговуванням, але й атмосферою, яка відновлює та дарує гармонію.✨</b>"
#     ]

#     for text in texts:
#       bot.send_message(message.chat.id, text, parse_mode="HTML")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in massage_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Дитяче дозвілля")
# def kids_handler(message):
#     texts = [
#         "<b> Westhills — це справжній рай для дітей! </b> \n"
#         "У нас є все, щоб ваші маленькі гості відчували себе як удома та весело проводили час.\n\n"
#         "🛝 Просторий дитячий майданчик з різноманітними гірками та гойдалками, де кожен малюк знайде собі розвагу за смаком;\n"
#         "🎮 Сучасна дитяча кімната з безліччю ігор та розваг, що подарують дітям години захоплюючого дозвілля;\n"
#         "🤹‍♂️ Ігри з аніматором на басейні, які подарують веселощі та позитивні емоції дітям і дорослим;\n"
#         "👩‍🍳 У нашому ресторані проводяться цікаві кулінарні майстер-класи для дітей, де малюки можуть навчитись готувати смачні страви разом з нашими шеф-кухарями.\n\n"
#         "У Westhills ваші діти не лише знайдуть розваги на будь-який смак, а й отримають безліч незабутніх вражень!"
#     ]

#     for text in texts:
#       bot.send_message(message.chat.id, text, parse_mode="HTML")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in kids_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Дитяча кімната")
# def kids_room_handler(message):
#     bot.send_message(message.chat.id, "[🧸Дитяча кімната](https://westhills.com.ua/services/children_room)", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Дитячий майданчик")
# def playground_handler(message):
#     bot.send_message(message.chat.id, "🛝*Наш дитячий майданчик* — це місце, де кожна дитина може відчути себе дослідником та відважним героєм! Тут є різноманітні гірки, гойдалки, лазалки та інші атракціони, що забезпечать веселі та активні ігри. Майданчик побудований з високоякісних та безпечних матеріалів, що гарантують безпеку ваших малюків під час розваг. Це ідеальне місце для маленьких дослідників, де вони можуть знайти нових друзів, розвиватися та весело проводити час на свіжому повітрі.", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Майстер класи, аніматори")
# def activities_handler(message):
#     bot.send_message(message.chat.id, "🎨У Westhills ми пильно дбаємо про кожного члена вашої родини, тому наш дитячий простір розвинений на найвищому рівні. " 
#     "Ми створили все необхідне для того, щоб ваші малюки могли не лише весело, а й корисно проводити час. " 
#     "🌟Ми переконані, що сімейний відпочинок має бути повним радості, емоцій та спільних вражень, і саме тому у нас передбачено безліч активностей для дітей, які дозволяють їм розвиватися та насолоджуватися часом разом з батьками.\n\n" 
#     "——\n\n"
#     "🏖️На території аквазони дітки можуть насолоджуватися веселими іграми з аніматором! Супермен-аніматор завжди готовий розвеселити малечу, організовуючи водні змагання, конкурси та цікаві ігри, які дарують море позитиву і емоцій. Діти не лише весело проводять час, але й розвивають командний дух та активно рухаються.\n\n" 
#     "——\n\n"
#     "🐻На сніданках малечу завжди зустрічає наш фірмовий ведмедик, який обіймає діток, дарує їм кульки та приносить емоції щасливого дитинства, створюючи неймовірну атмосферу радості з самого ранку.\n\n"
#     "——\n\n"
#     "🍕Вихідні у нас також дуже насичені! Для дітей проводяться майстер-класи з приготування піци, бельгійських вафель, тирамісу та пряників,а також цікаві хендмейд заняття, бісероплетіння та багато інших творчих активностей, що дарують дітям не тільки радість, а й нові навички.\n\n"
#     "——\n\n"
#     "✨*У Westhills кожен момент — це незабутнє свято для ваших малюків!*\n\n"
#     "Усі наші заходи ми анонсуємо на сторінці в Instagram та через SMS-розсилку, щоб ви завжди були в курсі всіх новинок та подій для вашої родини.", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Спортивний майданчик")
# def sports_ground_handler(message):
#     texts = [
#         "🏋️‍♂️Наш вуличний спортивний майданчик — це ідеальне місце для тих, хто хоче покращити свою фізичну форму на свіжому повітрі. "
#         " Тут ви знайдете різноманітні вуличні тренажери, у вільному доступі, що дозволяють працювати над різними аспектами вашого фізичного стану. "
#         " Усі тренажери розраховані на використання власної ваги тіла, що забезпечує ефективне і безпечне тренування. "
#         " Майданчик оснащений як кардіо-тренажерами, так і силовими пристроями, що дають можливість зміцнити серцево-судинну систему, розвинути силу та витривалість.\n\n"
#         "🌳Заняття на свіжому повітрі — це не лише фізичне навантаження, а й справжнє задоволення від атмосфери: майданчик розташований серед неймовірного ландшафту Карпатського лісу, де під час тренування можна насолоджуватися краєвидами та свіжим гірським повітрям.\n\n"
#         "Тренування на такому майданчику — це не просто спосіб підтримувати фізичну форму, а й можливість отримати заряд енергії, насолоджуючись природою. "
#     ]

#     for text in texts:
#       bot.send_message(message.chat.id, text, parse_mode="HTML")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in main_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Акції та пропозиції")
# def promotions_offers_handler(message):
#     texts = [
#         "🎉🎁 Для наших гостей ми регулярно організовуємо різноманітні акції та спеціальні пропозиції, щоб зробити їхній відпочинок ще більш приємним і вигідним. "
#         "Ми прагнемо, щоб кожен момент у Westhills був незабутнім, тому часто надаємо можливість скористатися ексклюзивними знижками, подарунками або бонусами на послуги. "
#         "Наші акції та пропозиції дозволяють не лише заощадити, а й зробити відпочинок ще комфортнішим, відкриваючи нові можливості для розваг та релаксації.\n\n"
#         "📲 Слідкуйте за нашими оновленнями, щоб не пропустити вигідні пропозиції!"
#     ]

#     for text in texts:
#       bot.send_message(message.chat.id, text, parse_mode="HTML")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in promotions_offers_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)
    
# @bot.message_handler(func=lambda message: message.text == "Іменна карта -10%")
# def name_card_handler(message):
#     bot.send_message(message.chat.id, "[🪪Іменна карта -10%](https://westhills.com.ua/special/imenna-karta-10)", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Знижка від кількості")
# def quantity_discount_handler(message):
#     bot.send_message(message.chat.id, "[👨‍👩‍👧‍👦Знижка від кількості днів проживання](https://westhills.com.ua/special/znizhka-vid-kilkosti-dniv-prozhivannya)", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Щасливий іменинник")
# def happy_noun_handler(message):
#     bot.send_message(message.chat.id, "[🎂Щасливий іменинник](https://westhills.com.ua/special/shaslivij-imeninnik)", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Знижка для УБД -10%")
# def discount_handler(message):
#     bot.send_message(message.chat.id, "", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Подарунковий сертифікат")
# def gift_certificate_handler(message):
#     bot.send_message(message.chat.id, "[🎁Подарунковий сертифікат](https://westhills.com.ua/special/podarunkovij-sertifikat)", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Події")
# def offers_handler(message):
#     texts = [
#         "🎶У Westhills часто проходять як камерні, так і масштабні події — від концертів українських зірок до закритих гастрономічних вечерь. \n\n"
#         "Кожних вихідних ми розважаємо гостей живою музикою в ресторані, де виступають скрипалі, саксофоністи, гітаристи та інші талановиті музиканти."
#         "На басейні також працює діджей, створюючи чудову атмосферу для відпочинку.💫\n\n"
#         "Для дітей організовуються розважальні програми з аніматором та майстер-класи, що дарують малечі незабутні враження.\n\n"
#         "<b>Також регулярно проводимо аукціони та концерти на підтримку наших військових, збираючи кошти на закупівлю дронів та іншого спорядження.</b>\n\n"
#         "📱Усі заходи анонсуються у наших соціальних мережах, щоб ви завжди були в курсі подій. https://westhills.com.ua/news "
#     ]

#     for text in texts:
#       bot.send_message(message.chat.id, text, parse_mode="HTML")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in main_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Залишити відгук")
# def reviews_handler(message):
#     texts = [
#         "<b>Дякуємо за вибір Westhills cottage town & SPA !</b>\n\n"
#         "Наша команда дбає про кожну деталь, щоб ваш відпочинок був не лише комфортним, а наповненим щирими, яскравими емоціями.\n\n"
#         "Ми будемо раді, якщо ви поділитесь своїм досвідом та враженнями — це допоможе нам краще розуміти ваші потреби та впроваджувати найкращі ідеї для вашого відпочинку❤️"
#     ]

#     for text in texts:
#       bot.send_message(message.chat.id, text, parse_mode="HTML")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in main_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Контакти та інформація")
# def contacts_information_handler(message):
#     texts = [
#     ]

#     for text in texts:
#         bot.send_message(message.chat.id, text, parse_mode="Markdown")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in contacts_information_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Інстаграм")
# def instagram_handler(message):
#     bot.send_message(message.chat.id, "📸 *Наш Instagram:*\n[westhills_cottage_town](https://www.instagram.com/westhills_cottage_town/?hl=uk)", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Тік Ток")
# def tiktok_handler(message):
#     bot.send_message(message.chat.id, "🎵 *Наш TikTok:*\n_(тимчасово відсутній)_", parse_mode="Markdown")  

# @bot.message_handler(func=lambda message: message.text == "Сайт")
# def website_handler(message):
#     bot.send_message(message.chat.id, "🌐*Наш сайт*\nhttps://westhills.com.ua/", parse_mode="Markdown") 

# @bot.message_handler(func=lambda message: message.text == "Рецепція Котеджів")
# def phone_cottages_handler(message):
#     bot.send_message(message.chat.id, "🏡 *Зателефонувати в рецепцію котеджів*\n+380677778144", parse_mode="Markdown") 

# @bot.message_handler(func=lambda message: message.text == "Рецепція Апартаментів", parse_mode="Markdown") 
# def phone_apartments_handler(message):
#     bot.send_message(message.chat.id, "🏢 *Зателефонувати в рецепцію апартаментів*\n+380667778144", parse_mode="Markdown") 

# @bot.message_handler(func=lambda message: message.text == "Відділ бронювання")
# def phone_booking_handler(message):
#     bot.send_message(message.chat.id, "🗓 *Зателефонувати у відділ бронювання*\n+380737778144", parse_mode="Markdown") 

# @bot.message_handler(func=lambda message: message.text == "Ресторан")
# def phone_restaurant_handler(message):
#     bot.send_message(message.chat.id, "🍽 *Зателефонувати у ресторан* \n+380687778144", parse_mode="Markdown") 

# @bot.message_handler(func=lambda message: message.text == "Наша Локація", parse_mode="Markdown") 
# def location_handler(message):
#     bot.send_message(message.chat.id, "📍*Наша локація*\nhttps://maps.app.goo.gl/o9GrjJqiJHUwHKJT6", parse_mode="Markdown") 

# if __name__ == "__main__":
#     bot.infinity_polling()


# import telebot
# from telebot import types
# import os
# from telebot.types import InputMediaPhoto 

# TOKEN = '8123915539:AAFI7M_1WE4PTLzGTT2vG9QDlSFh6ROg1cE'
# bot = telebot.TeleBot(TOKEN)

# # головне меню
# main_menu = [
#     ["Котеджне містечко Westhills"],
#     ["Котеджі/апартаменти", "Ресторан Westhill"],
#     ["Pool & Aquazone", "Pool bar"],
#     ["SPA – центр", "PRIVATE SPA"],
#     ["Додаткові послуги", "Масаж"],
#     ["Дитяче дозвілля", "Спортивний майданчик"],
#     ["Акції та пропозиції", "Події"],
#     ["Залишити відгук", "Контакти та інформація"]
# ]

# # меню Котеджі/апартаменти
# cottages_apartments_menu = [
#     ["Котеджі", "Апартаменти"],
#     ["Додаткове розміщення", "Розміщення з тваринами"],
#     ["⬅️ Назад"]
# ]

# # меню Ресторан Westhill 
# restaurant_westhills_menu = [
#     ["Кухня", "Бар"],
#     ["Винна карта", "Room service"],
#     ["Контакти", "⬅️ Назад"]
# ]

# # меню Pool & Aquazone 
# pool_aquazone_menu = [
#     ["Фото Pool & Aquazone"], 
#     ["⬅️ Назад"]
# ]

# # меню Poll bar
# pool_bar_menu = [
#     ["Меню Pool Bar"],
#     ["⬅️ Назад"]
# ]

# # меню Spa - центр
# spa_center_menu = [
#     ["Фото", "⬅️ Назад"]
# ]

# # меню Private spa
# private_spa_menu = [
#     ["Фото та вартість"],
#     ["⬅️ Назад"]
# ]

# # меню Додаткові послуги
# additional_services_menu = [
#     ["Прокат велосипедів", "Зарядка електромобіля"],
#     ["Оренда зони BBQ", "⬅️ Назад"]
# ]

# # меню Масаж
# massage_menu = [
#     ["Вартість", "⬅️ Назад"]
# ]

# # меню Дитяче дозвілля
# kids_menu = [
#     ["Дитяча кімната", "Дитячий майданчик"],
#     ["Майстер класи, аніматори", "⬅️ Назад"]
# ]

# # меню Акції та пропозиції
# promotions_offers_menu = [
#     ["Іменна карта -10%", "Знижка від кількості днів проживання"],
#     ["Щасливий іменинник", "Подарунковий сертифікат"],
#     ["Знижка для УБД -15%", "⬅️ Назад"]
# ]

# # меню Контакти та інформація
# contacts_information_menu = [
#     ["Тік Ток", "Інстаграм"],
#     ["Сайт", "Рецепція котеджів"],
#     ["Рецепція апартаментів", "Відділ бронювання"],
#     ["Ресторан", "Наша локація"],
#     ["⬅️ Назад"]
# ]

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in main_menu:
#         buttons = [types.KeyboardButton(text) for text in row]
#         markup.add(*buttons)

#     bot.send_message(
#         message.chat.id,
#         "🏡 *Ласкаво просимо до котеджного містечка Westhills!*\n"
#             "Ми пропонуємо сучасну територію з розвиненою інфраструктурою.\n\n"
#             "Westhills ідеально підходить для відпочинку на природі, активних розваг, сімейного відпочинку, корпоративів, свят та спортивних зборів.  "
#             "Незалежно від пори року, ми забезпечимо вам чудовий настрій і незабутні враження. Завдяки кваліфікованому персоналу та індивідуальному підходу, "
#             "ваше перебування в Westhills буде комфортним і приємним.\n\n"
#             "*Контакти:*\n"
#             "+38 (067) 777 81 44 — рецепція котеджів\n"
#             "+38 (066) 777 81 44 — рецепція апартаментів\n"
#             "+38 (068) 777 81 44 — ресторан\n\n"
#             "*Команда котеджного містечка Westhills бажає Вам приємного перебування!*",
#         parse_mode="Markdown",
#         reply_markup=markup
#     )

# @bot.message_handler(func=lambda message: True)
# def menu_handler(message):

#     if message.text == "Котеджне містечко Westhills":
#         with open("cottage-town.jpg", "rb") as photo:
#             bot.send_photo(message.chat.id, photo)

#         bot.send_message(message.chat.id, 
#             "🏡 *Ласкаво просимо до котеджного містечка Westhills!*\n"
#             "Ми пропонуємо сучасну територію з розвиненою інфраструктурою.\n\n"
#             "Westhills ідеально підходить для відпочинку на природі, активних розваг, сімейного відпочинку, корпоративів, свят та спортивних зборів.  "
#             "Незалежно від пори року, ми забезпечимо вам чудовий настрій і незабутні враження. Завдяки кваліфікованому персоналу та індивідуальному підходу, "
#             "ваше перебування в Westhills буде комфортним і приємним.\n\n"
#             "*Контакти:*\n"
#             "+38 (067) 777 81 44 — рецепція котеджів\n"
#             "+38 (066) 777 81 44 — рецепція апартаментів\n"
#             "+38 (068) 777 81 44 — ресторан\n\n"
#             "*Команда котеджного містечка Westhills бажає Вам приємного перебування!*",
#             parse_mode="Markdown"
#         )
#     elif message.text == "Котеджі/апартаменти":
#         cottages_apartments_menu_handler(message)
#     elif message.text == "Ресторан Westhill":
#         restaurant_handler(message)
#     elif message.text == "Pool & Aquazone":
#         pool_aquazone_handler(message)
#     elif message.text == "Pool bar":
#         pool_bar_handler(message)
#     elif message.text == "SPA – центр":
#         spa_center_handler(message)
#     elif message.text == "PRIVATE SPA":
#         private_spa_handler(message)
#     elif message.text == "Додаткові послуги":
#         additional_services_handler(message)
#     elif message.text == "Масаж":
#         massage_handler(message)
#     elif message.text == "Дитяче дозвілля":
#         kids_handler(message)
#     elif message.text == "Спортивний майданчик":
#         sports_ground_handler(message)
#     elif message.text == "Акції та пропозиції":
#         promotions_offers_handler(message)
#     elif message.text == "Події":
#         offers_handler(message)
#     elif message.text == "Залишити відгук":
#         reviews_handler(message)
#     elif message.text == "Контакти та інформація":
#         contacts_information_handler(message)
#     elif message.text == "Котеджі":
#         cottages_handler(message)
#     elif message.text == "Апартаменти":
#         apartments_handler(message)
#     elif message.text == "Додаткове розміщення":
#         additional_accommodation_handler(message)
#     elif message.text == "Розміщення з тваринами":
#         pets_accommodation_handler(message)
#     elif message.text == "Кухня":
#         restaurant_kitchen_handler(message)
#     elif message.text == "Бар":
#         restaurant_bar_handler(message)
#     elif message.text == "Меню Pool Bar":
#         pool_bar_menu_handler(message)
#     elif message.text == "Винна карта":
#         wine_menu_handler(message)
#     elif message.text == "Room service":
#         room_service_handler(message)
#     elif message.text == "Контакти":
#         restaurant_contacts_handler(message)
#     elif message.text == "Фото":
#         restaurant_photos_handler(message)
#     elif message.text == "Фото Pool & Aquazone":
#         pool_photos_handler(message)
#     elif message.text == "Вартість":
#         send_price_pdf(message)
#     elif message.text == "Фото та вартість":
#         photos_prices_handler(message)
#     elif message.text == "Прокат велосипедів":
#         bike_rental_handler(message)
#     elif message.text == "Зарядка електромобіля":
#         ev_charging_handler(message)
#     elif message.text == "Оренда зони BBQ":
#         bbq_zone_rental_handler(message)
#     elif message.text == "Дитяча кімната":
#         kids_room_handler(message)
#     elif message.text == "Дитячий майданчик":
#         playground_handler(message)
#     elif message.text == "Майстер класи, аніматори":
#         activities_handler(message)
#     elif message.text == "Іменна карта -10%":
#         name_card_handler(message)
#     elif message.text == "Знижка від кількості днів проживання":
#         quantity_discount_handler(message)
#     elif message.text == "Щасливий іменинник":
#         happy_noun_handler(message)
#     elif message.text == "Подарунковий сертифікат":
#         gift_certificate_handler(message)
#     elif message.text == "Знижка для УБД -15%":
#         discount_handler(message)
#     elif message.text == "Тік Ток":
#         tiktok_handler(message)
#     elif message.text == "Інстаграм":
#         instagram_handler(message)
#     elif message.text == "Сайт":
#         website_handler(message)
#     elif message.text == "Рецепція котеджів":
#         phone_cottages_handler(message)
#     elif message.text == "Рецепція апартаментів":
#         phone_apartments_handler(message)
#     elif message.text == "Відділ бронювання":
#         phone_booking_handler(message)
#     elif message.text == "Ресторан":
#         phone_restaurant_handler(message)
#     elif message.text == "Наша локація":
#         location_handler(message)
#     elif message.text == "⬅️ Назад":
#         send_main_menu(message)
#     else:
#         bot.send_message(message.chat.id, f"🔎 Інформація про *{message.text}* оновлюється!"
#                          "Ми працюємо над оновленням даних для вас! Дякуємо за розуміння.", parse_mode="Markdown")
                

# def send_price_pdf(message):
#     base_dir = os.path.dirname(__file__)
#     pdf1_path = os.path.join(base_dir, "Вартість_1.pdf")
#     pdf2_path = os.path.join(base_dir, "Вартість_2.pdf")

#     with open(pdf1_path, "rb") as pdf1:
#         bot.send_document(chat_id=message.chat.id, document=pdf1)

#     with open(pdf2_path, "rb") as pdf2:
#         bot.send_document(chat_id=message.chat.id, document=pdf2)

#     bot.send_message(
#         chat_id=message.chat.id,
#         text="✅ Ось ваші прайс-листи!"
#     )

# def send_main_menu(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in main_menu:
#         buttons = [types.KeyboardButton(text) for text in row]
#         markup.add(*buttons)

#     bot.send_message(
#         message.chat.id,
#         text="Оберіть опцію:", 
#         reply_markup=markup 
#     )

# @bot.message_handler(func=lambda message: message.text == "Котеджі/апартаменти")
# def cottages_apartments_menu_handler(message):

#     photo_files = ["cottages-apartments.png"]
#     for filename in photo_files:
#         with open(filename, "rb") as photo:
#             bot.send_photo(message.chat.id, photo)

#     texts = [
#         "🏘Котеджне містечко в Карпатах, де  архітектура зливається з природою, а людина — відновлює сили. "
#         "Тут розташовано 11 будинків, побудованих з дерева та каменю, що гармонійно вписуються в навколишній ландшафт. "
#         "Окрім цього, є окремий корпус з сучасними та просторими апартаментами, які забезпечують комфортне проживання.\n\n"
#         "——\n\n"
#         "🛏 *Проживання та інфраструктура:*\n\n"
#         "• *Критий SPA-центр*: 10:00 – 22:00\n"
#         "  - басейн 8×4 м (30°)\n"
#         "  - басейн-джакузі з випливом на вулицю 7×3×1,3 м\n"
#         "  - фінська парна та турецький хамам\n"
#         "  - два панорамних джакузі (35°)\n"
#         "  - кімната відпочинку з карпатським чаєм\n"
#         "  - панорамна зона з шезлонгами\n\n"
#         "• *Pool & Aquazone*: 09:00 – 21:00\n"
#         "  - відкритий панорамний басейн 350 м² (29°)\n"
#         "  - дитяча aquazone (30°)\n"
#         "  - панорамна зона з шезлонгами\n\n"
#         "——\n\n"
#         "🍳 *Харчування:*\n\n"
#         "• Сніданки включені у вартість проживання (з 08:00 до 11:00 у ресторані Westhill)\n"
#         "• Ресторан Westhill: 13:00 – 23:00 (замовлення приймаються до 22:30)\n"
#         "• Pool bar: 10:00 – 21:00\n"
#         "• Доступний room service з 13:00–22:30.\n"
#         "_Рекомендуємо бронювання столиків заздалегідь._\n\n"
#         "——\n\n"
#         "🦌 *Заповідник з оленями:*\n\n"
#         "Поруч із готелем розташований парк, де мешкають олені та косулі. "
#         "Прогулянки безкоштовні, а тварин можна побачити з різних куточків містечка.\n\n"
#         "——\n\n"
#         "👧 *Для найменших гостей:*\n\n"
#         "• Дитячий майданчик\n• Ігрова кімната\n• Аніматори\n• Майстер-класи\n"
#         "Westhills — справжній рай для дітей, де вони завжди знайдуть щось цікаве!\n\n"
#         "——\n\n"
#         "🅿️ *Паркінг:*\n\n"
#         "Паркінг на території містечка під охороною і з відеоспостереженням — безпечно та зручно.\n\n"
#         "——\n\n"
#         "💪 *Спортивний майданчик:*\n\n"
#         "Вуличні тренажери доступні для всіх гостей, тож спорт і свіже повітря завжди поруч.\n\n"
#         "——\n\n"
#         "📞 *Контакти:*\n"
#         "+38 (067) 777 81 44 — рецепція котеджів\n"
#         "+38 (066) 777 81 44 — рецепція апартаментів\n"
#         "+38 (068) 777 81 44 — ресторан\n\n"
#         "_Інформацію про послуги та розваги шукайте у розділах цього бота або звертайтеся на рецепцію._\n\n"
#         "*Команда котеджного містечка Westhills бажає Вам приємного перебування!*"
#     ]
#     for text in texts:
#         bot.send_message(message.chat.id, text, parse_mode="Markdown")

#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in cottages_apartments_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Котеджі")
# def cottages_handler(message):
#     bot.send_message(message.chat.id, "Програму вашого вікенду, інформацію про послуги та розваги дізнавайтеся у розділах нашого чат-боту. " 
#     "У разі додаткових запитань звертайтеся на рецепцію – будемо раді зробити ваш візит комфортним.\n\n"
#     "https://westhills.com.ua/cottages")
#     # send_cottages_apartments_menu(message)

# @bot.message_handler(func=lambda message: message.text == "Апартаменти")
# def apartments_handler(message):
#     bot.send_message(message.chat.id, "Програму вашого вікенду, інформацію про послуги та розваги дізнавайтеся у розділах нашого чат-боту. " 
#     "У разі додаткових запитань звертайтеся на рецепцію – будемо раді зробити ваш візит комфортним.\n\n"
#     "https://westhills.com.ua/cottages/cottage ")

# @bot.message_handler(func=lambda message: message.text == "Додаткове розміщення")
# def additional_accommodation_handler(message):

#     photo_files = ["additional-accommodation.jpg"]
#     for filename in photo_files:
#         with open(filename, "rb") as photo:
#             bot.send_photo(message.chat.id, photo)

#     bot.send_message(message.chat.id, "У апартаментах 50м2 - можливе розміщення однієї дитини до 3-х років  безкоштовно, " 
#     "або за додаткову плату в залежності від віку:\n\n"
#     "*• 4-6 р. - 800 грн/доба,*\n"
#     "*• 7-11 р. - 1200 грн/доба,*\n"
#     "*• 12+ - 1900 грн/доба.*\n\n"
#     "У котеджах можливе розміщення 1 додаткового місця (для дорослого) – 1900 грн/доба, при умові, якщо відсутні діти старші 3-х років.\n"
#     "❗Діти віком від 12 років вважаються дорослими.\n"
#     "Розміщення у вітальні на дивані.",parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Розміщення з тваринами")
# def pets_accommodation_handler(message):

#     photo_files = ["animal.jpg"]
#     for filename in photo_files:
#         with open(filename, "rb") as photo:
#             bot.send_photo(message.chat.id, photo)

#     bot.send_message(message.chat.id, "*🐾Умови проживання з домашніми улюбленцями:*\n\n"
#     "- вага до 7 кг:\n"
#     "- дозволене розміщення тільки однієї тваринки в номері;\n"
#     "- вигул відбувається тільки у спеціально призначених для цього місцях. Забороняється вигул тваринок на газонах території;\n"
#     "- у місця загального користування (ресторан, SPA-центр, басейн, дитячу кімнату та інші) не дозволено брати з собою домашніх тварин у зв’язку з санітарно-епідеміологічними вимогами;\n"
#     "- забороняється залишати улюбленця самого в номері більше ніж на 1,5 годин;\n"
#     "- у вартість перебування тваринки входить прибирання апартаментів/котеджу після виїзду паровим обладнанням;\n"
#     "- у вартість не входить компенсація у разі пошкодження майна готелю тваринкою. Збиток, нанесений готелю тваринами, компенсується окремо від вартості проживання повною мірою згідно з виставленим рахунком;\n"
#     "- у разі порушення цих умов проживання з домашніми улюбленцями, готель залишає за собою права виселити Гостей з тваринкою без повернення оплати.",
#     parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Ресторан Westhill")
# def restaurant_handler(message):

#     photo_files = ["restaurant.jpg"]
#     for filename in photo_files:
#         with open(filename, "rb") as photo:
#             bot.send_photo(message.chat.id, photo)

#     texts = [
#         "🍽 Ресторан Westhill — це справжня перлина котеджного містечка Westhills, де естетика та кулінарне мистецтво зливаються в одне ціле." 
#         " Сучасний інтер’єр ресторану, витриманий у стилі розкоші та комфорту, створює неповторну атмосферу." 
#         " Панорамні вікна відкривають захоплюючий вигляд на величний карпатський ліс та закритий парк з косулями, що додає ще більше магії цьому місцю." 
#         " У ресторані ви також зможете насолодитися стравами, приготованими в печі, а на відкритій терасі — відпочити та насолодитися атмосферою природи." 
#         " Авторська кухня, бездоганна професійність та висока якість обслуговування залишать у вас незабутні враження та подарують справжнє гастрономічне задоволення." 
#         " Кожна деталь нашого ресторану відображає вишуканий смак і неперевершену майстерність.\n\n\n"

#         "🏠 Ресторан знаходиться в окремій будівлі на початку котеджного містечка.\n\n"
#          "🕰 **Графік роботи**:\n"
#         "13:00 - 23:00\n"
#         "Приймаємо замовлення до 22:30.\n\n"
        
#         "📞 **Контакти**:\n"
#         "Бронюйте ваш столик за телефоном: +38068 777 81 44\n\n"
#         "https://westhills.com.ua/services/restaurant"
#     ]

#     for text in texts:
#         bot.send_message(message.chat.id, text, parse_mode="Markdown")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in restaurant_westhills_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)  

# @bot.message_handler(func=lambda message: message.text == "Кухня")
# def restaurant_kitchen_handler(message):
#     bot.send_message(message.chat.id, "[📖Переглянути меню](https://expz.menu/3d04ea14-c177-4b8c-a4a8-e83c337aed6d/menu?menuId=18922)", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Винна карта")
# def wine_menu_handler(message):
#     bot.send_message(message.chat.id, "[🍇Переглянути винну карту](https://expz.menu/3d04ea14-c177-4b8c-a4a8-e83c337aed6d/menu?menuId=19407)", parse_mode="Markdown")
    
# @bot.message_handler(func=lambda message: message.text == "Бар")
# def restaurant_bar_handler(message):
#     bot.send_message(message.chat.id, "[🍷Переглянути бар ресторану](https://expz.menu/3d04ea14-c177-4b8c-a4a8-e83c337aed6d/menu?menuId=19409)", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Меню Pool Bar")
# def pool_bar_menu_handler(message):
#     bot.send_message(message.chat.id, "[🍷Переглянути меню Pool Bar](https://expz.menu/0b3c5445-1828-48d7-94be-5f5dd417b8f8/menu?menuId=19216)", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Room service")
# def room_service_handler(message):
#     bot.send_message(message.chat.id, "🛎 Смакуйте вишукані страви, не виходячи з котеджу чи апартаментів!\n\n" 
#     "Наш рум сервіс створений для тих, хто бажає насолодитися комфортом та смачною кухнею прямо в номері. " 
#     "Від класичних європейських страв до авторських шедеврів від шефа — ми забезпечимо вам незабутні гастрономічні враження будь-якої миті." 
#     " Оберіть улюблені страви з нашого меню та замовляйте прямо до вашого котеджу чи апартаментів!\n\n" 
#     "📞Замовлення за телефоном +380687778144", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Контакти")
# def restaurant_contacts_handler(message):
#     bot.send_message(message.chat.id, "📞Забронювати столик можна за телефоном: +380687778144 ")
    

# @bot.message_handler(func=lambda message: message.text == "Pool & Aquazone")
# def pool_aquazone_handler(message):

#     media = [
#         InputMediaPhoto(open("pool-aquazone-1.jpg", "rb")),
#         InputMediaPhoto(open("pool-aquazone-2.jpg", "rb")),
#         InputMediaPhoto(open("pool-aquazone-3.jpg", "rb")),
#     ]
#     bot.send_media_group(message.chat.id, media)

#     text = (
#         "🌞Ідеальний відпочинок для всієї родини з дітьми?"
#         " У Westhills це абсолютно реально!\n\n"
#         "- Відкритий басейн з підігрівом, та зоною джакузі для вашого комфорту;\n"
#         "- Водяні гірки та дитячий басейн з підігрівом для маленьких гостей;\n"
#         "- POOL BAR для приємного відпочинку біля води.\n\n"
#         "Ваші діти не будуть нудьгувати, і ви зможете насолоджуватись спокоєм.\n"
#         "А після активного дня — солодкий та спокійний сон гарантовано! Найголовніше — у Westhills ми завжди піклуємось про безпеку наших гостей.\n"
#         "Що може бути важливіше за такі незабутні спогади? Розваги для дітей, комфорт для батьків.\n\n"
#         "*Чекаємо на вас у Westhills, де природа і сучасний комфорт відпочинку створюють ідеальну гармонію!🌿*"
#     )
#     bot.send_message(message.chat.id, text, parse_mode="Markdown")

#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     pool_aquazone_menu = [
#         ["Фото Pool & Aquazone"], 
#         ["⬅️ Назад"]
#     ]
#     for row in pool_aquazone_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)


# @bot.message_handler(func=lambda message: message.text == "Фото")
# def restaurant_photos_handler(message):
#     bot.send_message(message.chat.id, "[📸Переглянути фото](https://westhills.com.ua/services/spa)", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Фото Pool & Aquazone")
# def pool_photos_handler(message):
#     bot.send_message(message.chat.id, "[📸Переглянути фото](https://westhills.com.ua/services/pool)", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Pool bar")
# def pool_bar_handler(message):

#     photo_files = ["pool-bar.jpg"]
#     for filename in photo_files:
#         with open(filename, "rb") as photo:
#             bot.send_photo(message.chat.id, photo)

#     texts = [
#        "🍹На нашому басейні працює Pool Bar, де ви зможете насолодитися різноманітними напоями — від освіжаючих безалкогольних до вишуканих алкогольних коктейлів, що створять ідеальну атмосферу для вашого відпочинку.\n\n"
#        "Ми пропонуємо смачне морозиво, а також широкий вибір страв на кухні, де ви зможете скуштувати піцу чи бургери, приготовані з найкращих інгредієнтів. \n\n"
#        "Усе це забезпечить вам комфорт та насолоду протягом часу, проведеного біля басейну.☀️🏖️"
#     ]

#     for text in texts:
#         bot.send_message(message.chat.id, text, parse_mode="Markdown")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in pool_bar_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "PRIVATE SPA")
# def private_spa_handler(message):

#     photo_files = ["private-spa.jpg"]
#     for filename in photo_files:
#         with open(filename, "rb") as photo:
#             bot.send_photo(message.chat.id, photo)

#     texts = [
#         "🌲<b>Карпатська баня</b> \n\n"
#         "Відвідування сауни в котеджному містечку Westhills — це гарантований шлях до ідеального релаксу та відновлення сил!\n\n"
#         "• Басейн 5*4 м з температурою води 25-26°C та глибиною 1,5 м;\n"
#         "• Баня на дровах з традиційною пропаркою віниками, послуги банщика включені у вартість;\n"
#         "• На терасі ви зможете освіжитися в діжці з крижаною водою або розслабитися в гарячому джакузі;\n"
#         "• Хамам (турецька парова сауна);\n"
#         "• Кімната, наповнена ароматами карпатських трав;\n"
#         "• Масажний кабінет для додаткового розслаблення;\n"
#         "• Зона відпочинку біля каміну для затишного часу.\n\n"
#         "Це приватна зона, де ви та ваша компанія відпочиваєте наодинці, без сторонніх. "
#         "Під час бронювання ви маєте можливість насолоджуватися цією атмосферою в повній приватності. "
#         "Також ви можете замовляти смачні страви та напої з нашого ресторану або приносити свої для ще більшого комфорту.\n\n"
#         "🍵 А ще, наш банщик приготує для вас смачний трав’яний карпатський чай з медом, щоб ваш відпочинок став ще приємнішим!\n\n"
#         "https://westhills.com.ua/services/karpatska_banya "
#     ]

#     for text in texts:
#       bot.send_message(message.chat.id, text, parse_mode="HTML")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in private_spa_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])
    
#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Бар")
# def photos_prices_handler(message):
#     bot.send_message(message.chat.id, "[🌲Фото та вартість Карпатської бані](https://westhills.com.ua/prices )", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "SPA – центр")
# def spa_center_handler(message):

#     photo_files = ["spa.jpg"]
#     for filename in photo_files:
#         with open(filename, "rb") as photo:
#             bot.send_photo(message.chat.id, photo)
#     texts = [
#         "🌿 <b>SPA-центр у Westhills — це місце, де кожна мить відчувається по-новому.</b> \n\n"
#         "Відпочивайте та відновлюйтесь у нашій SPA-зоні, де кожна деталь створена для вашого комфорту.\n\n"
#         "• 2 сауни: хамам та парна;\n"
#         "• Басейн з підігрівом 8x4 м, глибина 1,25 м;\n"
#         "• Басейн-джакузі з виходом на вулицю 7x3x1,3 м, глибина 1,3 м;\n"
#         "• 2 панорамних гарячих джакузі, глибина 0,8-0,9 м;\n"
#         "• Кімната відпочинку з карпатським чаєм;\n"
#         "• Панорамна зона з шезлонгами для вашого релаксу.\n\n"
#         "✨ <b>Залиште всі турботи позаду і створюйте незабутні моменти для себе та своїх близьких у Westhills Cottage Town!</b>"
#     ]

#     for text in texts:
#       bot.send_message(message.chat.id, text, parse_mode="HTML")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in spa_center_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Додаткові послуги")
# def additional_services_handler(message):

#     photo_files = ["additional-services.jpg"]
#     for filename in photo_files:
#         with open(filename, "rb") as photo:
#             bot.send_photo(message.chat.id, photo)

#     texts = [
#        "🚴‍♂️ Активний відпочинок у Westhills – це незабутній час, сповнений приємних вражень, що залишаться з вами назавжди."
#        "Ми пропонуємо різноманітні види активностей для всіх:\n\n"
#        "• оренда мангалу з альтанкою;\n"
#        "• прокат велосипедів;\n"
#        "• відкритий дитячий майданчик;\n"
#        "• тренажерний майданчик на відкритому повітрі;\n"
#        "• прогулянки до лісових мешканців (косуль та оленів), що живуть у нашому заповіднику;\n"
#        "• велика територія для прогулянок і відпочинку.\n\n"
#        "<b>Запрошуємо вас до Westhills – тут ви поринете у справжній відпочинок, ближче до природи і подалі від міського шуму!</b>"
#     ]

#     for text in texts:
#       bot.send_message(message.chat.id, text, parse_mode="HTML")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in additional_services_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Зарядка електромобіля")
# def ev_charging_handler(message):

#     photo_files = ["electric-charging.jpg"]
#     for filename in photo_files:
#         with open(filename, "rb") as photo:
#             bot.send_photo(message.chat.id, photo)

#     bot.send_message(message.chat.id, "🔌*Включення/відключення зарядки за допомогою картки ТОКА :*\n\n" 
#     "Наявні два типи портів Type 1, Type 2. \n\n" 
#     "• Під’їхавши до зарядної станції мережі «ТОКА», Вам необхідно вставити зарядний кабель у відповідний  роз’єм  електромобіля;\n" 
#     "• Для запуску процесу зарядки, піднесіть картку мережі «ТОКА» до зчитувача на станції;\n" 
#     "• Для припинення процесу зарядки, дістаньте зарядний кабель із зарядної станції.\n\n" 
#     "Станція знаходиться у внутрішньому дворі, на паркінгу.\n\n" 
#     "💲Вартість послуги  – 17 грн -1 кВт, розрахунок відбувається на центральній рецепції Westhills", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Оренда зони BBQ")
# def bbq_zone_rental_handler(message):

#     photo_files = ["grill.jpg"]
#     for filename in photo_files:
#         with open(filename, "rb") as photo:
#             bot.send_photo(message.chat.id, photo)

#     bot.send_message(message.chat.id, "🍖*Запрошуємо вас насолодитися чудовим відпочинком на свіжому повітрі з орендою зони BBQ у Westhills.*\n\n " 
#     "Насолоджуйтесь смачними стравами, приготованими на мангалі, в затишній альтанці серед природи. " 
#     "Усе необхідне для приготування барбекю – мангал, інвентар та комфортна альтанка – вже підготовлено для вас. " 
#     "Створіть незабутні спогади, насолоджуючись природою та смачними стравами на свіжому повітрі!\n\n" 
#     "💲Вартість послуги – 900 грн за 2 години,  оренда здійснюється за попереднім замовленням.", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Прокат велосипедів")
# def bike_rental_handler(message):

#     photo_files = ["bicycles.jpg"]
#     for filename in photo_files:
#         with open(filename, "rb") as photo:
#             bot.send_photo(message.chat.id, photo)

#     bot.send_message(message.chat.id, "🚴‍♂️*Прокат велосипедів у Westhills – ідеальний спосіб активно провести час на свіжому повітрі!*\n\n" 
#     "У нас є велосипеди для дорослих і для дітей, а також дитячі крісла та замочки для вашої зручності. \n\n" 
#     "Відправляйтесь на велопрогулянку по мальовничих стежках та насолоджуйтесь красою природи Карпат.\n\n" 
#     "Вартість прокату  велосипеду: \n\n" 
#     "1️⃣ година - 200 грн\n"
#     "2️⃣ години - 300 грн\n"
#     "3️⃣ години - 400 грн\n"
#     "⏩ Кожна наступна година - 100 грн", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Масаж")
# def massage_handler(message):

#     photo_files = ["massages.jpg"]
#     for filename in photo_files:
#         with open(filename, "rb") as photo:
#             bot.send_photo(message.chat.id, photo)

#     texts = [
#         "💆‍♀️Запрошуємо вас поринути у світ розкоші та релаксу, де кожен дотик створює атмосферу гармонії і відновлення. "
#         "Наш масажний кабінет — це місце, де ви зможете відчути справжню силу карпатських гір, занурюючись у відчуття спокою та енергії природи. "
#         "Ми поєднуємо традиційні методи масажу з авторськими техніками, що розроблені спеціально для того, щоб кожен сеанс приносив максимальний ефект відновлення.\n\n"
#         "Наші майстри використовують тільки найкращу преміальну косметику, яка дарує вашій шкірі ніжний догляд та живлення, сприяючи глибокому розслабленню. "
#         "Від класичного масажу до комплексних процедур, ми пропонуємо широкий спектр послуг для тих, хто прагне відновити сили, покращити самопочуття та отримати незабутні враження.\n\n"
#         "<b>Завітайте до нас і насолоджуйтесь не тільки висококласним обслуговуванням, але й атмосферою, яка відновлює та дарує гармонію.✨</b>"
#     ]

#     for text in texts:
#       bot.send_message(message.chat.id, text, parse_mode="HTML")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in massage_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "⬅️ Назад")
# def back_handler(message):
#     bot.send_message(message.chat.id, "Повернулися назад")

# @bot.message_handler(func=lambda message: message.text == "Дитяче дозвілля")
# def kids_handler(message):

#     media = [
#         InputMediaPhoto(open("childrens-leisure-time-1.jpg", "rb")),
#         InputMediaPhoto(open("childrens-leisure-time-2.jpg", "rb")),
#         InputMediaPhoto(open("childrens-leisure-time-3.jpg", "rb")),
#     ]
#     bot.send_media_group(message.chat.id, media)

#     texts = [
#         "<b> Westhills — це справжній рай для дітей! </b> \n"
#         "У нас є все, щоб маленькі гості відчували себе як удома та весело проводили час.\n\n"
#         "💫 Просторий дитячий майданчик з різноманітними гірками та гойдалками, де кожен малюк знайде собі розвагу за смаком;\n"
#         "🎮 Сучасна дитяча кімната з безліччю ігор та розваг, що подарують дітям години захоплюючого дозвілля;\n"
#         "🤹‍♂️ Ігри з аніматором на басейні, які подарують веселощі та позитивні емоції дітям і дорослим;\n"
#         "👩‍🍳 У нашому ресторані проводяться цікаві кулінарні майстер-класи для дітей, де малюки можуть навчитись готувати смачні страви разом з нашими шеф-кухарями.\n\n"
#         "У Westhills ваші діти не лише знайдуть розваги на будь-який смак, а й отримають безліч незабутніх вражень!"
#     ]

#     for text in texts:
#       bot.send_message(message.chat.id, text, parse_mode="HTML")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in kids_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Дитяча кімната")
# def kids_room_handler(message):

#     photo_files = ["childrens-room.jpg"]
#     for filename in photo_files:
#         with open(filename, "rb") as photo:
#             bot.send_photo(message.chat.id, photo)

#     description = (
#         "✨*Дитяча кімната — це особливий, казковий простір, який ми з любов’ю створили для найменших відвідувачів Westhills.*\n\n"
#         "Це багатофункціональна зона, що поєднує в собі місце для ігор, творчості та фантазій, а також затишне середовище для відпочинку й розвитку дитини.\n\n"
#         "У певні дні тижня в нашій дитячій кімнаті працює аніматор, який дарує малюкам яскраві враження завдяки веселій програмі розваг.\n\n"
#         "Адже саме незабутні емоції — це найцінніший подарунок для дітей.🎨"
#     )

#     link = "[🧸Дитяча кімната](https://westhills.com.ua/services/children_room)"

#     bot.send_message(message.chat.id, description, parse_mode="Markdown")
#     bot.send_message(message.chat.id, link, parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Дитячий майданчик")
# def playground_handler(message):

#     photo_files = ["childrens-playground.jpg"]
#     for filename in photo_files:
#         with open(filename, "rb") as photo:
#             bot.send_photo(message.chat.id, photo)

#     bot.send_message(message.chat.id, "💫*Дитячий майданчик* — це місце, де кожна дитина може відчути себе дослідником та відважним героєм! Тут є різноманітні гірки, гойдалки, лазалки та інші атракціони, що забезпечать веселі та активні ігри. Майданчик побудований з високоякісних та безпечних матеріалів, що гарантують безпеку ваших малюків під час розваг. Це ідеальне місце для маленьких дослідників, де вони можуть знайти нових друзів, розвиватися та весело проводити час на свіжому повітрі.", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Майстер класи, аніматори")
# def activities_handler(message):

#     media = [
#         InputMediaPhoto(open("master-classes.jpg", "rb")),
#         InputMediaPhoto(open("master-classes-2.jpg", "rb")),
#     ]
#     bot.send_media_group(message.chat.id, media)

#     bot.send_message(message.chat.id, "🎨У Westhills ми пильно дбаємо про кожного члена вашої родини, тому дитячий простір розвинений на найвищому рівні. " 
#     "Ми створили все необхідне для того, щоб ваші малюки могли не лише весело, а й корисно проводити час. " 
#     "🌟Сімейний відпочинок має бути повним радості, емоцій та спільних вражень, і саме тому у Westhills передбачено безліч активностей для дітей, які дозволяють їм розвиватися та насолоджуватися часом разом з батьками.\n\n" 
#     "——\n\n"
#     "🏖️На території аквазони дітки можуть насолоджуватися веселими іграми з аніматором! Супермен-аніматор завжди готовий розвеселити малечу, організовуючи водні змагання, конкурси та цікаві ігри, які дарують море позитиву і емоцій. Діти не лише весело проводять час, але й розвивають командний дух та активно рухаються.\n\n" 
#     "——\n\n"
#     "🐻На сніданках малечу завжди зустрічає наш фірмовий ведмедик, який обіймає діток, дарує їм кульки та приносить емоції щасливого дитинства, створюючи неймовірну атмосферу радості з самого ранку.\n\n"
#     "——\n\n"
#     "🍕Вихідні у нас також дуже насичені! Для дітей проводяться майстер-класи з приготування піци, бельгійських вафель, тирамісу та пряників,а також цікаві хендмейд заняття, бісероплетіння та багато інших творчих активностей, що дарують дітям не тільки радість, а й нові навички.\n\n"
#     "——\n\n"
#     "✨*У Westhills кожен момент — це незабутнє свято для ваших малюків!*\n\n"
#     "Усі наші заходи ми анонсуємо на сторінці в Instagram та через SMS-розсилку, щоб ви завжди були в курсі всіх новинок та подій для вашої родини.", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Спортивний майданчик")
# def sports_ground_handler(message):

#     photo_files = ["playground.jpg"]
#     for filename in photo_files:
#         with open(filename, "rb") as photo:
#             bot.send_photo(message.chat.id, photo)

#     texts = [
#         "🏋️‍♂️Наш вуличний спортивний майданчик — це ідеальне місце для тих, хто хоче покращити свою фізичну форму на свіжому повітрі. "
#         " Тут ви знайдете різноманітні вуличні тренажери, у вільному доступі, що дозволяють працювати над різними аспектами вашого фізичного стану. "
#         " Усі тренажери розраховані на використання власної ваги тіла, що забезпечує ефективне і безпечне тренування. "
#         " Майданчик оснащений як кардіо-тренажерами, так і силовими пристроями, що дають можливість зміцнити серцево-судинну систему, розвинути силу та витривалість.\n\n"
#         "🌳Заняття на свіжому повітрі — це не лише фізичне навантаження, а й справжнє задоволення від атмосфери: майданчик розташований серед неймовірного ландшафту Карпатського лісу, де під час тренування можна насолоджуватися краєвидами та свіжим гірським повітрям.\n\n"
#         "Тренування на такому майданчику — це не просто спосіб підтримувати фізичну форму, а й можливість отримати заряд енергії, насолоджуючись природою. "
#     ]

#     for text in texts:
#       bot.send_message(message.chat.id, text, parse_mode="HTML")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in main_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Акції та пропозиції")
# def promotions_offers_handler(message):
#     texts = [
#         "🎉🎁 Для наших гостей ми регулярно організовуємо різноманітні акції та спеціальні пропозиції, щоб зробити їхній відпочинок ще більш приємним і вигідним. "
#         "Ми прагнемо, щоб кожен момент у Westhills був незабутнім, тому часто надаємо можливість скористатися ексклюзивними знижками, подарунками або бонусами на послуги. "
#         "Наші акції та пропозиції дозволяють не лише заощадити, а й зробити відпочинок ще комфортнішим, відкриваючи нові можливості для розваг та релаксації.\n\n"
#         "📲 Слідкуйте за нашими оновленнями, щоб не пропустити вигідні пропозиції!"
#     ]

#     for text in texts:
#       bot.send_message(message.chat.id, text, parse_mode="HTML")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in promotions_offers_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)
    
# @bot.message_handler(func=lambda message: message.text == "Іменна карта -10%")
# def name_card_handler(message):
#     bot.send_message(message.chat.id, "[🪪Іменна карта -10%](https://westhills.com.ua/special/imenna-karta-10)", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Знижка від кількості днів проживання")
# def quantity_discount_handler(message):
#     bot.send_message(message.chat.id, "[👨‍👩‍👧‍👦Знижка від кількості днів проживання](https://westhills.com.ua/special/znizhka-vid-kilkosti-dniv-prozhivannya)", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Щасливий іменинник")
# def happy_noun_handler(message):
#     bot.send_message(message.chat.id, "[🎂Щасливий іменинник](https://westhills.com.ua/special/shaslivij-imeninnik)", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Знижка УБД -15%")
# def discount_handler(message):
#     bot.send_message(message.chat.id, "[💙💛Знижка УБД -15%](https://westhills.com.ua/special/ubd)", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Подарунковий сертифікат")
# def gift_certificate_handler(message):
#     bot.send_message(message.chat.id, "[🎁Подарунковий сертифікат](https://westhills.com.ua/special/podarunkovij-sertifikat)", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Події")
# def offers_handler(message):

#     media = [
#         InputMediaPhoto(open("event-1.jpg", "rb")),
#         InputMediaPhoto(open("event-2.jpg", "rb")),
#         InputMediaPhoto(open("event-3.jpg", "rb")),
#     ]
#     bot.send_media_group(message.chat.id, media)

#     texts = [
#         "🎶У Westhills часто проходять як камерні, так і масштабні події — від концертів українських зірок до закритих гастрономічних вечерь. \n\n"
#         "Кожних вихідних ми розважаємо гостей живою музикою в ресторані, де виступають скрипалі, саксофоністи, гітаристи та інші талановиті музиканти. "
#         "На басейні також працює діджей, створюючи чудову атмосферу для відпочинку.💫\n\n"
#         "Для дітей організовуються розважальні програми з аніматором та майстер-класи, що дарують малечі незабутні враження.\n\n"
#         "<b>Також регулярно проводимо аукціони та концерти на підтримку наших військових, збираючи кошти на закупівлю дронів та іншого спорядження.</b>\n\n"
#         "📱Усі заходи анонсуються у наших соціальних мережах, щоб ви завжди були в курсі подій. https://westhills.com.ua/news "
#     ]

#     for text in texts:
#       bot.send_message(message.chat.id, text, parse_mode="HTML")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in main_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Залишити відгук")
# def reviews_handler(message):
#     texts = [
#         "<b>Дякуємо за вибір Westhills Cottage Town & SPA !</b>\n\n"
#         "Наша команда дбає про кожну деталь, щоб ваш відпочинок був не лише комфортним, а наповненим щирими, яскравими емоціями.\n\n"
#         "Ми будемо раді, якщо ви поділитесь своїм досвідом та враженнями — це допоможе нам краще розуміти ваші потреби та впроваджувати найкращі ідеї для вашого відпочинку❤️\n\n"
#         "https://docs.google.com/forms/d/e/1FAIpQLSdyo8H5065kd3DgYNIEHaOM361eeA35dcFdqzg9GJ2VPjVedA/viewform?usp=header"
#     ]

#     for text in texts:
#       bot.send_message(message.chat.id, text, parse_mode="HTML")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in main_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Контакти та інформація")
# def contacts_information_handler(message):
#     texts = [
#     ]

#     for text in texts:
#         bot.send_message(message.chat.id, text, parse_mode="Markdown")
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for row in contacts_information_menu:
#         markup.add(*[types.KeyboardButton(text) for text in row])

#     bot.send_message(message.chat.id, "Оберіть опцію:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Інстаграм")
# def instagram_handler(message):
#     bot.send_message(message.chat.id, "📸 *Наш Instagram:*\n[westhills_cottage_town](https://www.instagram.com/westhills_cottage_town/?hl=uk)", parse_mode="Markdown")

# @bot.message_handler(func=lambda message: message.text == "Тік Ток")
# def tiktok_handler(message):
#     bot.send_message(message.chat.id, "🎵 *Наш TikTok:*\nhttps://www.tiktok.com/@westhills.cottage?_t=ZM-8xgVPM6JoYv&_r=1 ", parse_mode="Markdown")  

# @bot.message_handler(func=lambda message: message.text == "Сайт")
# def website_handler(message):
#     bot.send_message(message.chat.id, "🌐*Наш сайт*\nhttps://westhills.com.ua/", parse_mode="Markdown") 

# @bot.message_handler(func=lambda message: message.text == "Рецепція котеджів")
# def phone_cottages_handler(message):
#     bot.send_message(message.chat.id, "🏡 *Зателефонувати в рецепцію котеджів*\n+380677778144", parse_mode="Markdown") 

# @bot.message_handler(func=lambda message: message.text == "Рецепція апартаментів", parse_mode="Markdown") 
# def phone_apartments_handler(message):
#     bot.send_message(message.chat.id, "🏢 *Зателефонувати в рецепцію апартаментів*\n+380667778144", parse_mode="Markdown") 

# @bot.message_handler(func=lambda message: message.text == "Відділ бронювання")
# def phone_booking_handler(message):
#     bot.send_message(message.chat.id, "🗓 *Зателефонувати у відділ бронювання*\n+380737778144", parse_mode="Markdown") 

# @bot.message_handler(func=lambda message: message.text == "Ресторан")
# def phone_restaurant_handler(message):
#     bot.send_message(message.chat.id, "🍽 *Зателефонувати у ресторан* \n+380687778144", parse_mode="Markdown") 

# @bot.message_handler(func=lambda message: message.text == "Наша локація", parse_mode="Markdown") 
# def location_handler(message):
#     bot.send_message(message.chat.id, "📍*Наша локація*\nhttps://maps.app.goo.gl/X9HPA7mzDCQm4zqT7", parse_mode="Markdown") 

import os
import telebot
from telebot import types

TOKEN = "8297975325:AAEKXiKd_iBubZ-_HtRAPNx4IVVOdTIu1_w"
ADMIN_ID = [733841797, 8073693021]
bot = telebot.TeleBot(TOKEN)

complexes = [
    # "«Кварлал Липки-2» - вул. Мазепи 168",
    "«Квартал Галицький» - вул. Хіміків 35, 37, 39",
    "«Квартал Галицький 2» - вул. Хіміків, 43",
    "«Левада Дем’янів Лаз» - вул. Демʼянів Лаз 35, 37, 39",
    "«Квартал Галичанка» - вул. Галицька 59А",
    "«Квартал Гімназійний» - вул. Горбачевського 14Е",
]

address_files = {
    "«Кварлал Липки-2»": "kvartal_lipki_2.txt",
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
        parse_mode="Markdown"
    )

    user_data[message.chat.id]["waiting_pib"] = True
    bot.send_message(message.chat.id, "👋Будь ласка, введіть ваше ПІБ:")


@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("waiting_pib", False))
def get_pib(message):
    user_data[message.chat.id]["pib"] = message.text
    user_data[message.chat.id]["waiting_pib"] = False
    user_data[message.chat.id]["waiting_exact_address"] = True

    bot.send_message(message.chat.id, "🚪Вкажіть, будь ласка, вашу точну адресу та номер квартири:")


@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("waiting_exact_address", False))
def get_exact_address(message):
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
            reply_markup=types.ReplyKeyboardRemove()
        )
        send_main_menu(message.chat.id)


@bot.message_handler(func=lambda message: message.text == "Мій рахунок")
def show_account(message):
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
    bot.send_message(ADMIN_ID, admin_text, parse_mode="Markdown")

    bot.send_message(
        message.chat.id,
        "✅ Ваш запит прийнято. Найближчим часом ми надішлемо інформацію про ваш рахунок.",
    )


@bot.message_handler(func=lambda message: message.text == "Залишити звернення")
def leave_complaint(message):
    user_data[message.chat.id]["waiting_complaint"] = True
    bot.send_message(message.chat.id, "Будь ласка, опишіть вашу проблему:")


@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("waiting_complaint", False))
def complaint_text(message):
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


@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("waiting_photo", False))
def complaint_photo_choice(message):
    user_data[message.chat.id]["waiting_photo"] = False
    choice = message.text

    if choice == "Так 📸":
        user_data[message.chat.id]["waiting_photo_upload"] = True
        bot.send_message(message.chat.id, "Будь ласка, надішліть фото:", reply_markup=types.ReplyKeyboardRemove())
    else:
        send_complaint_to_admin(message.chat.id)
        bot.send_message(message.chat.id, "✅ Дякуємо за звернення! Ми з вами зв'яжемося найближчим часом.")
        send_main_menu(message.chat.id)


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

    if photo_id:
        bot.send_photo(ADMIN_ID, photo_id, caption=admin_text, parse_mode="Markdown")
    else:
        bot.send_message(ADMIN_ID, admin_text, parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == "Актуальні оголошення")
def announcements(message):
    complex_name = user_data.get(message.chat.id, {}).get("complex")
    if not complex_name:
        bot.send_message(message.chat.id, "Спочатку оберіть адресу командою /start")
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
        bot.send_message(message.chat.id, "Спочатку оберіть адресу командою /start")
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
        "Бухгалтерія: +38 (050) 197 24 85\n"
        "Техвідділ: +38 (095) 681 30 40"
    )
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📘 Facebook", url="https://www.facebook.com/%D0%9B%D0%B5%D0%B2%D0%B0%D0%B4%D0%B0-213141559222862/"))
    markup.add(types.InlineKeyboardButton("📹 YouTube", url="https://www.youtube.com/channel/UCBxxdQ10jUh2EXib2ibcUKA?disable_polymer=true"))
    markup.add(types.InlineKeyboardButton("📸 Instagram", url="https://www.instagram.com/levada.if?igsh=MWhqa2xwMHUzNGRkNw=="))
    bot.send_message(message.chat.id, contacts_text, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Обрати іншу адресу 🔙")
def change_address(message):
    send_complex_menu(message.chat.id)


print("Бот запущений...")
bot.delete_my_commands()
bot.polling(none_stop=True)

