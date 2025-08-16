import json
from pyrogram import Client, filters
from FB import generate
from pyrogram.types import ForceReply
import config
import random
import datetime
import keyboartButton
import base64
bot = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    name="Life helper"
)
def button_filters(button):
    async def func(_,bot,message):
        return message.text == button.text
    return filters.create(func,"ButtonFilter", button=button)

@bot.on_callback_query()
async def handle_query(bot,query):
    await query.message.delete()
    if query.data == "start_quest":
        await query.message.reply_text("ТЫ стоишь перед двумя двкрьми,"
                                       "Какую из них выберешь?",
        reply_markup=keyboartButton.inline_kb_left_right)
    elif query.data == "start_right":
        await bot.answer_callback_query(
            query.id,
            text="Добро пожаловать в линию квеста с змеями",
            show_alert=True
        )
        await query.message.reply_text("Ты в комнате полна змеями,"
                                       "Твой действия?",
        reply_markup=keyboartButton.inline_kb_sword_flute )
    elif query.data == "start_left":
        await bot.answer_callback_query(
            query.id,
            text="Добро пожаловать в линию квеста с пираниями",
            show_alert=True
        )
        await query.message.reply_text("Ты в комнате полна пираней,"
                                       "Твой действия?",
        reply_markup=keyboartButton.inline_kb_raft_swim)
    elif query.data == "start_sword":
        await bot.answer_callback_query(
            query.id,
            text="Ты взял меч и убил всех змей,"
            "Ты молодец, ты прошол игру",
            show_alert=True
        )
    elif query.data == "start_flute":
        await bot.answer_callback_query(
            query.id,
            text="Ты спомощью музыки усыпил змей,но ты наступил на одну,"
                                    "Ты умер и проеграл",
            show_alert=True
        )
    elif query.data == "start_raft":
        await bot.answer_callback_query(
            query.id,
            text="Ты переплыл басейнс пираниями и выжыл,"
                                    "Ты молодец, ты прошол игру",
            show_alert=True
        )
    elif query.data == "start_swim":
        await bot.answer_callback_query(
            query.id,
            text="Ты умер"
                    "Ты умер и проеграл",
            show_alert=True
        )
life = 5
num = random.randint(0, 100)
player1 = ("Угодай число")
query_text = ("Введите запрос для генирации"
              "Запрос,Стиль")
@bot.on_message(filters.command("image1") | button_filters(keyboartButton.btn_image))
async  def image1(bot,message):
    await message.reply_text(query_text,
                             reply_markup=ForceReply(True))

@bot.on_message(filters.command("numbers1") | button_filters(keyboartButton.btn_numbers))
async  def numbers1(bot,message):
    global num,life
    life = 5
    num = random.randint(0, 100)
    await message.reply_text(player1,
                             reply_markup=ForceReply(True))


@bot.on_message(filters.reply)
async  def reply(bot,message):
    global life
    numbers = random.randint(0, 1000)
    if message.reply_to_message.text == query_text:
        query,style = message.text.split(",")
        await message.reply_text(f"Генерируется запрос '{query}' подождите немного ...")
        images = await generate(query,style.strip())
        if images:
            image_data = base64.b64decode(images[0])
            with open(f"images/image{numbers}.jpg", "wb") as file:
                file.write(image_data)
            await bot.send_photo(message.chat.id, f"images/image{numbers}.jpg",
                                     reply_to_message_id=message.id)
        else:
            await message.reply_text("Возникла ошибка, попробуйте снова",
                                         reply_to_massege_id=message.id)
    elif message.reply_to_message.text == player1:
        player = int(message.text)
        if life == 0:
            await message.reply("У вас нет жызней")

        elif player > num:
            await message.reply("Слишком большое число")
            life -= 1
            print(life)
            await message.reply_text(player1,
                                         reply_markup=ForceReply(True))
        elif player < num:
            await message.reply("Слишком маленикое число")
            life -= 1
            print(life)
            await message.reply_text(player1,
                                     reply_markup=ForceReply(True))
        else:
            await message.reply("ВЫ выграли ")
            await message.reply("У вас жызней", life)
            await message.reply("Вам было добавлино 10 очков к болансу")
            with open("coins.json", "r") as f:
                users = json.load(f)
                if users[str(message.from_user.id)] <= 10:
                    with open("coins.json", "r") as f:
                        users = json.load(f)
                    users[str(message.from_user.id)] += 10
                    with open("coins.json", "w") as f:
                        json.dump(users, f)






@bot.on_message(filters.command("quest") | button_filters(keyboartButton.btn_quest))
async  def kvest(bot,message):
    await message.reply_text("Хотите ли вы от правится в увликательное путешествия"
                        "полное приключений и загадок?",
                        reply_markup=keyboartButton.inline_kb_start_quest)

@bot.on_message(filters.command("coin") | button_filters(keyboartButton.btn_coin))
async def coin(bot,message):
    with open("coins.json", "r") as f:
        users = json.load(f)
        await message.reply(f"{users}")

