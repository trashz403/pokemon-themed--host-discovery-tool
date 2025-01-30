from termcolor import colored
import pygame
import time
import nmap
from tqdm import tqdm
import itertools
import sys
import random
import pyttsx3

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Initialize pygame mixer
pygame.mixer.init()

# Load and play the music
music_file = "jigglypuff.mp3"
try:
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
except pygame.error:
    print(colored(f"Error: No file '{music_file}' found in working directory.", "red"))
    exit(1)

# Define ANSI color codes
PINK = '\033[95m'
BLUE = '\033[94m'
WHITE = '\033[97m'
RESET = '\033[0m'

# ASCII Art with color formatting
ascii_banner = f"""{PINK}
                                         ./%%%/.                                      
                                     /(((((#(((((((##.                          ##%((%.                                                               
                                   .%((((((((%(((((((((%,                     .####(%((%                                                              
                                   ##((((((((((((%&((((((##                   &(####%(((*                                                             
                                   %#((((((((((((((((((#%(((#                /#####%#((((                                                             
                                   %###(((((((((((((%   .&((((#(           ((##(%((((#(                                                              
                                   #####(((((((((((. #&&&,,%((((#(        %#%#/.   .     .(/                                                        
                                     @##(###(((((((#   &&&&&&( %(((((%*,*/&.                .  .(                                                     
                                     #&%##(########*   @&&&&&&&# *,                               #                                                   
                                   %###(#%########&.  ,@&&&&&&&&&#../   ,                       .  .,                                                {BLUE}
                                *###############%,%   .&&#.   .   .      **,,.   .                   /  .(@&.*                                        
                                &###(#####(##(%,. (.   ,                     ...(@&,                 (&&&&&#,.                                        
                                (############*.  .      .                    ,/,,,,,(.               %&&&&%..                                         
                                 %#########%,                              ..(,,,,,/(,,.  .      ..,(&&&&&*.                                          
                                  ,%######&*                    .,,      ..  (,,,,,*,,,,,,,,,,,,,,,&, (@@#                                            
                                    .#,    ,(/            /&&@@@@@&@&&#((.. . ,#*,,,,,,,,,,,,,,,(*     %#                                             {WHITE}
                                      %        .        %&&@&&&&&&&@,     ,,     ./&/*,,,,*/%*.    . .  *                                             
                                       /               *%&&&&&&&&&&&&,/%@#  *     .      .       .     .%                                             
                                       /(    .         ,##%&#%##( .* *%#%*  *             .*&&&&&* #.  ./.                                            
                                       /,*   .         * &%%#%@&&@&%#%#&.   *            .@@&&@@    #.  *.                                            
                                       (,,,.           ,* .%%##%###%%#     ,,          . %&####/     /  *.                                            
                                       /,,,, .          .(                %..           .&###%%&%#%  *  #                                             
                                       (,,,,,              *(.        ,%.   ..&.        .&&%%* #*%  .*  *                                             
                                        #,,,,,.                .     .     (*/&&,        *%####%#   *  (                                              
                                        ,*,,,,,,.                         /,,,#&&&&   .  .% *,    , . *.(                                             
                                         *,,,,,,,,                       ..(*(%,   . .    .(    */   .(  /                                            
                                          .(,,,,,,,,.                    .                   ..     *, */.                                            
                                            (,,,,,,,,,,        .                                 .,&,                                                {PINK}
                                            ./%*,,,,,,,,,,.                                 .,,,,(.                                                   
                                          */,,,,*&*,,,,,,,,,,,,,                    ...,,,,,,,*/                                                      
                                        **,.,,,,,,,##*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*#,                                                         
                                      ./     .,,,/.    *#*,,,,,,,,,,,,,,,,,,,,,,,,*,,((*                                                              
                                     ...      ,(.            .%@(/,,,,,,,,,*/%&*                                                                      
                                     (.      (.                      ,,,,,,,,,#                                                                       
                                      %/*%/.                          #,,,,,,,,(                                                                      
                                                                       #,,,....*.                                                                     
                                                                        /.      *                                                                     
                                                                          &.    /                                                                     
                                                                            //./,{RESET} """

print(ascii_banner)

# Wait for the music to finish before exiting
time.sleep(10)  # Adjust based on music length

# User Input
target = input(colored("Enter target IP or range (e.g., 192.168.1.0/24): ", "cyan"))
print(colored("Select scan type:", "yellow"))
print(colored("1. TCP SYN Scan", "green"))
print(colored("2. TCP ACK Ping", "green"))
print(colored("3. UDP Scan", "green"))
print(colored("4. ICMP Address Mask Request", "green"))
print(colored("5. ICMP Timestamp Request", "green"))
print(colored("6. ICMP Echo Request", "green"))
print(colored("7. Indepth Scan", "green"))
choice = str(input(colored("Enter choice (1-7): ", "cyan")))

results = [
    "✨ A Wild Host Appeared! ✨",
    "⚡ Jigglypuff used Scan! It’s Super Effective! ⚡",
    "🛑 No Hosts Found... Jigglypuff Fell Asleep! 💤"
]

def print_result(host, state):
    print(colored(random.choice(results), "green"))
    engine.say("Scan complete! Jigglypuff found a wild host!")
    engine.runAndWait()

def icmp_echo_request(target):
    print(colored(f"Scanning {target} with ICMP Echo Request...", "blue"))
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-PE -n -sn')
    for host in nm.all_hosts():
        print_result(host, nm[host].state())

def icmp_timestamp_request(target):
    print(colored(f"Scanning {target} with ICMP Timestamp Request...", "blue"))
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-PP -n -sn')
    for host in nm.all_hosts():
        print_result(host, nm[host].state())

def icmp_address_mask_request(target):
    print(colored(f"Scanning {target} with ICMP Address Mask Request...", "blue"))
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-PM -n -sn')
    for host in nm.all_hosts():
        print_result(host, nm[host].state())

def tcp_syn_scan(target):
    print(colored(f"Scanning the specified target {target} with TCP SYN Scan...", "blue"))
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-PS -n -sn')
    for host in nm.all_hosts():
        print_result(host, nm[host].state())

def tcp_ack_ping(target):
    print(colored(f"Scanning the specified target {target} with TCP ACK Ping...", "blue"))
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-PA -n -sn')
    for host in nm.all_hosts():
        print_result(host, nm[host].state())

def udp_scan(target):
    print(colored(f"Scanning the specified target {target} with UDP Scan...", "blue"))
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-PU -n -sn')
    for host in nm.all_hosts():
        print_result(host, nm[host].state())

def indepth_scan(target):
    print(colored(f"Scanning the specified target {target} with Indepth Scan...", "blue"))
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-PE -PP -PM -PS -PA -PU -n -sn')
    for host in nm.all_hosts():
        print_result(host, nm[host].state())

# Running the selected scan
if choice == '1':
    tcp_syn_scan(target)
elif choice == '2':
    tcp_ack_ping(target)
elif choice == '3':
    udp_scan(target)
elif choice == '4':
    icmp_address_mask_request(target)
elif choice == '5':
    icmp_timestamp_request(target)
elif choice == '6':
    icmp_echo_request(target)
elif choice == '7':
    indepth_scan(target)
else:
    print(colored("Invalid choice", "red"))
    def type_out(text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        print()

    type_out("Jigglypuff is singing... scanning network... 🎤")
    if random.choice([True, False]):
        print("🔥 ERROR: Jigglypuff got angry and shut down your PC! 😱")
    else:
        print("✅ Scan completed successfully!")
