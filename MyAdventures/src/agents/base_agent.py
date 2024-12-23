from abc import ABC, abstractmethod
import mcpi.minecraft as minecraft

class BaseAgent:
    def __init__ ( self ):
        self.mc = minecraft.Minecraft.create()

    @abstractmethod
    def run ( self ):
        pass

    @abstractmethod
    def print_message ( self ):
        pass
