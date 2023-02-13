import os
from colorama import Fore,Back,Style
from time import sleep
import time
import pyfiglet
from tqdm import tqdm



Clear = "clear"
os.system(Clear)

print(Fore.RED+"")

print("""

.                                                      .
      .n                     .             .                n.
  . .dP                   dP               9b               9b   .
 4  qXb         .        dX                 Xb       .      dXp   t
dX.  9Xb      .dXb     __                     __    dXb.   dXP   .Xb
9XXb._     _.dXXXXb dXXXXbo.               dXXXXb dXXXXb._   _.dXXP
 9XXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXP
   9XXXXXXXXXXXXXXX ~   ~ OOO8b   d8OOO ~   ~ XXXXXXXXXXXXXXXXXP
     9XXXXXP   9XX      *     98v8P      *     XXP   9XXXXXXXP
      ~~~       9X.          .db|db.          .XP       ~~~
                  )b.  .dbo.dP' v  9b.odb.  .dX(
                ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
               dXXXXXXXXXXXP'   .    9XXXXXXXXXXXb
              dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
              9XXb'    XXXXXb.dX|Xb.dXXXXX'    dXXP
                       9XXXXXX(   )XXXXXXP
                       XXXX X. v .X XXXX
                        XP^X' b   d' X^XX
                        X. 9         P )X
                         b          '  d'

                script by CyBeR ArMy HaKhAmAnEsH

            telegram > https://t.me/+No9LkvAfx6YzYzlk

                     instagram > _l_.666._l_

""")







print(Fore.RESET+"")

print(Fore.CYAN+"")

print("[1]->> Metasploit")

print("")

print("[2]->> Sqlmap")

print("")

print("[3]->> Nmap")

print("")

print("[4]->> Nikto")

print("")

print("[5]->> DDOS")

print("")

print("[6]->> hammer")

print("")

print("[7]->> D-TECT")

print("")

print("[8]->> Help ")


print("")

x = input("Enter: =>> ")
print("")
cl = "clear"
os.system(cl)

for char in tqdm(range(100), colour = "RED"):
     time.sleep(0.1)
print(Fore.GREEN+"")
time.sleep(1)
print("[+] The request was entered ...")
print("")
time.sleep(1)
print("[+] The order was confirmed ...")
print("")
time.sleep(1)                                                                    
print("[+] Commands to run other seconds ...")
print("")
time.sleep(1)
print("[+] Installing...")



print(Fore.RESET+"")



if x == 1:
    print("")
    meta = "pkg install wget && wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh"
    os.system(meta)
    Meta = "./metasploit.sh"
    os.system(Meta)
    msfconsole = "msfconsole"
    os.system(msfconsole)

if x == 2:
   print(Fore.CYAN+"")
   sql = "apt update && apt upgrade && pkg install git && pkg install python && pkg install python2 && git clone https://github.com/sqlmapproject/sqlmap.git"
   os.system(sql)
   sqlmap = " chmod +x * && cd sqlmap && python sqlmap.py"
   os.system(sqlmap)

if x == 3:
   print("")
   NMAP = "pkg update && pkg upgrade && apt-get update && apt-get upgrade && pkg install nmap && nmap --help"
   os.system(NMAP)

if x == 4:
   print("")
   nikto = "apt upgrade && apt update && apt install git && apt install perl && git clone https://github.com/sullo/nikto.git "
   os.system(nikto)
   Nikto = "cd nikto/ && cd program/ && chmod +x * && perl nikto.pl -h"
   os.system(Nikto)

if x == 5:
   print("")
   DDOS = "apt update && apt upgrade && pkg install python && pkg install python2 && pkg install git && git clone https://github.com/Err0r-ICA/DDoS"
   os.system(DDOS)
   ddos = "cd DDoS && python2 DDoS"
   os.system(ddos)

if x == 6:
   print("")
   hammer = "pkg update && pkg upgrade && pkg install git && pkg install python && git clone https://github.com/cyweb/hammer"
   os.system(hammer)
   HAMMER = "cd hammer && python hammer.py"
   os.system(HAMMER)

if x == 7:
   print("")
   D = "apt update && apt upgrade && pkg install git && pkg install python2 && git clone https://github.com/HackTeachz/D-TECT"
   os.system(D)
   TECT = "cd D-TECT && chmod 777 * && pip2 install requests && python2 d-tect.py "
   os.system(TECT)
   
if x == 8:
   print(Fore.GREEN+"")
   print("")
   sleep(1)
   print("                                            Install Metasploit                    ")
   print("")
   sleep(1)
   print("If you want to use Metasploit tools, press these commands after installing the tool")
   print("")
   sleep(1)
   print("orders install metasploit =>  chmod +x metasploit.sh")
   print("")
   sleep(1)
   print("orders install metasploit =>  ./metasploit.sh")
   print("")
   sleep(1)
   print("orders install metasploit =>   msfconsole")
   print("")
   print("")
   print("")
   sleep(1)
   print("If you want to use NMAP tools, press these commands after installing the tool")
   print("")
   sleep(1)
   print("                                            Install nmap                         ")
   print("")
   sleep(1)
   print("nmap")
   print("")
   print("")
   print("")
   sleep(1)
   print("If you want to use sqlmap tools, press these commands after installing the tool")
   print("")
   sleep(1)
   print("                                            Install sqlmap                      ")
   print("")
   sleep(1)
   print("orders install sqlmap =>   cd sqlmap")
   sleep(1)
   print("orders install sqlmap =>   chmod +x *")
   sleep(1)
   print("orders install sqlmap =>   python sqlmap.py")
   print("")
   print("")
   print("")
   sleep(1)
   print("If you want to use Nikto tools, press these commands after installing the tool")
   print("")
   sleep(1)
   print("                                             Install Nikto                      ")
   print("")
   sleep(1)
   print("orders install Nikto =>   cd nikto/")
   sleep(1)
   print("orders install Nikto =>   cd program/")
   sleep(1)
   print("orders install Nikto =>   perl nikto.pl -h")
   print("")
   print("")
   print("")
   sleep(1)
   print("If you want to use DDOS tools, press these commands after installing the tool")
   print("")
   sleep(1)
   print("                                               Install DDOS                     ")
   print("")
   sleep(1)
   print("orders install DDOS =>   cd DDoS")
   sleep(1)
   print("orders install DDOS =>  python2 DDoS")
   print("")
   print("")
   print("")
   sleep(1)
   print("If you want to use Hammer tools, press these commands after installing the tool")
   print("")
   sleep(1)
   print("                                              Install Hammer                     ")
   print("")
   sleep(1)
   print("orders install hammer =>   cd hammer")
   sleep(1)
   print("orders install hammer =>   python hammer.py")
   print("")
   print("")                                                                           
   print("")                                                                          
   sleep(1)
   print("If you want to use D-TECT tools, press these commands after installing the tool")
   print("")
   sleep(1)
   print("                                            install  D-TECT                     ")
   print("")
   sleep(1)                                                                 
   print("orders install D-TECT =>   cd D-TECT")
   sleep(1)
   print("orders install D-TECT =>   chmod 777 *")
   sleep(1)
   print("orders install D-TECT =>   python2 d-tect.py")
   print("")