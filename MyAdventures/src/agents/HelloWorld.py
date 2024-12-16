import mcpi.minecraft as minecraft
import sys

mc = minecraft.Minecraft.create()
mc.postToChat( sys.argv[1:] )

