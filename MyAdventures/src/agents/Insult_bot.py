import random
from .base_agent import BaseAgent

# Lambda Function to create a random number
random_insult = lambda n, m: random.randint(n,m)

class InsultBot ( BaseAgent ):
    def __init__ ( self ):
        super().__init__()          # Crear Conexion
        self.insults = [
            'Marica',
            'Gei',
            'Soplanucas'
        ]

    def run ( self ):
        self.mc.postToChat( self.insults[ random_insult(0, len(self.insults)-1 ) ] )

    def print_message ( self ):
        print("Te he insultado jaja")