@bot.on_message(filters.command("add_coin") | button_filters(keyboartButton.btn_add_coin))
async def add_coin(bot,message):
    with open("coins.json", "r") as f:
        users = json.load(f)

    with open("coins.json", "r") as f:
        users = json.load(f)
        if users[str(message.from_user.id)] <= 10:
            with open("coins.json", "r") as f:
                users = json.load(f)
            users[str(message.from_user.id)] += 1
            with open("coins.json", "w") as f:
                json.dump(users, f)
            await message.reply(f"Плюс одна монета к вашиму акаунту.Ваш баланс {users}")
        else:
            await message.reply("У вас уже эсть нужное кольчество монет")

@bot.on_message(filters.command("RSP") | button_filters(keyboartButton.btn_knb))
async def RSP(bot,message):
    with open("coins.json", "r") as f:
        users = json.load(f)
        if users[str(message.from_user.id)] >= 10:
            await message.reply("Твой ход", reply_markup=keyboartButton.kb_RSP)
        else:
            await message.reply(f"НЕ хватрет средств."
                                f"На твоем счету{users[str(message.from_user.id)]}."
                                f"Минимум сумма для игры - 10")



@bot.on_message(button_filters(keyboartButton.btn_rock) | button_filters(keyboartButton.btn_paper) | button_filters(
    keyboartButton.btn_scissors))
async def choice_rps(bot, message):
    rock = keyboartButton.btn_rock.text
    scissors = keyboartButton.btn_scissors.text
    paper = keyboartButton.btn_paper.text
    bot = random.choice([rock, scissors, paper])
    await message.reply("Выбор бота: ")
    await message.reply(bot)
    if message.text == bot:
        await message.reply("Ничья")
    elif (message.text == rock and bot == scissors) or (message.text == scissors and bot == paper) or (
            message.text == paper and bot == rock):
        await message.reply("Победа")
        with open("coins.json", "r") as f:
            users = json.load(f)
        users[str(message.from_user.id)] += 10
        with open("coins.json", "w") as f:
            json.dump(users, f)
    else:
        await message.reply("Пройгрышь")
        with open("coins.json", "r") as f:
            users = json.load(f)
        users[str(message.from_user.id)] -= 10
        with open("coins.json", "w") as f:
            json.dump(users, f)
@bot.on_message(filters.command("back") | button_filters(keyboartButton.btn_back))
async def back(bot,message):
    await message.reply("Это главное меню",reply_markup = keyboartButton.kb_main)



@bot.on_message(filters.command("games") | button_filters(keyboartButton.btn_games) | button_filters(keyboartButton.btn_back_game))
async def games(bot,message):
    await message.reply("Выбери игру: ",reply_markup = keyboartButton.kb_games)

@bot.on_message(filters.command("time") | button_filters(keyboartButton.btn_time))
async def time(bot,message):
    dt = datetime.datetime.now()
    await message.reply(f"время:  {dt.time()}")


@bot.on_message(filters.command("story"))
async def story(bot,message):
    fake = [
        f"Как-то раз в маленикой деревне.Была годалка но она брала годы жызни за годания.Никто ее не верил и один мужык сказал возьми все мой годы.Но напишы на лестке будушее моих родных и дай им когда я умру.Кaк он вышол от гадалке он умер.И все что было на лестке начало сбыаться",
        f"Жыл был мальчик.Как-то раз он пошел в посадку где были быки.И он решыл дать под зад быку.Ну бык его погнал но все было хорошо.И он продолжыл жыть одноногой жызную",
        f"Как-то раз злой дракон украл принцесу и сказал(пиво,дениги мне на стол и отпушу вашу принцесу).Ну принесли ему все и все было хорошо"]
    num = random.randint(0,len(fake) - 1)
    await message.reply(fake[num])



@bot.on_message(filters.command("info") | button_filters(keyboartButton.btn_info))
async def info(bot,message):
    await message.reply("Добро пожаловать в нашого бота."
                        "Этот бот умет базовые команды.Как")
    await message.reply("Эсть команда /start,/info"
                        ""
            "В скором будут добавлины новые функцый")

@bot.on_message(filters.command("start"))
async def start(bot,message):
    await message.reply("Добро пожаловать!",
                        reply_markup=keyboartButton.kb_main)
    await bot.send_photo(message.chat.id,"a85375000415be8ce06be68e0f5766d2.jpg")
    with open("coins.json", "r") as f:
        users = json.load(f)
    if str(message.from_user.id) not in users.keys():
        users[message.from_user.id] = 10
        with open("coins.json", "w") as f:
            json.dump(users, f)


@bot.on_message()
async def echo(bot,message):
    if message.text.lower() == "привет":
        await message.reply("Привет мой друг")
    elif message.text.lower() == "пока":
        await message.reply("Пока")

bot.run()