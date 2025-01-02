import time

from    MyAdventures.mcpi.connection import RequestError
import  MyAdventures.mcpi.block as Block
from    bots.Bot import Bot

class TNTBot ( Bot ):
    def __init__ ( self ):
        super().__init__()
        self.coords = [ # Un circulo de tnts
            (-2,-2),(-1,-2),(0,-2),(1,-2),(2,-2),
            (-2,-1),(2,-1),
            (-2,0),(0,0),(2,0),
            (-2,1),(2,1),
            (-2,2),(-1,2),(0,2),(1,2),(2,2)
        ]

    def tnt( self ):
        try:
            pos     = self.mc.player.getTilePos()
            x, y, z = pos.x, pos.y, pos.z

            for coord in self.coords:
                self.mc.setBlock(x+coord[0], y+7, z+coord[1], Block.TNT.id)
                self.mc.setBlock(x+coord[0], y+8, z+coord[1], Block.FIRE.id)

        except RequestError:
            pass

    def run ( self ):
        self.mc.postToChat("Cargando tnt... Corre !")
        time.sleep(1)
        self.tnt()

    def test_msg ( self ):
        return "TNTBot: Done"
