# Airodump-maclookup

A Python 3 tool that parses airodump-ng csv files, and finds the client’s (Station's) vendor or company name by checking it's MAC addresss ranges.

## Simplicity

It's a basic python3 script that requires the *aircrack-ng* suite to be installed. After installing the *aircrack-ng suite*, and capturing the wireless traffic ; use this python3 script to output useful data, including the client's MAC addresses and client probes.

# Installation

    $ git clone https://github.com/W00t3k/airodump-maclookup
    $ cd airodump-maclookup
    $ pip3 install -r requirements.txt
  
 ## Usage
 
    $ airodump-ng wlan1mon --bssid  00:00:00:00:00:00 -c 6 --output-format csv -w filename
    $ python3 airodump-maclookup.py
