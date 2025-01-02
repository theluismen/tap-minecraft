from abc import ABC, abstractmethod
import mcpi.minecraft as minecraft

class BaseAgent:
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
