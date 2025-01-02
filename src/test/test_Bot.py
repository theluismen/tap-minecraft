from bots.Bot import Bot

from .support_server import start_server, stop_server

# TEST 1: Con el servidor APAGADO, que NO se conecte
def test_Bot_1():
    bot = Bot()
    assert bot.connected() == False

# TEST 2: Encendemos el servidor y verificamos que se ha conectado
def test_Bot_2():
    connected = False
    server, server_on = start_server()
    if server_on:
        bot = Bot()
        connected = bot.connected()
        stop_server( server )

    assert connected == True
