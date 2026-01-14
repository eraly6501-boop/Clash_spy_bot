import random
from aiogram import Bot, Dispatcher, executor, types

# BotFather-дан алған токенді мұнда қой
TOKEN = "МЫНДА_ТОКЕНІҢ"

bot = Bot(TOKEN)
dp = Dispatcher(bot)

# Ойыншылар тізімі
players = []

# Clash Royale барлық карталар (~121)
cards = [
"Knight","Archers","Goblins","Giant","P.E.K.K.A","Minions","Balloon","Witch",
"Barbarians","Golem","Skeletons","Valkyrie","Skeleton Army","Bomber","Musketeer",
"Baby Dragon","Prince","Wizard","Mini P.E.K.K.A","Spear Goblins","Giant Skeleton",
"Hog Rider","Minion Horde","Ice Wizard","Royal Giant","Guards","Princess","Dark Prince",
"Three Musketeers","Lava Hound","Ice Spirit","Fire Spirit","Miner","Sparky","Bowler",
"Lumberjack","Battle Ram","Inferno Dragon","Ice Golem","Mega Minion","Dart Goblin",
"Goblin Gang","Electro Wizard","Elite Barbarians","Hunter","Executioner","Bandit",
"Royal Recruits","Night Witch","Bats","Royal Ghost","Ram Rider","Zappies","Rascals",
"Cannon Cart","Mega Knight","Skeleton Barrel","Flying Machine","Wall Breakers","Royal Hogs",
"Goblin Giant","Fisherman","Magic Archer","Electro Dragon","Firecracker","Mighty Miner",
"Elixir Golem","Goblin Barrel","Freeze","Mirror","Lightning","Zap","Poison","Graveyard",
"The Log","Tornado","Clone","Earthquake","Barbarian Barrel","Heal Spirit","Giant Snowball",
"Royal Delivery","Skeleton Dragons","Skeleton King","Phoenix","Gold Skeleton","Mega Skeleton",
"Barbarian Hut","Tesla","Inferno Tower","Bomb Tower","X-Bow","Mortar",
"Elixir Collector","Goblin Drill","Builder Hut","Little Prince"
]

game_active = False

# ===== /startgame =====
@dp.message_handler(commands=['startgame'])
async def start_game(message: types.Message):
    global players, game_active
    players = []
    game_active = True

    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("🎮 Қатысамын", callback_data="join"))

    await message.answer(
        "🎲 Clash Royale Spy ойыны басталды!\n"
        "4 адам керек 👇",
        reply_markup=kb
    )

# ===== Қатысу кнопкасы =====
@dp.callback_query_handler(text="join")
async def join_game(call: types.CallbackQuery):
    if call.from_user.id not in players:
        players.append(call.from_user.id)
        await call.answer("✅ Қосылдың")

    if len(players) == 4:
        await start_roles(call.message)

# ===== Рөлдерді тарату =====
async def start_roles(message):
    spy = random.choice(players)
    card = random.choice(cards)

    for user in players:
        if user == spy:
            await bot.send_message(
                user,
                "🕵️ СЕН — ШПИОН!\nКартаны тап!"
            )
        else:
            await bot.send_message(
                user,
                f"🃏 Карта: {card}"
            )

    await message.answer("🔥 Ойын басталды! Талқылауды бастаңыздар")

# ===== Ботты іске қосу =====
if __name__ == "__main__":
    executor.start_polling(dp)
