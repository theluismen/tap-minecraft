import os
import time
import platform
import subprocess
# Encender Servidor:
#  returns True si se encendió; False si no
def start_server():
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

# Apagar el servidor
def stop_server( server ):
    system = platform.system().lower()
    if system == 'windows':
        os.system("TASKKILL /IM java.exe /F")
    elif system == 'linux':
        os.system("kill -9 {server.pid}")
