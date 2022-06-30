# Please do not mess around with the text file's saved locations - only delete them FULLY
from mcpi.minecraft import Minecraft
import os
open("/home/" + os.getlogin() + "/Desktop/982D9E3EB996F559E633F4D194DEF3761D909F5A3B647D1A851FEAD67C32C9D1.txt", "a")
while 1 == 1:
 question = input("")
 if question == "save":
  question = input("Would you like to save this point (y/n)")
  if question == "y" or question == "Y" or question == "yes":
     question = input("What would you like to call this point?")
     point = ""
     mc = Minecraft.create()
     area = mc.player.getPos()
     try:
       with open("/home/" + os.getlogin() + "/Desktop/982D9E3EB996F559E633F4D194DEF3761D909F5A3B647D1A851FEAD67C32C9D1.txt", "a") as file:
        file.write("\n" + question + " " + str(area).replace("Vec3(", "").replace(")", ""))
        print("Created point at " + str(area) + " with name '" + question + "'")
        question = ""
     except IOError:
       print("Failed To Save Point")
  if question == 'no' or question == 'n'or question == 'N':
    print("location not saved")
 if question == "load":
  new_lst=[]
  try:
   with open("/home/" + os.getlogin() + "/Desktop/982D9E3EB996F559E633F4D194DEF3761D909F5A3B647D1A851FEAD67C32C9D1.txt") as file:
    output = file.read().splitlines()
    res = []
    for ele in output:
     if ele.strip():
        res.append(ele)
    print(str(res))
    question = input("Where Would You Like To Go (Enter NUMBER - 0 is starting index)")
    mc = Minecraft.create()
    wz = res[int(question)]
    wzw = wzw = ''.join(filter(lambda x: (x.isnumeric() or x == '-' or x == '.' or x == ','), wz))
    print("Moved to " + wzw)
    mc.player.setPos(wzw)
    mc.postToChat("Moved To " + wzw)
  except IOError:
    print("Failed To Load Points")
 
