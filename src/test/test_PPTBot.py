from bots.PPT_bot import PPTBot
from .support_server import start_server, stop_server


# TEST 1: Comprabacion del estado del bot
def test_PPTBot_1():
    bot = PPTBot()
    bot.human_choice = "piedra"
    bot.bot_choice = "tijera"
    estado = bot.get_state()
    assert estado["human_choice"] == "piedra"
    assert estado["bot_choice"] == "tijera"

# TEST 2: Caso de partida donde gane el bot, que gane el bot
def test_PPTBot_2():
    bot = PPTBot()
    bot.human_choice = "piedra"
    bot.bot_choice = "tijera"
    resultado = bot.determine_winner()
    assert resultado == "humano"

# TEST 3: Caso de partida donde haya empate, que haya empate
def test_PPTBot_3():
    bot = PPTBot()
    bot.human_choice = "papel"
    bot.bot_choice = "papel"
    resultado = bot.determine_winner()
    assert resultado == "empate"

# TEST 4: Caso de partida donde gane el bot, que gane el bot
def test_PPTBot_4():
    bot = PPTBot()
    bot.human_choice = "tijera"
    bot.bot_choice = "piedra"
    resultado = bot.determine_winner()
    assert resultado == "bot"
