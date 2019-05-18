#!usr/lib/python3

import math

#initialization of important variables
crit=0
crit_per =0
baseCrit=25

stats = int(input("Enter the amount of CRT stat on your char"),10)
baseCrit += math.floor(stats/3.4)


gears= int(input("enter the amount of flat crit by gears"),10)
crit += gears

gears_per = int(input("enter the amount of crit% by gears"),10)
crit_per += gears_per

avatar = int(input("enter the amount of flat crit by avatar"),10)
crit += avatar

avatar_per = int(input("enter the amount of crit% by avatar"),10)
crit_per += avatar

critUp = input("Do you use crit-up skill?")
if(critUp == 'Yes' or critUp == 'yes'):
	critUpLevel = int(input("Enter the level of crit-up skill that you use"),10)
	critUpBonus= math.floor(critUpLevel/2)
	crit += critUpBonus


misc = int(input("Enter any miscellaneous flat crit that wasn't covered in the previous options,including food buff"),10)
crit += misc

misc_per = int(input("Enter any miscellaneous crit% that wasn't covered in the previous options"),10)
crit_per += misc_per

totalCrit= math.floor(baseCrit * (100+crit_per)/100) +crit

print("Your crit rate is :",totalCrit)
