import subprocess
import os
import time

from support_server import start_server, stop_server

# Funcion que ejecuta el framework
def run_framework ( bot = "" ):
    fm_path = os.path.join( os.path.dirname(__file__), '../src/framework.py')
    fm_cmd  = ["python3", fm_path]

    if bot != "":
        fm_cmd.append( bot )

    fm = subprocess.Popen(
        fm_cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, text=True
    )
    return fm

# TEST 1: Con el servidor APAGADO, y SIN BOT especificado
#  no debe devolver nada
def test_framework_1():
    framework = run_framework()
    stdout, stderr = framework.communicate()
    assert stdout.strip() == ""

# TEST 2: Con el servidor APAGADO, y con Bot INCORRECTO...
#  ... intentaria conectar al servidor y daria error de conexión
def test_framework_2():
    framework = run_framework("asas")
    stdout, stderr = framework.communicate()
    assert stdout.strip() == "ERROR: Conection refused"

# TEST 3: Con el servidor APAGADO, y con Bot CORRECTO...
#  ... intentaria conectar al servidor y daria error de conexión
def test_framework_3():
    framework = run_framework("insultbot")
    stdout, stderr = framework.communicate()
    assert stdout.strip() == "ERROR: Conection refused"

# TEST 4: Con el servidor APAGADO, y con Bot CORRECTO...
#  ... intentaria conectar al servidor y daria error de conexión
def test_framework_4():
    framework = run_framework("tntbot")
    stdout, stderr = framework.communicate()
    assert stdout.strip() == "ERROR: Conection refused"

# TEST 5: Con el servidor APAGADO, y con Bot CORRECTO...
#  ... intentaria conectar al servidor y daria error de conexión
def test_framework_5():
    framework = run_framework("infobot")
    stdout, stderr = framework.communicate()
    assert stdout.strip() == "ERROR: Conection refused"

# TEST 6: Con el servidor ENCENDIDO, y SIN BOT especificado
#  no debe devolver nada
def test_framework_6():
    server, server_on = start_server()
    stdout, stderr = "",""
    if server_on:
        framework = run_framework()
        stdout, stderr = framework.communicate()
        stop_server( server )
        assert stdout.strip() == ""

# TEST 7: Con el servidor ENCENDIDO, y con Bot INCORRECTO...
#  ... intentaria conectar al servidor, se conectaria, ...
#  ... se ejecutaria y daria mensaje satisfactorio
def test_framework_7():
    server, server_on = start_server()
    stdout, stderr = "",""
    if server_on:
        framework = run_framework("FDSDFSD")
        stdout, stderr = framework.communicate()
        stop_server( server )
        assert stdout.strip() == "ExceptionBot: Done"

# TEST 8: Con el servidor ENCENDIDO, y con Bot CORRECTO...
#  ... intentaria conectar al servidor, se conectaria, ...
#  ... se ejecutaria y daria mensaje satisfactorio
def test_framework_8():
    server, server_on = start_server()
    stdout, stderr = "",""
    if server_on:
        framework = run_framework("insultbot")
        stdout, stderr = framework.communicate()
        stop_server( server )
    assert stdout.strip() == "InsultBot: Done"

# TEST 9: Con el servidor ENCENDIDO, y con Bot CORRECTO...
#  ... intentaria conectar al servidor, se conectaria, ...
#  ... se ejecutaria y daria mensaje satisfactorio
def test_framework_9():
    server, server_on = start_server()
    stdout, stderr = "",""
    if server_on:
        framework = run_framework("tntbot")
        stdout, stderr = framework.communicate()
        stop_server( server )
    assert stdout.strip() == "TNTBot: Done"

# TEST 10: Con el servidor ENCENDIDO, y con Bot CORRECTO...
#  ... intentaria conectar al servidor, se conectaria, ...
#  ... se ejecutaria y daria mensaje satisfactorio
def test_framework_10():
    server, server_on = start_server()
    stdout, stderr = "",""
    if server_on:
        framework = run_framework("infobot")
        stdout, stderr = framework.communicate()
        stop_server( server )
    assert stdout.strip() == "InfoBot: Done"