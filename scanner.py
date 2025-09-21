import subprocess
import os
import sys
import threading

tcp_scan_template = 'nmap -p- -Pn -n -A -sTVC -oN {} {}'
udp_scan_template = 'nmap -Pn -n -sUVC -oN {} {}'
raw_ips = sys.argv[1::]

def nmap_scan(command):
    print(command)
    subprocess.run(command.split(' '))

ip_list = []
for ip in raw_ips:
    ip = ip.split('.')
    for index,octals in enumerate(ip):
        if '-' not in octals or ',' not in octals:
            pass
        else:
            octals = octals.split(',')
            for octal in octals:
                if '-' in octal:
                    first, last = octal.split('-')
                    for new_octal in range(int(first),int(last)+1):
                        target = ip[:index] + [str(new_octal)] + ip[index+1:]
                        ip_list.append('.'.join(target))
                else: 
                    target = ip[:index] + [str(octa)] + ip[index+1:]
                    ip_list.append('.'.join(target))

print('scanning against the following IPs: ', *ip_list )

target_list = []
for ip in ip_list:
    last_octa = ip.split('.')[-1]
    if last_octa not in os.listdir():
        os.mkdir(last_octa)
    tcp_scan = tcp_scan_template.format(f'{last_octa}/tcp_scan.txt',ip)
    udp_scan = udp_scan_template.format(f'{last_octa}/udp_scan.txt',ip)
    target_list.append(tcp_scan)
    target_list.append(udp_scan)



threads = []
for target in target_list:
    thread = threading.Thread(target=nmap_scan, args=(target,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
