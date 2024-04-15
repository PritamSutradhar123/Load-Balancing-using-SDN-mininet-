#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.node import OVSKernelSwitch
from mininet.node import Host
from mininet.cli import CLI
from mininet.log import setLogLevel, info, error

def myNetwork():

    net = Mininet(topo=None,
                  build=False,
                  ipBase='10.0.0.0/8')

    info('*** Adding controller\n')
    c0 = net.addController(name='c0',
                           controller=RemoteController,
                           ip='127.0.0.1',
                           protocol='tcp',
                           port=6634)  # Changed port to 6634

    info('*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, controller=c0)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, controller=c0)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch, controller=c0)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch, controller=c0)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch, controller=c0)

    info('*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, mac="00:00:00:00:00:01")
    h2 = net.addHost('h2', cls=Host, mac="00:00:00:00:00:02")

    info('*** Add links\n')
    net.addLink(h1, s1)
    net.addLink(s1, s2)
    net.addLink(s1, s3)
    net.addLink(s1, s4)
    net.addLink(s5, h2)
    net.addLink(s5, s2)
    net.addLink(s5, s3)
    net.addLink(s5, s4)

    info('*** Starting network\n')
    net.build()

    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()
        if not controller.isListening(ip=controller.ip, port=controller.port):
            error("Controller is not listening!")

    info('*** Starting switches\n')
    for switch in net.switches:
        switch.start([c0])

    info('*** Post configure switches and hosts\n')
    
    h1.cmd("ifconfig h1-eth0 0")
    h1.cmd("ifconfig h1-eth0 10.0.0.1/24")
    h1.cmd("arp -s 10.0.0.2 00:00:00:00:00:02")

    h2.cmd("ifconfig h2-eth0 0")
    h2.cmd("ifconfig h2-eth0 10.0.0.2/24")
    h2.cmd("arp -s 10.0.0.1 00:00:00:00:00:01")

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
