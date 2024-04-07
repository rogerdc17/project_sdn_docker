
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController
from time import sleep
from mininet.link import Intf

CONTROLLER_IP = "127.0.0.1"

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self):
        s1 = self.addSwitch('s1',dpid='200')
        #tenant1
        a4 = self.addHost('a4', mac="00:00:00:00:00:04", ip="10.1.1.4/24")
        a5 = self.addHost('a5', mac="00:00:00:00:00:05", ip="10.1.1.5/24")
        a6 = self.addHost('a6', mac="00:00:00:00:00:06", ip="10.1.1.6/24")
        self.addLink(a4, s1)
        self.addLink(a5, s1)
        self.addLink(a6, s1)

if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()
    #change the controller IP here
    c1 = RemoteController('c1', ip=CONTROLLER_IP)
    net = Mininet(topo=topo, controller=c1)
    net.start()
    sleep(5)
    net.pingAll()
    CLI(net)
    net.stop()



'''
sudo ovs-vsctl add-port s1 vxlan1 -- set interface vxlan1 type=vxlan options:remote_ip=192.168.122.149
'''
