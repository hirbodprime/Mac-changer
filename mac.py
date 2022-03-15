import subprocess
import time
import optparse
import re
from colorama import *
init(autoreset=True)

def get_args():
    print(Style.BRIGHT + Fore.YELLOW + "[+]MacAddress Changer!\n")
    
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface", help=" change Interface")
    parser.add_option("-m","--macaddress", dest="new_mac", help=" change MacAddress")
    (options , arguments) = parser.parse_args()
    if not options.interface:
        parser.error (Style.BRIGHT + Fore.RED + "[-]Please specify an interface " + 
        Fore.YELLOW + "| use " +Fore.MAGENTA +  "--help " + Fore.YELLOW +  "for more!")
    elif not options.new_mac:
        parser.error(Style.BRIGHT + Fore.RED + "[-]Please specify a MacAddress " + 
        Fore.YELLOW + "| use " +Fore.MAGENTA +  "--help " + Fore.YELLOW +  "for more!")
    return options

def change_mac(interface,new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw" , "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    # print(Fore.YELLOW + "Wait 1 sec....!")
    # time.sleep(1)
    

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    macaddress_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if macaddress_result:
        return macaddress_result.group(0)
    else:
        print("[-]Please check your input use --help for more!")


def check_mac(current_mace,new_mac,current_mac):
    if current_mace == options.new_mac:
        print(Style.BRIGHT + Fore.GREEN +"MacAddress successfully changed from "+ current_mac + " to " + current_mace)
    else:
        print(Style.BRIGHT + Fore.RED + "[-]Could not change MacAddress!")
        print(Style.BRIGHT + Fore.YELLOW + "Current mac is: " + str(current_mac))



options = get_args()
current_mac = get_current_mac(options.interface)
change_mac(options.interface , options.new_mac)
current_mace = get_current_mac(options.interface)
check_mac(current_mace,options.new_mac,current_mac)

