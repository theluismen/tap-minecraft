import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.AsyncPlayerChatEvent;
import org.bukkit.plugin.java.JavaPlugin;

import java.io.FileWriter;
import java.io.IOException;

public class ChatLogger extends JavaPlugin implements Listener {

    @Override
    public void onEnable() {
        getServer().getPluginManager().registerEvents(this, this);
    }

    @EventHandler
    public void onPlayerChat(AsyncPlayerChatEvent event) {
        // String message = event.getPlayer().getName() + ": " + event.getMessage();
        // try (FileWriter writer = new FileWriter("chatlog.txt", true)) {
        //     writer.write(message + "\n");
        // } catch (IOException e) {
        //     e.printStackTrace();
        // } /create TNTBot
        System.cmd("python3 framework.py " + event.getMessage() );
    }
}
