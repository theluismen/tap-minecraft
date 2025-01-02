from .base_agent import BaseAgent
import mcpi.block as Block
import time
class TNTBot ( BaseAgent ):
    def __init__ ( self ):
        super().__init__()

    def perform_action(self):
        pos = mc.player.getTilePos()
        x, y, z = pos.x, pos.y, pos.z

        # for i in range(3):
        #     for j in range(3):
        #         mc.setBlock(pos.x+i, pos.y+7, pos.z+i, block.TNT.id)
        #         mc.setBlock(pos.x+j, pos.y+8, pos.z+j, block.FIRE.id)
        print(x,y,z)
    def run ( self ):

        self.perform_action()
        self.mc.postToChat("Cargando tnt....")
        self.mc.postToChat(pos.x)
        sleep(2)

        self.mc.postToChat("Cargando tnt....")

    def print_message ():
        print("ya esploté")
