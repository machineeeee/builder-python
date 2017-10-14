import yaml

from ..util import util
from port import Port
from state import State

class Component(object):

    def __init__(self, component_dict=None):
        """ The ``Component`` class represents a device.

        A component stores state individually for each instance and can be
        configured by passing in parameters using a structure that reprsents
        the state.

        Args:
            path (str): path to a model yaml file.
        """

        self.name = None
        self.ports = []

        # Load name from component data file
        if 'name' in component_dict:
            self.name = component_dict['name']

        # Load host flag from component data file
        if 'host' in component_dict:
            self.host = component_dict['host']
        else:
            self.host = False

        # Load ports from component data file
        for port_dict in component_dict['ports']:
            port = Port(self, port_dict)
            self.ports.append(port)

        # self.compute_port_dependencies()


    def get_ports(self):
        # TODO: return list of ports
        # TODO: device.ports
        return self.ports

    @staticmethod
    def open(paths):
            """
            Reads the model files located at the specified paths and returns a list of
            model objects.
            """
            components = []
            for path in paths:
                if path != None:
                    component_dict = util.load_yaml_file(path)
                    component = Component(component_dict)
                    components.append(component)
            return components

    # def compute_port_dependencies(self):
	# print 'Port Dependencies for %s:' % self.name
	# for port in self.ports:
                # port_dependency = port.compute_compatible_state_set()
                # print '\t%s' % port_dependency
	# print ''


"""
device = Component()
supported_voltages = device.get_ports()[0].get_model().get_voltages()

is_supported_config = device.get_ports()[0].get_model().get_voltages()

----

device.ports.get(number=3)      # Low-level API (for on-device, calls into platform API)
device.ports.get('adc')         # High-level API (for controllers)

----

devices                                # list of available devices
device.ports()                         # list of ports attached to the device
device.ports(3, 4)                     # list of ports attached to the device
device.ports(3, 4).voltage
device.ports(3, 4).get('mode', 'voltage')
device.ports(3, 4).set('mode': 'digital', 'voltage': '5v')

----

device.ports.get('adc').set(adc=844)
    device.ports.get('adc').sample(adc=844)
    single_sample_value = device.ports.get('adc').sample()
        device.ports.get('adc').value(adc=844)
        single_sample_value = device.ports.get('adc').value()
device.ports.get('adc').publish(adc=844)
device.ports.get('adc').publish(voltage=2.4)
device.ports.get('adc').publish(voltage=2.4)
adc_value_stream = device.ports.get('adc').subscribe()

// path_config = assemble(device_001, device_002)

device.ports.get(3).voltage
device.ports.get(3).validate(mode='digital', direction='input', voltage='5v')
device.ports.get(3).configure(mode='digital', direction='input', voltage='5v')

device.ports.get([3,5,8]).validate(mode='digital', voltage='5v')
device.ports.get([3,5,8]).value(mode='digital', voltage='5v')
device.ports.set([3,5,8]).value(mode='digital', voltage='5v')

device.ports(3).voltage
device.ports(3).validate(mode='digital', direction='input', voltage='5v')
device.ports(3).configure(mode='digital', direction='input', voltage='5v')
device.ports([3,4,8]).voltage

device.ports[3].voltage
device.ports[3].validate(mode='digital', direction='input', voltage='5v')
device.ports[3].configure(mode='digital', direction='input', voltage='5v')

??? device.interfaces
system.interfaces                       # .interfaces only for system, not device? device analog is port?
system.interfaces.get('right-motor')    # interface name is specified in path name and yaml interface cfg
system.interfaces.get('robot').controller

Note:
Using the following has a parallel UI in the mobile app (i.e., diff levels of abstraction in zoom levels)
    `device.ports.*`
    `system.interfaces.*`

interfaces = device.get_interfaces()
interfaces['interface-name'].ports
"""