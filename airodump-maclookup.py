#!/usr/bin/env python3
import pandas as pd
import logging
import sys
import os
from manuf import manuf
from pathlib import Path
import os.path
import readline,glob
import time
from colorama import init
from colorama import Fore, Style
init(autoreset=True)

sys.tracebacklimit = 0
class DevNull:
    def write(self, msg):
        pass
sys.stderr = DevNull()

def airodump_csv_parser(CommandClass, CompleterClass, name):
    command = CommandClass(name)
    completer = CompleterClass(command)
    readline.set_completer(completer.complete)
while True:
    if 'libedit' in readline.__doc__:
        readline.parse_and_bind('bind ^I rl_complete')
    else:
        readline.parse_and_bind("tab: complete")
    filename = input('What is the airodump-ng csv file''s name? ')
    if not os.path.isfile(filename):
        print ('[-]' '', filename + " is not an airodump-ng .csv file!!! ")
    if os.path.exists(filename):
        print ('[+]' '  ' "File Exists!!! " + filename)
        colnames = ['Station MAC', 'First time seen', 'Last time seen', 'Power', '# packets', 'BSSID', 'Probed ESSIDs']
        colnames2 = ['BSSID', 'First time seen', 'Last time seen', 'channel', 'Speed', 'Privacy', 'Cipher', 'Authentication', 'Power', '# beacons', '# IV', 'LAN IP', 'ID-length', 'ESSID', 'Key']
        df = pd.read_csv(f'{filename}', names=colnames, skip_blank_lines=True, header=None, skipinitialspace=0, engine='python', dtype=str, skiprows=5, usecols=range(1))
        df2 = pd.read_csv(f'{filename}', names=colnames2, skip_blank_lines=True, header=None, skipinitialspace=0, engine='python', skiprows=2, usecols=range(15),nrows=1)
        df3 = pd.read_csv(f'{filename}', names=colnames2, skip_blank_lines=True, header=None, skipinitialspace=0, engine='python', skiprows=2, usecols=range(6),nrows=1)
        df4 = pd.read_csv(f'{filename}', names=colnames2, skip_blank_lines=True, header=None, skipinitialspace=0, engine='python', skiprows=2, usecols=range(8),nrows=1)
        df5 = pd.read_csv(f'{filename}', names=colnames, skip_blank_lines=True, header=None, skipinitialspace=0, engine='python', dtype=str, skiprows=5, usecols=range(7)).dropna().drop_duplicates("Probed ESSIDs")
        df6 = pd.read_csv(f'{filename}', names=colnames, skiprows=14, usecols=range(7)).dropna().drop_duplicates("Probed ESSIDs")
        # Set to True, to refresh the MAC address DB
        p = manuf.MacParser(update=False)
    for row, series in df2.iterrows():
            print('\n'*0)
            print ("Wireless Network Name:")
            print(Fore.RED + series["ESSID"])
            print('\n'*0)
            for row, series in df3.iterrows():
                print ("Wireless Network Type:")
                print(Fore.RED + series["Privacy"])
                for row, series in df4.iterrows():
                    print('\n'*0)
                    print ("Wireless Network Authentication in use:")
                    print(Fore.RED + series["Authentication"])
                    print('\n'*0)
                    print("Clients on network and corresponding MAC Addresses:")
                    print('\n'*0)     
                    for row, series in df.iterrows():
                        print(p.get_manuf_long(series["Station MAC"]), "Client MAC =",Fore.RED + (series["Station MAC"]))    
    for row, series in df5.iterrows():
        print('\n'*0)
        print("Client ESSID Probes:")
        print(Fore.RED + series["Probed ESSIDs"])
    