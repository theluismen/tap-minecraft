from .base_agent import BaseAgent

class ExceptionBot( BaseAgent ):
    def __init__ ( self ):
        super().__init__()

    def run ( self ):
        self.mc.postToChat("Nombre de bot desconocido.")
        self.mc.postToChat("Use:")
        self.mc.postToChat("/bot infobot:")
        self.mc.postToChat("para ver los bots disponibles")

    def test_msg ( self ):
        return "ExceptionBot: Done"
