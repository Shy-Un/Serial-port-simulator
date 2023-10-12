
import serial
import serial.tools.list_ports
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfile
class SerialPortCommunication:
    def __init__(self,band=115200,check="No Check Bit",data=8,stop=1):
        self.port = None
        # Get Available Serial Ports
        self.port_list = list(serial.tools.list_ports.comports())
        assert (len(self.port_list) != 0),"No Serial Port Available"

        self.bandRate = band
        self.checkbit = check
        self.databit = data
        self.stopbit = stop

        # Read and write data
        self.read_data = None
        self.write_data = None

        pass
    def show_port(self):
        for i in range(0,len(self.port_list)):
            print(self.port_list[i])

    def show_other(self):
        print("Baud rate:"+self.bandRate)
        print("Check digit:" + self.checkbit)
        print("Data bits:" + self.databit)
        print("Stop bits:" + self.stopbit)
    # Return to Serial Port
    def get_port(self):
        return self.port_list
    # Open Serial Port
    def open_port(self,port):
        self.port = serial.Serial(port, self.bandRate,timeout = None)

    def delete_port(self):
        if self.port != None:
            self.port.close()
            print("Close Serial Port Complete")
        else:
            pass

    def Read_data(self):   # Self.port.read (self.port.in_wait) indicates that all data in the receiving serial port is received
        self.read_data = self.port.read(self.port.in_waiting)   # Read data
        return self.read_data.decode("utf-8")

    def Write_data(self,data):
        if self.port.isOpen() == False:
            print("Serial Port Open Error")
        else:
            self.port.write(data.encode("utf-8")) 
    def open_file(self):
        askopenfilename() 
    # def Stream_write(self)
    #     if streamw == '1' :
    #        streamw = '0'
    #     else
    #       if self.port.is_open() == False:
    #           print("Serial Port Open Error!")
    #       else:  
    #           while (streamw)
    #               if data.encode
    #               self.port.write(data.encode("utf-8"))
    #               self.read_data = self.port.read(self.port.in_waiting)   # Read data
    #               return self.read_data.decode("utf-8")
    #       streamw = '1'
if __name__ == '__main__':
    myser = SerialPortCommunication()
    myser.open_port("COM÷")
    myser.delete_port()
    myser.show_port()