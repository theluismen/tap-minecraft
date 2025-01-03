# TAP: Práctica "Minecraft Agent Framework" 
[![codecov](https://codecov.io/github/theluismen/tap-minecraft/graph/badge.svg?token=KD9B9TK3N0)](https://codecov.io/github/theluismen/tap-minecraft)

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
