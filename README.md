# ARP_Spoofer
> This security tool is an APR_Spoofer, well I guess it is more like a malware tool to conduct man-in-the-middle attacks.
> I'm using the `scapy module` that python provides. Scapy is a program that allows the user to send, sniff and dissect and forge network packets. The capability of scapy allows me to construct various tools that can probe, scan, or attack. It's a powerful interactive packet manipulation module.

- Use your home network as your target network and virtual machine as your host network.

<br />
<br />

# Getting Started
Super easy to get started with this program Things you need to do first:
- You'll need to OS to play around with this tool. Because this is a Man in the middle maalware tool. This allows you to take over your vitims network sessions. So I recommend downloading (`VMware` <a href='https://customerconnect.vmware.com/en/downloads/details?downloadGroup=WKST-PLAYER-1623-NEW&productId=1039&rPId=85399'> VMware download</a>) or (`VirtualBox` <a href='https://www.virtualbox.org/wiki/Downloads'>VirtualBox Download</a>)
- Download linux
- Once once your virtual machines have been set up start up your linux environment.
- In your Linus envirnment you'll want to download a IDE Editior like `visual studio code` or `Pycharm`
- Next you can either fork this script and in your terminal you the following command: `git clone https://github.com/Dlray89/arp_spoofer.git`. This will upload the `Py File`

## Things you need:
- You need both the `target IP` and `Mac address` along with the `IP of your router`. You also need to make sure your virtual environment is on the same network as your host environment

- if you dont know those felt free to visit my network scanning tool. This will tell you all IP address on the network along with the Mac Address asscoaited with it. You can find this project at <a href='https://github.com/Dlray89/Network_Scanner'>Network Scanner</a>. I explain how to use this tool inthat repo.


## Starting the tool
- Go to the target machine and retrieve your arp table before excuting this program. To do that  open your `terminal` or `windows cmd` and type `arp -a`. 
- Gnce you pulled up your arp table on the targeted machine. All you need to do to start up this tool once you have all the requirement information, just type in your terminal `python arp_spoofer.py`
- Go back to the targets ARP Table and see if the router mac address changed to your host machine which should be your kali machine.
