from .base_agent import BaseAgent

class InfoBot( BaseAgent ):
    def __init__ ( self ):
        super().__init__()

    def run ( self ):
        self.mc.postToChat("## Bot de Informacion - Nombre de Bots ##")
        self.mc.postToChat("- insultbot     para Insult Bot")
        self.mc.postToChat("- tntbot        para TNT Bot")
        self.mc.postToChat("- infobot       para Info Bot")

    def print_message ( self ):
        pass