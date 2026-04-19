#!/usr/bin/env python3
from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
import os

def create_topology():
    net = Mininet(controller=RemoteController, switch=OVSKernelSwitch, link=TCLink)
    info('*** Adding Controller\n')
    net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6653)
    
    info('*** Adding Switch and Hosts\n')
    s1 = net.addSwitch('s1', protocols='OpenFlow13')
    h1 = net.addHost('h1', ip='10.0.0.1/24', mac='00:00:00:00:00:01')
    h2 = net.addHost('h2', ip='10.0.0.2/24', mac='00:00:00:00:00:02')
    h3 = net.addHost('h3', ip='10.0.0.3/24', mac='00:00:00:00:00:03')
    h4 = net.addHost('h4', ip='10.0.0.4/24', mac='00:00:00:00:00:04')

    info('*** Creating Links\n')
    for h in [h1, h2, h3, h4]: net.addLink(h, s1)

    info('*** Starting Network\n')
    net.start()
    os.system('ovs-vsctl set bridge s1 protocols=OpenFlow13')
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_topology()
