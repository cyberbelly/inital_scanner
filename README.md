A simple Python script that organizes and parallelizes Nmap scans for my OSCP and OSEP journey.

example
```console
kali@kali:~$ sudo scanner.py 192.168.1.28-30,35 
```
the scanner understand '-' as being a range operator and ',' as additional host.

it will create a folder for each host and name it after its last octal.

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



  
