from .base_agent import BaseAgent

class InsultBot ( BaseAgent ):
    def __init__ ( self ):
        super().__init__()

    def run ( self ):
        self.mc.postToChat("Marica");

    def print_message ():
        print("Te insulté")
