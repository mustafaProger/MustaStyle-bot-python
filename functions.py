import telebot
from telebot import TeleBot, types
models_watch = {
    'Rolex': {
        'Submariner': '600,000 - 2,700,000 руб.',
        'Datejust': '525,000 - 3,750,000 руб.',
        'Day-Date': '1,875,000 - 7,500,000 руб.',
        'GMT-Master II': '675,000 - 3,750,000 руб.',
        'Explorer': '450,000 - 1,875,000 руб.',
        'Yacht-Master': '825,000 - 3,750,000 руб.',
        'Sea-Dweller': '825,000 - 1,500,000 руб.',
        'Daytona': '975,000 - 6,000,000 руб.',
        'Milgauss': '600,000 - 1,500,000 руб.',
        'Oyster Perpetual': '375,000 - 1,500,000 руб.',
    },
    'Omega': {
        'Speedmaster': '400,000 - 2,000,000 руб.',
        'Seamaster': '350,000 - 1,800,000 руб.',
        'Constellation': '500,000 - 2,500,000 руб.',
        'De Ville': '450,000 - 2,000,000 руб.',
        'Aqua Terra': '300,000 - 1,500,000 руб.',
        'Planet Ocean': '600,000 - 3,000,000 руб.',
        'Railmaster': '350,000 - 1,500,000 руб.',
        'Globemaster': '600,000 - 3,500,000 руб.',
        'Bullhead': '500,000 - 2,500,000 руб.',
        'Ploprof': '700,000 - 3,500,000 руб.',
    },
    'Patek Philippe': {
        'Calatrava': '1,500,000 - 3,750,000 руб.',
        'Nautilus': '2,250,000 - 22,500,000 руб.',
        'Aquanautilus': '3,000,000 - 30,000,000 руб.',
        'Twenty~4': '800,000 - 8,000,000 руб.',
        'Gondolo': '1,000,000 - 5,000,000 руб.',
        'Complications': '2,000,000 - 15,000,000 руб.',
        'Golden Ellipse': '1,200,000 - 10,000,000 руб.',
        'Grand Complications': '5,000,000 - 50,000,000 руб.',
        'Calatrava Pilot': '2,000,000 - 20,000,000 руб.',
        'Aquanaut': '3,500,000 - 35,000,000 руб.',
    },
    'Audemars Piguet': {
        'Royal Oak': '1,000,000 - 20,000,000 руб.',
        'Royal Oak Offshore': '1,500,000 - 25,000,000 руб.',
        'Royal Oak Concept': '3,000,000 - 30,000,000 руб.',
        'Millenary': '750,000 - 10,000,000 руб.',
        'Jules Audemars': '1,200,000 - 15,000,000 руб.',
        'Haute Joaillerie': '5,000,000 - многомиллионные руб.',
        'Code 11.59': '2,000,000 - 25,000,000 руб.',
        'Edward Piguet': '1,500,000 - 18,000,000 руб.',
        'Tradition': '800,000 - 12,000,000 руб.',
        'Royal Oak Tourbillon': '3,500,000 - 40,000,000 руб.',
    },
    'Tag Heuer': {
        'Carrera': '50,000 - 500,000 руб.',
        'Monaco': '60,000 - 600,000 руб.',
        'Aquaracer': '40,000 - 400,000 руб.',
        'Formula 1': '30,000 - 300,000 руб.',
        'Connected': '70,000 - 700,000 руб.',
        'Autavia': '55,000 - 550,000 руб.',
        'Link': '45,000 - 450,000 руб.',
        'Kirium': '40,000 - 400,000 руб.',
        'Carrera Heuer 02': '65,000 - 650,000 руб.',
        'Carrera Calibre 16': '60,000 - 600,000 руб.',
    },
    'Seiko': {
        'Presage': '20,000 - 200,000 руб.',
        'Prospex': '30,000 - 300,000 руб.',
        'Astron': '50,000 - 500,000 руб.',
        '5': '10,000 - 100,000 руб.',
        'Premier': '40,000 - 400,000 руб.',
        'Velatura': '25,000 - 250,000 руб.',
        'Recraft': '15,000 - 150,000 руб.',
        'Ananta': '60,000 - 600,000 руб.',
        'Brightz': '45,000 - 450,000 руб.',
        'Lukia': '35,000 - 350,000 руб.',
        },
        'Casio': {
        'G-Shock': '5,000 - 50,000 руб.',
        'Edifice': '10,000 - 100,000 руб.',
        'Pro Trek': '15,000 - 150,000 руб.',
        'Vintage': '3,000 - 30,000 руб.',
        'Baby-G': '4,000 - 40,000 руб.',
        'Wave Ceptor': '7,000 - 70,000 руб.',
        'Illuminator': '2,000 - 20,000 руб.',
        'Databank': '2,500 - 25,000 руб.',
        'Beside': '6,000 - 60,000 руб.',
        'Sheen': '8,000 - 80,000 руб.',
    },

    'Fossil': {
        'Gen 6': '15,000 - 35,000 руб.',
        'Hybrid HR Collider': '10,000 - 25,000 руб.',
        'Solar': '12,000 - 30,000 руб.',
        'The Carlyle HR': '14,000 - 40,000 руб.',
        'Monroe': '7,000 - 20,000 руб.',
        'Nate': '9,000 - 22,000 руб.',
        'Machine': '8,000 - 18,000 руб.',
        'Forrester': '10,000 - 24,000 руб.',
        'The Minimalist': '6,000 - 15,000 руб.',
        'Neutra': '5,000 - 12,000 руб.',
    },

    'Citizen': {
        'Eco-Drive': '10,000 - 30,000 руб.',
        'Promaster': '15,000 - 50,000 руб.',
        'Chandler': '7,000 - 20,000 руб.',
        'L': '20,000 - 60,000 руб.',
        'Satellite Wave': '25,000 - 70,000 руб.',
        'Signature Collection': '30,000 - 80,000 руб.',
        'Corso': '12,000 - 40,000 руб.',
        'Paradigm': '18,000 - 50,000 руб.',
        'Brycen': '15,000 - 45,000 руб.',
        'Nighthawk': '20,000 - 55,000 руб.',
    },

    'Timex': {
        'Expedition': '3,000 - 10,000 руб.',
        'Weekender': '2,000 - 7,000 руб.',
        'Ironman': '4,000 - 15,000 руб.',
        'Fairfield': '3,000 - 12,000 руб.',
        'Metropolitan': '5,000 - 20,000 руб.',
        'Waterbury': '6,000 - 25,000 руб.',
        'Marlin': '8,000 - 30,000 руб.',
        'Standard': '4,000 - 18,000 руб.',
        'Allied': '5,000 - 22,000 руб.',
        'Navi': '7,000 - 28,000 руб.',
    },
        'Swatch': {
        'Sistem51': '5,000 - 15,000 руб.',
        'Originals': '3,000 - 10,000 руб.',
        'Irony': '4,000 - 12,000 руб.',
        'Skin': '6,000 - 18,000 руб.',
        'Scuba Libre': '7,000 - 20,000 руб.',
        'Big Bold': '8,000 - 25,000 руб.',
        'X 007': '10,000 - 30,000 руб.',
        'X You': '6,000 - 15,000 руб.',
        'Art Specials': '7,000 - 18,000 руб.',
        'POP': '3,000 - 10,000 руб.',
    },

    'Tissot': {
        'Le Locle': '15,000 - 40,000 руб.',
        'T-Touch': '30,000 - 80,000 руб.',
        'Visodate': '20,000 - 50,000 руб.',
        'PRS 516': '25,000 - 60,000 руб.',
        'V8': '18,000 - 45,000 руб.',
        'Carson': '22,000 - 55,000 руб.',
        'Couturier': '28,000 - 70,000 руб.',
        'Tradition': '12,000 - 35,000 руб.',
        'Heritage': '40,000 - 100,000 руб.',
        'Seastar 1000': '35,000 - 90,000 руб.',
    },

    'Bulova': {
        'Precisionist': '25,000 - 60,000 руб.',
        'Marine Star': '30,000 - 70,000 руб.',
        'Lunar Pilot': '40,000 - 90,000 руб.',
        'Curv': '35,000 - 80,000 руб.',
        'Accutron': '50,000 - 100,000 руб.',
        'Sutton': '20,000 - 45,000 руб.',
        'Wilton': '15,000 - 35,000 руб.',
        'Maquina': '10,000 - 25,000 руб.',
        'Computron': '25,000 - 55,000 руб.',
        'Aerojet': '18,000 - 40,000 руб.',
    },

    'Michael Kors': {
        'Access Runway': '15,000 - 35,000 руб.',
        'Lexington': '18,000 - 40,000 руб.',
        'Parker': '12,000 - 30,000 руб.',
        'Bradshaw': '20,000 - 50,000 руб.',
        'Sofie': '25,000 - 60,000 руб.',
        'Pyper': '10,000 - 25,000 руб.',
        'Darci': '22,000 - 55,000 руб.',
        'Jaryn': '14,000 - 35,000 руб.',
        'Blair': '28,000 - 70,000 руб.',
        'Mini Slim Runway': '18,000 - 45,000 руб.',
    },

    'DIOR': {
        'VIII Montaigne': '100,000 - 1,000,000 руб.',
        'VIII Grand Bal': '150,000 - 2,000,000 руб.',
        'Chiffre Rouge': '80,000 - 800,000 руб.',
        'La D de DIOR': '120,000 - 1,200,000 руб.',
        'Grand Soir': '200,000 - 2,500,000 руб.',
        'Christal': '90,000 - 1,000,000 руб.',
        'Vortex': '180,000 - 2,000,000 руб.',
        'Inversé': '150,000 - 1,500,000 руб.',
        'Mini D': '70,000 - 800,000 руб.',
        'La Mini D de DIOR': '60,000 - 700,000 руб.',
    }
}


