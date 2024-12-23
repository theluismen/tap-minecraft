import mcpi.minecraft as minecraft
import sys

mc = minecraft.Minecraft.create("localhost", 4711)
mc.postToChat( sys.argv[1:] )
