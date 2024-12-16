from mcrcon import MCRcon

RCON_HOST = "127.0.0.1"
RCON_PASSWORD = "yourpassword"

try:
    with MCRcon(RCON_HOST, RCON_PASSWORD) as mcr:
        # Ejecuta un comando para interactuar con el servidor
        logs = mcr.command("list")  # Lista los jugadores conectados
        print("Jugadores conectados:", logs)
except Exception as e:
    print("Error al conectarse al servidor RCON:", e)