TOKEN = "6556679332:AAGd4ZDmpWh1O9luTfeUKSGXUjdAAzEPiJ4"
bot = telebot.TeleBot(TOKEN)

def show_all_models(choose_watch, model_1, model_2, model_3, model_4, model_5, model_6, model_7, model_8, model_9, model_10, about_price, message):
    bot.send_message(message.chat.id,  f'Отлично, {message.from_user.first_name}, ваш выбор пал на фирму {choose_watch}.')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(model_1)
    btn2 = types.KeyboardButton(model_2)
    btn3 = types.KeyboardButton(model_3)
    btn4 = types.KeyboardButton(model_4)
    btn5 = types.KeyboardButton(model_5)
    btn6 = types.KeyboardButton(model_6)
    btn7 = types.KeyboardButton(model_7)
    btn8 = types.KeyboardButton(model_8)
    btn9 = types.KeyboardButton(model_9)
    btn10 = types.KeyboardButton(model_10)
    btn11 = types.KeyboardButton(about_price)
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
    bot.send_message(message.chat.id, 'Теперь выберите модель часов.',  parse_mode='html', reply_markup=markup)

def show_prices(model_1, price_1, model_2, price_2, model_3, price_3, model_4, price_4, model_5, price_5, model_6, price_6, model_7, price_7, model_8, price_8, model_9, price_9, model_10, price_10, message):
    models_and_price = f"<b>1. {model_1}</b>\n    <i>{price_1}</i>\n<b>2. {model_2}</b>\n    <i>{price_2}</i>\n<b>3. {model_3}</b>\n    <i>{price_3}</i>\n<b>4. {model_4}</b>\n    <i>{price_4}</i>\n<b>5. {model_5}</b>\n    <i>{price_5}</i>\n<b>6. {model_6}</b>\n    <i>{price_6}</i>\n<b>7. {model_7}</b>\n    <i>{price_7}</i>\n<b>8. {model_8}</b>\n    <i>{price_8}</i>\n<b>9. {model_9}</b>\n    <i>{price_9}</i>\n<b>10. {model_10}</b>\n    <i>{price_10}</i>\n"
    bot.send_message(message.chat.id, models_and_price,  parse_mode='html')


# # def about_model(model_1, price_1, model_2, price_2, model_3, price_3, model_4, price_4, model_5, price_5, model_6, price_6, model_7, price_7, model_8, price_8, model_9, price_9, model_10, price_10, message):
# #     choose_model_1 = f"Ваш выбор пал на модель {model_1}. Это утонченные часы, которые может позволить не каждый человек. Каждый тик в нем - это внимание окружающих. Цена его, в зависимости от комплектации, будет {price_1}"

def show_modal_and_price(message):
    for company, models in models_watch.items():
        for model, price_range in models.items():
            bot.send_message(message.chat.id, f"Выбранная модель часов {company} {model} имеет стоимость в пределах {price_range} в зависимости от комплектации.")