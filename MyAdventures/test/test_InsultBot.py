import os

from support_files  import lines_of_file
from support_server import start_server, stop_server
from src.agents.Insult_bot import InsultBot

# TEST 1: Con el servidor APAGADO, que NO se conecte
def test_InsultBot_1():
    bot = InsultBot()
    assert bot.connected() == False

# TEST 2: Encendemos el servidor y verificamos que se ha conectado
def test_InsultBot_2():
    connected = False
    server, server_on = start_server()
    if server_on:
        bot = InsultBot()
        connected = bot.connected()
        stop_server( server )

    assert connected == True

# TEST 3: Con el servidor APAGADO, ver si carga los insultos
def test_InsultBot_3():
    bot = InsultBot()
    filename = os.path.join(os.path.dirname(__file__), '../data/insults.txt')
    assert len( bot.insults ) in ( 3, lines_of_file(filename))
