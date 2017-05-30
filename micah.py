from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()


#mc.setBlock(x,y,z, block_id)

            
#y = y + 3

#for i in 0 to 3:

def micah_house( x, y, z ):
    block_id = 5#wood
    mc.setBlock(x,y,z,block_id)
    mc.setBlock(x,y+1,z,block_id)
    mc.setBlock(x,y+2,z,block_id)
    mc.setBlock(x,y+3,z,block_id)


    mc.setBlock(x+1,y,z,block_id)
    mc.setBlock(x+1,y+1,z,block_id)
    mc.setBlock(x+1,y+2,z,block_id)
    mc.setBlock(x+1,y+3,z,block_id)

    mc.setBlock(x+2,y,z,block_id)
    mc.setBlock(x+2,y+1,z,block_id)
    mc.setBlock(x+2,y+2,z,block_id)
    mc.setBlock(x+2,y+3,z,block_id)

    mc.setBlock(x+2,y,z-1,block_id)
    mc.setBlock(x+2,y+1,z-1,block_id)
    mc.setBlock(x+2,y+2,z-1,block_id)
    mc.setBlock(x+2,y+3,z-1,block_id)


    mc.setBlock(x+2,y,z-2,block_id)
    mc.setBlock(x+2,y+1,z-2,block_id)
    mc.setBlock(x+2,y+2,z-2,block_id)
    mc.setBlock(x+2,y+3,z-2,block_id)

    mc.setBlock(x+2,y,z-3,block_id)
    mc.setBlock(x+2,y+1,z-3,block_id)
    mc.setBlock(x+2,y+2,z-3,block_id)
    mc.setBlock(x+2,y+3,z-3,block_id)



    mc.setBlock(x+1,y,z-3,block_id)
    mc.setBlock(x+1,y+1,z-3,block_id)
    mc.setBlock(x+1,y+2,z-3,block_id)
    mc.setBlock(x+1,y+3,z-3,block_id)


    mc.setBlock(x,y,z-3,block_id)
    mc.setBlock(x,y+1,z-3,block_id)
    mc.setBlock(x,y+2,z-3,block_id)
    mc.setBlock(x,y+3,z-3,block_id)

    block_id = 64#door

    mc.setBlock(x,y,z-2,block_id,0)
    mc.setBlock(x,y+1,z-2,block_id,8)
    time.sleep(1)
    mc.setBlock(x,y,z-1,block_id,0)
    mc.setBlock(x,y+1,z-1,block_id,8)
    block_id = 5#wood
    mc.setBlock(x-1,y+2,z-1,block_id)
    mc.setBlock(x-1,y+2,z-2,block_id)

    mc.setBlock(x,y+3,z-1,block_id)
    mc.setBlock(x,y+3,z-2,block_id)

    mc.setBlock(x+1,y+4,z-1,block_id)
    mc.setBlock(x+1,y+4,z-2,block_id)
    block_id = 26#bed


    mc.setBlock(x+1,y,z-2,block_id,0)
    mc.setBlock(x+1,y,z-1,block_id,8)



pos = mc.player.getTilePos()
    
x =pos.x
y =pos.y 
z =pos.z 

micah_house(x,y,z)

x =pos.x
y =pos.y
z =pos.z + 4   
micah_house(x,y,z)
x =pos.x
y =pos.y
z =pos.z + 8  
micah_house(x,y,z)
x =pos.x
y =pos.y
z =pos.z + 12  
micah_house(x,y,z)
x =pos.x
y =pos.y
z =pos.z + 16  
micah_house(x,y,z)

