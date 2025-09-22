A simple Python script that organizes and parallelizes Nmap scans for my OSCP and OSEP journey.

example
```console
kali@kali:~$ sudo scanner.py 192.168.1.28-30,35 
```
<img width="1187" height="373" alt="image" src="https://github.com/user-attachments/assets/61acd1dd-f760-4c6e-a9d1-3b0c2f87a569" />

the scanner understand '-' as being a range operator and ',' as additional host.

it will create a folder for each host and name it after its last octal.

<img width="319" height="480" alt="image" src="https://github.com/user-attachments/assets/404e7720-495f-4a13-810f-7042bc568e0e" />


it will start a thread for each tcp and udp scan for each target at once and save the output inside of its host folder.

hopefully this will be one less step that will be operator error in your OSCP journey.


scanning options used for both UDP and TCP scans:

&emsp;-Pn  = disables ping for host is up(incase a box has icmp responses diabled)

&emsp;-n   = diable name resolution of the target host (helps speed up)

&emsp;-sV  = version scanning, tries to find the version the service is running

&emsp;-sC  = script scanning, will run default set of nmap scripts to 

&emsp;-oN  = save the output in the nmap format(aka the output that you see on the terminal)


TCP scan options:

&emsp;-p-  = scan all ports

&emsp;-sT  = full tcp scan (im peranoid that -sS syn scan can brick or hang some vulnerable services)

UDP scan options:

&emsp;default 1000 ports

&emsp;-sU  = UDP scan



  
