from .base_agent import BaseAgent

class InfoBot( BaseAgent ):
    def __init__ ( self ):
        super().__init__()

    def run ( self ):
        if not( self.connected() ):
            return

        self.mc.postToChat("## Info Bot ##")
        self.mc.postToChat("- insultbot     for Insult Bot")
        self.mc.postToChat("- tntbot        for TNT Bot")
        self.mc.postToChat("- infobot       for Info Bot")

    def print_message ( self ):
        pass
