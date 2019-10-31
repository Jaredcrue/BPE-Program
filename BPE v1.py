"""
Program: 
Author: Jared Stormer
Start Date: 1-21-2018
"""
       


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

print ("Instructions:")
print ("Find your journal files C:-Users-PCUsername-Saved Games-Frontier Developments-Elite Dangerous.")
print ("Copy a file from a date you explored to the folder the program is in.")
print ("Copy the journal file name, by clicking rename and CTRL+C. Make sure the file name has not been changed!")
print ("Paste the file name into the command line with the .log extension at the end.")
print ("Press enter, and your finds will be revealed!")
print ("There should be a new file in the folder you put the program into.  Discoveries_Journal.xxxxxxx.xx")

inp =input("Enter file name:  ")
f = open(inp, "r")
'''
w= open("Discoveries_" + inp ,"w+")
'''
#f =open("Journal.log", "r")

import time

#Potenial way to monitor files
#Journal.190802202521.01.log Test file

while 1:
    where = f.tell()
    line = f.readline()
    if not line:
        time.sleep(1)
        f.seek(where)
    else:
        #print (line) # already has newline
        splt=line.split()
        print(splt)

'''
for line in f:
    splt=line.split()
'''   
    #print(line)
    #print(splt)
  
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

#Print in New File
'''
print ("------------------------------",file=w)
print ("Found:  ",file=w)
print (Eth, "Earth-Likes!",file=w)
print (Wtr, "Water Worlds!",file=w)
print (Terra, "Terraformable Worlds! (Excluding Water and Earthlikes)",file=w)
print (Blkh, "Black Holes!",file=w)
print (Amm, "Ammonia Worlds!",file=w)

PlanetNum =Eth + Wtr + Terra + Blkh +Amm
print (PlanetNum, "POI Bodies Found!!",file=w)

print ("Happy Exploring!",file=w)
print ("Date of py Scan: " , datetime.datetime.now(),file=w)
print ("------------------------------",file=w)

print ("If in Shell, restart program for another scan. Press F5")
c = input ("Press any key to exit.")
'''



'''{ "timestamp":"2018-01-21T01:24:03Z", "event":"Scan", "BodyName":"Eoch Pruae PS-U f2-3038 A",
"DistanceFromArrivalLS":0.000000, "StarType":"H", "StellarMass":2.992188, "Radius":8826.874023,
"AbsoluteMagnitude":20.000000, "Age_MY":8264, "SurfaceTemperature":0.000000, "Luminosity":"VII",
"SemiMajorAxis":15598797824.000000, "Eccentricity":0.053803, "OrbitalInclination":-35.729397, "Periapsis":46.054371,
"OrbitalPeriod":5227565.000000, "RotationPeriod":0.082461, "AxialTilt":0.000000 }
{ "timestamp":"2018-01-21T01:24:14Z", "event":"Music", "MusicTrack":"Supercruise" }'''



'''
    #print(w,l)
    tg=int(w)+int(l)
    wp=int(w)/int(tg)
    wp = "{0:.2f}".format(wp)
    a=("Team: " ,name, "| Total Games: " ,tg, "| Wins: ",w,"| losses: ",l, "| win %: " ,float(wp)*100)
   
    print("Team: " ,name, "| Total Games: " ,tg)
    print ("Wins: ",w,"| losses: ",l, "| win %: " ,float(wp)*100)
    print()
    if float(wp) > .50:
        
        top.write(str(a))
        
       
        print ("^ write to top.txt ^")
    else:
        bottom.write(str(a))
        
       
        print("^ write to bottom.txt ^")
# Exit the program
'''
f.close()
w.close()





                

      
      








              
