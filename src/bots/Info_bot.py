from bots.Bot import Bot

class InfoBot( Bot ):
    def __init__ ( self ):
        super().__init__()

    def run ( self ):
        self.mc.postToChat("## Bot de Informacion - Nombre de Bots ##")
        self.mc.postToChat("- insultbot     para Insult Bot")
        self.mc.postToChat("- tntbot        para TNT Bot")
        self.mc.postToChat("- infobot       para Info Bot")
        self.mc.postToChat("- pptbot piedra | papel | tijera  para PPT Bot")

    def test_msg ( self ):
        return "InfoBot: Done"
