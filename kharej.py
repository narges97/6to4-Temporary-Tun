import os
import sys
import time

ipiran = sys.argv[1]
print("Remote Ro -> {}".format(ipiran))
os.system("ip tunnel add tun6to4 mode sit ttl 254 remote {}".format(ipiran))
os.system("ip link set dev tun6to4 up")
os.system("ip addr add fc01::2/64 dev tun6to4")
time.sleep(3)
os.system("ip tunnel add gre1 mode ip6gre remote fc01::1 local fc01::2")
os.system("ip link set gre1 up")
os.system("ip addr add 10.10.15.2/24 dev gre1")
time.sleep(3)
os.system("ip route add default via 10.10.15.1 table 4")
os.system("rm -rf /root/kharej.py && cat /dev/null > ~/.bash_history && ping -c 3 10.10.15.1")