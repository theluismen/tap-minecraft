import os
import random

from bots.Bot import Bot

# Lambda Function to create a random number
random_insult = lambda n, m: random.randint(n,m)

class InsultBot ( Bot ):
    def __init__ ( self ):
        super().__init__()          # Crear Conexion
        self.insults = []
        self.cargar_insultos()

    def cargar_insultos ( self ):
        base_dir  = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, '../../data/insults.txt')
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    self.insults.append( line.strip('\r\n') );
        # Por si no lee el archivo o pasa algo raro
        except Exception as e:
            self.insults = ['Tonto','Feo','Baboso']

    def run ( self ):
        self.mc.postToChat( "Eres un " + self.insults[ random_insult(0, len(self.insults)-1 ) ] )

    def test_msg ( self ):
        return "InsultBot: Done"
