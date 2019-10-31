"""
Program: 
Author: Jared Stormer
Start Date: 1-21-2018
"""
       




Wtr = 0
Eth = 0
Terra = 0
Blkh = 0
Amm = 0

'''
print ("Instructions:")
print ("Find your journal files C:-Users-PCUsername-Saved Games-Frontier Developments-Elite Dangerous.")
print ("Copy a file from a date you explored to the folder the program is in.")
print ("Copy the journal file name, by clicking rename and CTRL+C. Make sure the file name has not been changed!")
print ("Paste the file name into the command line with the .log extension at the end.")
print ("Press enter, and your finds will be revealed!")
print ("There should be a new file in the folder you put the program into.  Discoveries_Journal.xxxxxxx.xx")
'''
#inp =input("Enter file name:  ")



with open("Journal.181102002755.01.log", "r") as f:
#f = open("Journal.181102002755.01.log", "r")
    


#f =open("Journal.log", "r")

    
    for line in f:
        splt=line.split()
   
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

        time.sleep( 5 )
    
f.close()
    



    






                

      
      








              
