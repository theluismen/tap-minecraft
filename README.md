# TAP: Práctica "Minecraft Agent Framework" 
[![codecov](https://codecov.io/github/theluismen/tap-minecraft/graph/badge.svg?token=KD9B9TK3N0)](https://codecov.io/github/theluismen/tap-minecraft)

## framework.py
Nuestro framework se gestiona unicamente desde un solo archivo: [`./src/framework.py`](src/framework.py). Este es el archivo que se ejecuta para utilizar todos los bots que interactúan con el servidor de Minecraft. Las invocaciones válidas para este archivo son las siguientes:
```python3
python3 ./src/framework.py <bot>
python3 ./src/framework.py pptbot piedra | papel | tijera
```
> [!CAUTION]
> Si no se proporciona un bot como argumento o una de las opciones de *`pptbot`* no se corresponde con piedra, papel, o tijera, `framework.py` no hara nada.

La estructura de framework.py es la siguiente:
```python3
def main ():

    if len(sys.argv) == 1:
        return

    bot_type = sys.argv[1]

    if bot_type.lower()   == 'insultbot':
        bot = InsultBot()
    elif bot_type.lower() == 'tntbot':
        bot = TNTBot()
    elif bot_type.lower() == 'infobot':
        bot = InfoBot()
    elif bot_type.lower() == 'pptbot':
        choice = ""
        if len(sys.argv) == 3:
            choice   = sys.argv[2]
        bot = PPTBot(choice)
    else:
        bot = ExceptionBot() # Mensaje de error AL SERVIDOR

    if bot.connected():
        bot.run()
        print( bot.test_msg() )

if __name__ == "__main__":
    main()
```

## Plugin de Java
Para el uso del `framework.py` desde el chat o linea de comandos del servidor de Minecraft, hemos hecho un plugin de Java que detecta cuando se escribe en el chat `/bot` e invoca el archivo `./src/framework.py`. Todo lo referente a este componente de nuestro proyecto se encuentra en el directorio `./java/` y constan 3 archivos; el codigo fuente del plugin `ChatListener.java`, la información del plugin `plugin.yml` y el archivo `.jar` `spigot-1.12.jar`.

La parte importante de [`./java/ChatListener.java`](java/ChatListener.java) es esta función, que intercepta los comandos e invoca el `framework.py`.
```java
@Override
public boolean onCommand(CommandSender sender, Command command, String label, String[] args) {
    String framework;
    if ( ! command.getName().equalsIgnoreCase("bot") )
        return false;

    if ( args.length == 0 ) {
        sender.sendMessage("Uso incorrecto:");
        return false;
    }

    try {
        framework = "python3 ../src/framework.py " + args[0];
        if ( args.length == 2 )
            framework += " " + args[1];
        Runtime.getRuntime().exec(framework);
    } catch ( IOException e ) {
        sender.sendMessage("Hubo error");
    }

    return true;
}
```

## Instalación del Plugin de Java
Para instalar este plugin en la carpeta `./Server/plugins/` se ha creado un breve script de Bash llamado [`MakeJavaPlugin.sh`](MakeJavaPlugin.sh). Este se encarga de compilar el codigo fuente del plugin, empaquetarlo todo en un archivo `.jar` y luego mover este archivo a la carpeta `./Server/plugins/`. Ejecutamos el script con:
```bash
./MakeJavaPlugin.sh
```

## Referencias
- https://www.stuffaboutcode.com/p/minecraft-api-reference.html
