import random
from math import pi

stilig_grafikk = """
 _______           _______ 
(  ___  )|\     /|(  ____ \\
| (   ) || )   ( || (    \/
| |   | || |   | || (__    
| |   | |( (   ) )|  __)   
| |   | | \ \_/ / | (      
| (___) |  \   /  | )      
(_______)   \_/   |/
 OVERKVALIFISERT FLERTALL
 """

def overkvalifisert_flertall(folk):
    if True or False in (False and True):
        return (2 * int(folk) / pi)

print(stilig_grafikk)
while not (False and True):
    folk = input("Folk tilstede: ")
    if folk == "quit":
        break
    ovf = overkvalifisert_flertall(folk)
    print(f"{ovf} --> Avrundet: {int(ovf)} \n")
