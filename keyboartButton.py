from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton,InlineKeyboardMarkup

from pyrogram import emoji
btn_knb = KeyboardButton(f"{emoji.PLAY_BUTTON} камень,ножницы,бумага")
btn_info = KeyboardButton(f"{emoji.INFORMATION} Инфо")
btn_games = KeyboardButton(f"{emoji.VIDEO_GAME} Игры")
btn_profile = KeyboardButton(f"{emoji.PERSON} Профиль")
btn_time = KeyboardButton(f"{emoji.TIMER_CLOCK} Время")
btn_quest = KeyboardButton(f"{emoji.SUNSET} квест")
btn_back = KeyboardButton(f"{emoji.BACK_ARROW} назад")
btn_scissors = KeyboardButton(f"{emoji.SCISSORS} Ножницы")
btn_rock = KeyboardButton(f"{emoji.ROCK} Камень")
btn_paper = KeyboardButton(f"{emoji.NEWSPAPER} Бумага")
btn_back_game = KeyboardButton(f"{emoji.BACK_ARROW} нaзад")
btn_right = InlineKeyboardButton(f"{emoji.DOOR}{emoji.RIGHT_ARROW} Права",callback_data="start_right")
btn_left = InlineKeyboardButton(f"{emoji.LEFT_LUGGAGE}{emoji.DOOR} Влево",callback_data="start_left")
btn_image = KeyboardButton(f"{emoji.FRAMED_PICTURE}Сгенирировать изоброжения")
btn_coin = KeyboardButton(f"{emoji.COIN}Узнай сколько у тебя монет")
btn_add_coin = KeyboardButton(f"{emoji.PLUS}{emoji.COIN} одна монетаь")
btn_numbers = KeyboardButton(f"{emoji.INPUT_NUMBERS}Угадай число")

kb_main = ReplyKeyboardMarkup(
    keyboard=[
        [btn_info,btn_games,btn_profile,btn_time,btn_image]
    ],
    resize_keyboard=True
)

kb_games = ReplyKeyboardMarkup(
    keyboard=[
        [btn_knb,btn_coin,btn_numbers],
        [btn_quest,btn_back],
        [btn_add_coin]
    ],
    resize_keyboard=True
)

kb_RSP = ReplyKeyboardMarkup(
    keyboard=[
        [btn_paper,btn_rock,btn_scissors],
        [btn_back_game]
    ],
    resize_keyboard=True
)

inline_kb_start_quest = InlineKeyboardMarkup([
    [InlineKeyboardButton("Пройти квест",
                          callback_data="start_quest")]

    ],

)

inline_kb_left_right = InlineKeyboardMarkup([
    [btn_left],
    [btn_right],


],

)

inline_kb_raft_swim = InlineKeyboardMarkup([
    [InlineKeyboardButton(f"{emoji.MAN_SWIMMING}Проплыть",
                          callback_data="start_swim")],
    [InlineKeyboardButton(f"{emoji.SHIP}Проплыть на плоту",
                          callback_data="start_raft")],

],

)

inline_kb_sword_flute = InlineKeyboardMarkup([
    [InlineKeyboardButton(f"{emoji.SNAKE}Убить всех",
                          callback_data="start_sword")],
    [InlineKeyboardButton(f"{emoji.MUSICAL_KEYBOARD}Сыграть на флейте что-бы все уснкли",
                          callback_data="start_flute")],

],

)


