Tinker Tank Meetup V : Python and Pi
==================
## Summary

TODO :: Summarize


Prerequisites
------------------
1. x86_64 based Computer (Any laptop should do -- This is were we will run our IDE)
2. Raspberry Pi with Ethernet (Wifi is optional to complete this session)
3. SDCARD pre-loaded with Rasbian Jessie ([Download](https://www.raspberrypi.org/downloads/raspbian/))
4. CAT-5 Ethernet Cable ( USB Ethernet Dongle may be needed for newer Macs)
5. Optional, but highly recommended:
    1. Solderless Breadboard
    2. Male to Female Jumper Wires
    3. 270Ω Resistor
    4. Single LEDs

### Setting up Python on Windows Development Machines
Follow [this](http://docs.python-guide.org/en/latest/starting/install/win/) guide to install python on Windows machines.


### Setting up PyCharm IDE

1. Download & Install PyCharm Communitiy Edition for your OS ([Download](https://www.jetbrains.com/pycharm/download/))


### Create P2P Network for Local Development
[Source](https://pihw.wordpress.com/guides/direct-network-connection/)

1. Ensure the Raspberry Pi is powered off, and remove the SD-Card.
2. Insert the SD-Card into a card reader and plug it into your laptop.
3. Find the drive and you should find several files on the Card (note it a lot smaller than you’d expect since it is only the boot section of the Card (the rest is hidden)).
4. Make a copy of cmdline.txt and rename it cmdline.normal
5. Edit cmdline.txt and add the IP address at the end (be sure you don’t add any extra lines).
6. Return the card to the Raspberry Pi.   Attach the network cable attached to both the computer and Raspberry Pi and power up.

For network settings where the IP address is obtained automatically (DHCP), use an address in the range 169.254.X.X (169.254.0.0 – 169.254.255.255):

    ip=169.254.0.2

**Ensure you take note of this IP address** (you will need it every time you want to directly connect to the Raspberry Pi).

**NOTE THE FOLLOWING:**

+ You will need to wait for your computer to finish detecting the network settings (you may see a small networking icon flashing in your system tray while it does, or open up the network settings to see when it has finished and has an IP address) – it can take around 1/2 minute.  Your computer may report the connection as  “limited or no connection” when connected to the Raspberry Pi in this way, this is normal as indicates it is a direct computer to computer connection rather than a standard network.

+ If you forget or decide not to plug in the network cable, the Raspberry Pi will wait 2 minutes (or until you connect the cable) before completing it’s start-up (so if you only have a keyboard and monitor attached, you need to wait!).
