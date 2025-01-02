import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.bukkit.plugin.java.JavaPlugin;
import java.io.*;

public class ChatListener extends JavaPlugin {

    @Override
    public void onEnable() {
        getLogger().info("CHAT_LISTENER habilitado");
    }

    @Override
    public void onDisable() {
        getLogger().info("CHAT_LISTENER deshabilitado");
    }

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
}
