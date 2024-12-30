from support_server import start_server, stop_server
from src.agents.Info_bot import InfoBot

# TEST 1: Con el servidor APAGADO, que NO se conecte
def test_InfoBot_1():
    bot = InfoBot()
    assert bot.connected() == False

# TEST 2: Encendemos el servidor y verificamos que se ha conectado
def test_InfoBot_2():
    connected = False
    server, server_on = start_server()
    if server_on:
        bot = InfoBot()
        connected = bot.connected()
        stop_server( server )

    assert connected == True
