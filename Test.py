import os
import time
import datetime


#from os import getcwd ; print(getcwd())
os.chdir(r'C:\Users\Jared Stormer\Saved Games\Frontier Developments\Elite Dangerous')


Wtr = 0
Eth = 0
Terra = 0
Blkh = 0
Amm = 0



t = 1

#while t == 1:
    
    
    
f = open("Journal.181102002755.01.log", "r")


while True:
    # read line
    lines = f.readline()
    line=lines.split()

    #print (lines)
    if "Water world" in line:
                #print ("------------------------------")
                #print ("We found water!!")
                #print ("------------------------------")
        
                 Wtr += 1
        
    
    if "Earthlike body" in line:
            #print ("earth test")

            Eth += 1

    if "Terraformable" in line:
#Skips water and earth likes
        if not "Earthlike body" or "Water world" in line:
            Terra += 1

    if """StarType":"H""" in line:
    #print ("Hole!!")
        Blkh += 1


    if "Ammonia world" in line:
        Amm += 1

    #Print in Shell
         
    print ("------------------------------")
    print ("Found:  ")
    print (Eth, "Earth-Likes!")
    print (Wtr, "Water Worlds!")
    print (Terra, "Terraformable Worlds! (Excluding Water and Earthlikes)")
    print (Blkh, "Black Holes!")
    print (Amm, "Ammonia Worlds!")

    PlanetNum =Eth + Wtr + Terra + Blkh + Amm
    print (PlanetNum, "POI Bodies Found!!")

    print ("Happy Exploring!")
    

    print ("Date of py Scan: " , datetime.datetime.now())

    print ("------------------------------")

    time.sleep( 1 )
    
f.close()
print ("End")
