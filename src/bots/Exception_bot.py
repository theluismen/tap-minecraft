from bots.Bot import Bot

class ExceptionBot( Bot ):
    def __init__ ( self ):
        super().__init__()

    def run ( self ):
        self.mc.postToChat("Nombre de bot desconocido.")
        self.mc.postToChat("Use:")
        self.mc.postToChat("/bot infobot:")
        self.mc.postToChat("para ver los bots disponibles")

    def test_msg ( self ):
        return "ExceptionBot: Done"
