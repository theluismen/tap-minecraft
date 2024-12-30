from server_support import start_server, stop_server
from src.agents.base_agent import BaseAgent

# TEST 1: Con el servidor APAGADO, que NO se conecte
def test_BaseAgent_1():
    bot = BaseAgent()
    assert bot.connected() == False

# TEST 2: Encendemos el servidor y verificamos que se ha conectado
def test_BaseAgent_2():
    connected = False
    server, server_on = start_server()
    if server_on:
        bot = BaseAgent()
        connected = bot.connected()
        stop_server( server )

    assert connected == True
