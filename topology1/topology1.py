
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
        s1 = self.addSwitch('s1',dpid='100')
        #tenant1
        a1 = self.addHost('a1', mac="00:00:00:00:00:01", ip="10.1.1.1/24")
        a2 = self.addHost('a2', mac="00:00:00:00:00:02", ip="10.1.1.2/24")
        a3 = self.addHost('a3', mac="00:00:00:00:00:03", ip="10.1.1.3/24")
        self.addLink(a1, s1)
        self.addLink(a2, s1)
        self.addLink(a3, s1)

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
