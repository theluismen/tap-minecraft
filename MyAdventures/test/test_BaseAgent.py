import os
import time
import subprocess
from src.agents.base_agent import BaseAgent

# TEST 1: Con el servidor APAGADO, que NO se conecte
def test_BaseAgent_1():
    bot = BaseAgent()
    assert bot.connected() == False

# TEST 2: Encendemos el servidor y verificamos que se ha conectado
def test_BaseAgent_2():
    connected = False
    server, server_on = server_started()
    if server_on:
        bot = BaseAgent()
        connected = bot.connected()
        # Apagar el servidor
        os.system("TASKKILL /PID {0} /F".format(server.pid))

    assert connected == True

def server_started():
    process = subprocess.Popen(         # Iniciar el servidor de Minecraft
        ['bash', "./StartServer.sh"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, text=True
    )

    server_ready = False
    while True:                         # Leer la salida del servidor
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        # Comprobar si el servidor está listo
        if output and "Done" in output:
            server_ready = True
            break

        time.sleep(0.1)  # Evita consumir demasiado CPU en el ciclo

    return (process, server_ready)
