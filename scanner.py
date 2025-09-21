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
    for index,octa in enumerate(ip):
        if '-' in octa:
            first,last = octa.split('-')
            for new_octa in range(int(first),int(last)+1):
                target = ip[:index] + [str(new_octa)] + ip[index+1:]
                ip_list.append('.'.join(target))
        elif ',' in octa:
            for new_octa in octa.split(','):
                target = ip[:index] + [str(new_octa)] + ip[index+1:]
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
