# TAP: Práctica "Minecraft Agent Framework"
[![codecov](https://codecov.io/github/theluismen/tap-minecraft/graph/badge.svg?token=KD9B9TK3N0)](https://codecov.io/github/theluismen/tap-minecraft)

## Resumen
Este proyecto se centra en la creación de un framework para el desarrollo de bots en Minecraft utilizando Python, junto con un plugin de Java para facilitar su integración con el servidor del juego.

A través de este trabajo, se han diseñado bots que interactúan con el mundo de Minecraft para realizar tareas automatizadas. 

Para conseguirlo, se ha utilizando la herramienta **mcpi** para establecer la conexión con el servidor e interactuar con él.

## Bots
Para la creación de bots se ha creado una clase abstracta padre con métodos que deben implementar las clases hijas.
```python3
class Bot:
    def __init__ ( self ):
        try:
            self.mc = minecraft.Minecraft.create()
        except ConnectionRefusedError:
            print("ERROR: Conection refused")

    def connected( self ):
        return hasattr(self,"mc")

    @abstractmethod
    def run ( self ):
        pass

    @abstractmethod
    def test_msg ( self ):
        pass
```
El constructor de la clase sirve para establecer una conexión con el servidor, el método `run` se utiliza en la ejecución de los bots y los metodos connected y `test_msg` se utilizan para los tests.

A partir de esta clase se han creado 5 bots con diferentes funcionalidades:
- **`InfoBot`**: Muestra informacion de los bots existentes.
- **`InsultBot`**: Muestra por pantalla un insulto aleatorio de un fichero.
- **`TNTBot`**: Coloca un circulo de bloques de tnt i fuego en la posición del jugador.
- **`PPTBbot`**: Juega una partida de piedra papel tijera contigo.
- **`ExceptionBot`**: Bot usado en caso de no indicar el nombre de un bot correctamente. Indica que el bot introducido es incorrecto y pide que se use infobot para ver los bots disponibles.

## framework.py
Nuestro framework se gestiona unicamente desde un solo archivo: [`./src/framework.py`](src/framework.py). Este es el archivo que se ejecuta para utilizar todos los bots que interactúan con el servidor de Minecraft. Las invocaciones válidas para este archivo son las siguientes:
```bash
python3 ./src/framework.py <bot>
python3 ./src/framework.py pptbot piedra | papel | tijera
```
> [!CAUTION]
> Si no se proporciona un bot como argumento o una de las opciones de **`pptbot`** no se corresponde con piedra, papel, o tijera, `framework.py` no hara nada.

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

## Instalación de dependecias
Para instalar las dependencias del proyecto:
```bash
pip install -r requirements.txt
```

## Arrancar el Servidor de Minecraft
Una vez ya esta todo configurado, encender el servidor de Minecraft es tan fácil como ejecutar el siguiente script:
```bash
./StartServer.sh
```

## Referencias
- [Enunciado de la Práctica](data/Minecraft%20Agent%20Framework.pdf)
- https://github.com/AdventuresInMinecraft/AdventuresInMinecraft-Linux
- https://www.stuffaboutcode.com/p/minecraft-api-reference.html
