from abc import ABC, abstractmethod

class BaseAgent:
    def __init__ ( self ):
        pass

    @abstractmethod
    def run ( self ):
        pass

    @abstractmethod
    def print_message ():
        pass
