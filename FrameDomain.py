#!/usr/bin/env python3
#
import os

def main():
  print("""

 ███████████                                    ██████████                                  ███          
░░███░░░░░░█                                   ░░███░░░░███                                ░░░           
\033[1;39m ░███   █ ████████ ██████ █████████████   ██████░███   ░░███ ██████ █████████████   ██████ ████████████  
 ░███████░░███░░██░░░░░██░░███░░███░░███ ███░░██░███    ░██████░░██░░███░░███░░███ ░░░░░██░░██░░███░░███ 
 ░███░░░█ ░███ ░░░ ███████░███ ░███ ░███░███████░███    ░██░███ ░███░███ ░███ ░███  ███████░███░███ ░███ 
 ░███  ░  ░███    ███░░███░███ ░███ ░███░███░░░ ░███    ███░███ ░███░███ ░███ ░███ ███░░███░███░███ ░███ 
 █████    █████  ░░████████████░███ ████░░████████████████ ░░██████ █████░███ ████░░███████████████ █████
\033[1;36m░░░░░    ░░░░░    ░░░░░░░░░░░░ ░░░ ░░░░░ ░░░░░░░░░░░░░░░░   ░░░░░░ ░░░░░ ░░░ ░░░░░ ░░░░░░░░░░░░░░░ ░░░░░ 
                                                                                     \033[1;39m AngelSecurityTeam                                   
""")

def banner():
	    
	print ("""
\033[1;36m[\033[1;39m1\033[1;36m]\033[1;39m Subextractor
\033[1;36m[\033[1;39m2\033[1;36m]\033[1;39m SubDomainExt
\033[1;36m[\033[1;39m3\033[1;36m]\033[1;39m Cert
\033[1;36m[\033[1;39m4\033[1;36m]\033[1;39m BufferOver
\033[1;36m[\033[1;39m5\033[1;36m]\033[1;39m Threat
\033[1;36m[\033[1;39m7\033[1;36m]\033[1;39m Shodan
\033[1;36m[\033[1;39m8\033[1;36m]\033[1;39m Entrust
\033[1;36m[\033[1;39m9\033[1;36m]\033[1;39m SubForceDomain
\033[1;36m[\033[1;39m10\033[1;36m]\033[1;39m DnsDumpester    
""")

def opt_ini():
	
    opt=input("\033[1;39mOption : \033[1;39m")
    
    
    if(opt == '1'):
	    opt1=input("\n\033[1;39mDomain : \033[1;39m")
	    os.system("python3 1.py "+opt1)
	    print(" ")
	    
    if(opt == '2'):
	    os.system("python3 2.py ")
	    print(" ")
	    
    if(opt == '3'):
	    opt3=input("\n\033[1;39mDomain : \033[1;39m")
	    print("")
	    os.system("bash 2.sh -cert "+opt3)
	    print(" ")
	   
    if(opt == '4'):
	    opt4=input("\n\033[1;39mDomain : \033[1;39m")
	    print("")
	    os.system("bash 3.sh -cert "+opt4)
	    print(" ")
	 
    if(opt == '5'):
	    opt5=input("\n\033[1;39mDomain : \033[1;39m")
	    print("")
	    os.system("bash 4.sh -cert "+opt5)
	    print(" ")
	    
    if(opt == '6'):
	    os.system("python3 5.py ")
	    print(" ")
	    
    if(opt == '7'):
	    os.system("python3 6.py ")
	    print(" ")
	    	    		    		    
    if(opt == '8'):
	    opt8=input("\n\033[1;39mDomain : \033[1;39m")
	    print("")
	    os.system("python3 7.py -d "+opt8)
	    print(" ")
	        	    
    if(opt == '9'):
	    opt9=input("\n\033[1;39mDomain : \033[1;39m")
	    print("")
	    os.system("python3 8.py "+opt9+" wordlist.txt")
	    print(" ")
	    	    	    
    if(opt == '10'):
	    os.system("python3 9.py")
	    print(" ")
    else:
        exit()	   

if __name__ == '__main__':
 main()
banner()
opt_ini()
