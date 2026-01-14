from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import random

TOKEN = "МЫНДА_ТОКЕНІҢ"  # BotFather-ден алған токенді қой

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

cards = ["Archer", "Giant", "Knight", "Wizard", "P.E.K.K.A", "Hog Rider", "Miner", "Valkyrie"]  # Барлық карталарды қосуға болады
players = []

@dp.message_handler(commands=['startgame'])
async def start_game(message: types.Message):
    global players
    players = []
    keyboard = InlineKeyboardMarkup()
    for i in range(4):
        keyboard.add(InlineKeyboardButton(f"🎮 Қатысамын ({i+1}/4)", callback_data=f"join_{i}"))
    await message.reply("Ойынға қатысамын дегендерді басыңдар:", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data.startswith('join_'))
async def join_game(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    if user_id not in players:
        players.append(user_id)
    await callback_query.answer(f"Сіз қосылдыңыз! ({len(players)}/4)")
    if len(players) == 4:
        await start_round(callback_query.message)

async def start_round(message):
    spy = random.choice(players)
    card = random.choice(cards)
    for p in players:
        if p == spy:
            await bot.send_message(p, f"Сіз шпионсыз! Картаны білесіз: {card}")
        else:
            await bot.send_message(p, f"Сіздің картаңыз: {card}")
    await message.reply("Ойын басталды! Шпионды тап!")

if __name__ == '__main__':
    executor.start_polling(dp)
