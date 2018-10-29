from pymoduleconnector import ModuleConnector
from pymoduleconnector.ids import XTID_SM_STOP
from pymoduleconnector.ids import XTS_ID_APP_PRESENCE_2
from pymoduleconnector.ids import XTS_ID_PRESENCE_SINGLE
from pymoduleconnector.ids import XTS_ID_BASEBAND_IQ
from pymoduleconnector.ids import XTID_SM_RUN

import numpy as np

class StreamData:
    sampling_frequency = 17 # frames per second

    def __init__(self, usb_port):
        '''
        Parser for streaming data from Xethru X4M300 presence sensor from Novelda.

        :param usb_port: String
        '''
        self.usb_port = usb_port

        self.mc = ModuleConnector(usb_port)

        self.x4m300 = self.mc.get_x4m300()

        self.x4m300.set_sensor_mode(XTID_SM_STOP, 0)
        self.x4m300.load_profile(XTS_ID_APP_PRESENCE_2)
        self.x4m300.set_output_control(XTS_ID_PRESENCE_SINGLE, 1)
        self.x4m300.set_output_control(XTS_ID_BASEBAND_IQ, 1)
        self.x4m300.set_sensor_mode(XTID_SM_RUN, 0)


    def __iter__(self):
        while True:
            yield self.read_sensor()

    def read_sensor(self):
        '''
        Read data from sensor
        :return:
        '''
        messege = self.x4m300.read_message_baseband_iq()

        i_data = []
        q_data = []

        for data in messege.i_data:
            i_data = np.append(i_data, data)

        for data in messege.q_data:
            q_data = np.append(q_data, data)

        return (i_data, q_data)


if __name__ == '__main__':
    from secrets import USB_PORT

    sd = StreamData(USB_PORT)

    for i_data, q_data in sd:
        print('i_data:', i_data)
        print('q_data:', q_data)
