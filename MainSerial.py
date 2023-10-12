
import tkinter
from tkinter import ttk
from SerialClass import SerialPortCommunication   # Import Serial Communication Class
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
# from SerialClass import SerialPortCommunication.open_file
class MainSerial:
    def __init__(self):
        # Define Serial Port Variables
        self.port = None
        self.band = None
        self.check = None
        self.data = None
        self.stop = None
        self.myserial = None
        self.open_file = None 

        # Initialize Form
        self.mainwin = tkinter.Tk()
        self.mainwin.title("Serial Port Communicate")
        self.mainwin.geometry("560x400")

        # Label
        self.label1 = tkinter.Label(self.mainwin,text = "Port Name:")
        self.label1.place(x = 5,y = 5)
        self.label2 = tkinter.Label(self.mainwin, text="Rate:")
        self.label2.place(x=5, y=45)
        self.label3 = tkinter.Label(self.mainwin, text="Check bits:")
        self.label3.place(x=5, y=85)
        self.label4 = tkinter.Label(self.mainwin, text="Data bits:")
        self.label4.place(x=5, y=125)
        self.label5 = tkinter.Label(self.mainwin,text = "Stop Bit:")
        self.label5.place(x = 5,y = 165)

        # Text display, clear send data
        self.label6 = tkinter.Label(self.mainwin, text="send data:")
        self.label6.place(x=230, y=5)

        self.label7 = tkinter.Label(self.mainwin, text="receive data:")
        self.label7.place(x=230, y=200)

        # Serial slogan
        self.com1value = tkinter.StringVar()  # The text that comes with the form, creating a value
        self.combobox_port = ttk.Combobox(self.mainwin, textvariable=self.com1value,
                                          width = 10)
        # Enter Selection
        self.combobox_port["value"] = [""]  # Select here first

        self.combobox_port.place(x = 105,y = 5)  # display

        # baud rate
        self.bandvalue = tkinter.StringVar()  # The text that comes with the form, creating a value
        self.combobox_band = ttk.Combobox(self.mainwin, textvariable=self.bandvalue, width=10)
        # Enter Selection
        self.combobox_band["value"] = ["4800","9600","14400","19200","38400","57600","115200"]  # Select here first
        self.combobox_band.current(6)  # Select 0 by default
        self.combobox_band.place(x=105, y=45)  # display

        # Check bits
        self.checkvalue = tkinter.StringVar()  # The text that comes with the form, creating a value
        self.combobox_check = ttk.Combobox(self.mainwin, textvariable=self.checkvalue, width=10)
        # Enter Selection
        self.combobox_check["value"] = ["No Check Bit"]  # Select here first
        self.combobox_check.current(0)  # Select 0 by default
        self.combobox_check.place(x=105, y=85)  # display

        # Data bits
        self.datavalue = tkinter.StringVar()  # The text that comes with the form, creating a value
        self.combobox_data = ttk.Combobox(self.mainwin, textvariable=self.datavalue, width=10)
        # Enter Selection
        self.combobox_data["value"] = ["8", "9", "0"]  # Values
        self.combobox_data.current(0)  # Select 0 by default
        self.combobox_data.place(x=105, y=125)  # display

        # Stop Bit
        self.stopvalue = tkinter.StringVar()  # The text that comes with the form, creating a value
        self.combobox_stop = ttk.Combobox(self.mainwin, textvariable=self.stopvalue, width=10)
        # Enter Selection
        self.combobox_stop["value"] = ["1", "0"]  # Select here first
        self.combobox_stop.current(0)  # Select 0 by default
        self.combobox_stop.place(x=105, y=165)  # display

        # Open serial port
        self.button_OK = tkinter.Button(self.mainwin, text="Open Port",
                                        command=self.button_OK_click,
                                        width = 10,height = 1)
        self.button_OK.place(x = 5,y = 210)  # Display Control
        # Close Serial Port
        self.button_Cancel = tkinter.Button(self.mainwin, text="Close Port",  # Display Text
                                 command=self.button_Cancel_click,
                                 width=10, height=1)
        self.button_Cancel.place(x = 120,y = 210)  # Display Control

        # Clear Send Data
        self.button_Cancel = tkinter.Button(self.mainwin, text="Clear Sent",  # Display Text
                                            command=self.button_clcSend_click,
                                            width=13, height=1)
        self.button_Cancel.place(x=400, y=5)  # Display Control

        # Clear Received Data
        self.button_Cancel = tkinter.Button(self.mainwin, text="Clear Received",  # Display Text
                                            command=self.button_clcRece_click,
                                            width=13, height=1)
        self.button_Cancel.place(x=400, y=202)  # Display Control

        # Send keys
        self.button_Send = tkinter.Button(self.mainwin, text="Send",  # Display Text
                                            command=self.button_Send_click,
                                            width=6, height=1)
        self.button_Send.place(x=5, y=255)  # Display Control
        # Receive keys
        self.button_Send = tkinter.Button(self.mainwin, text="Receive",  # Display Text
                                          command=self.button_Rece_click,
                                          width=6, height=1)
        self.button_Send.place(x=5, y=310)  # Display Control
        # Browse Keys
        self.button_browse = tkinter.Button(self.mainwin, text="Browse", command=self.send_file,width=6, height=1)
        self.button_browse.place(x=5, y=365)    
        # Display Box
        # Implement Notepad's functional components
        self.SendDataView = tkinter.Text(self.mainwin,width = 40,height = 10)  # Text is actually a text editor
        self.SendDataView.place(x = 230,y = 35)  # display

        self.ReceDataView = tkinter.Text(self.mainwin, width=40, height= 10)  # Text is actually a text editor
        self.ReceDataView.place(x=230, y=230)  # display

        # Sent Content
        test_str = tkinter.StringVar(value="Interface Circuit")
        self.entrySend = tkinter.Entry(self.mainwin, width=20,textvariable = test_str)
        self.entrySend.place(x = 80,y = 260)  # display

        # Get File Path
        test_str = tkinter.StringVar(value="Interface Circuit")
        self.entrySend = tkinter.Entry(self.mainwin, width=20, textvariable=test_str)
        self.entrySend.place(x=80, y=260)  # display

        # Get the parameters of the interface
        self.band = self.combobox_band.get()
        self.check = self.combobox_check.get()
        self.data = self.combobox_data.get()
        self.stop = self.combobox_stop.get()
        print("Baud rate:"+self.band)
        self.myserial = SerialPortCommunication(int(self.band),self.check,self.data,self.stop)

        # Processing Serial Port Values
        self.port_list = self.myserial.get_port()
        port_str_list = []  # Used to store cut serial numbers
        for i in range(len(self.port_list)):
            lines = str(self.port_list[i])
            str_list = lines.split(" ")
            port_str_list.append(str_list[0])
        self.combobox_port["value"] = port_str_list
        self.combobox_port.current(0)  # Select 0 by default
    def send_file(self):
        askopenfilename()
    def show(self):
        self.mainwin.mainloop()

    def button_OK_click(self):
        '''
        @ Serial Open Function
        :return: 
        '''




        if self.port == None or self.port.isOpen() == False:
            self.myserial.open_port(self.combobox_port.get())
            print("Successfully opened serial port")
        else:
            pass
            
    def button_Cancel_click(self):
        self.myserial.delete_port()
        print("Successfully closed serial port")

    def button_clcSend_click(self):
        self.SendDataView.delete("1.0","end")

    def button_clcRece_click(self):
        self.ReceDataView.delete("1.0", "end")
    def button_choose_click(self):
        filename = askopenfilename()
           
    def button_Send_click(self):
        try:
            if self.myserial.port.isOpen() == True:
                print("Start sending data")
                send_str1 = self.entrySend.get()
                self.myserial.Write_data(send_str1)
                self.SendDataView.insert(tkinter.INSERT, send_str1+" ")
                print("Successful sending of data")
            else:
                print("Serial port not open")
        except:
            print("fail in send")
    def button_Rece_click(self):
        try:
            readstr = self.myserial.Read_data()
            self.ReceDataView.insert(tkinter.INSERT, readstr + " ")
        except:
            print("read failure")

 
if __name__ == '__main__':
    my_ser1 = MainSerial()
    my_ser1.show()