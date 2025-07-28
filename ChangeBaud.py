import time
import serial
from serial.tools import list_ports
from colorama import init, Cursor

init()

def Erase_Line():
    print(Cursor.UP(1) + '\033[2K', end='')

def Erase_Print(text):
    Erase_Line()
    print(text)

def find_Makcu():
    for port in list_ports.comports():
        if "USB-Enhanced-SERIAL CH343" in port.description or "VID:PID=1A86:55D3" in port.hwid:
            return port.device
    return None

def Connect_Makcu(baudRate, port):
    MakcuConn = serial.Serial(port, baudRate, timeout=1)
    Erase_Print(f"Connected To MAKCU! {{Port: {port} | Baud Rate: {baudRate}}}\033[0m")
    time.sleep(2)
    return MakcuConn

def main():
    Erase_Print(f"Baud Rate Changer For MAKCU!")
    time.sleep(3)
    Erase_Line()
    
    # Find The Port We Can Connect To Our MAKCU With.
    ComPort = find_Makcu()
    if not ComPort:
        Erase_Print("Could Not Detect A MAKCU!")
        return

    try:
        Erase_Print(f"Trying To Connect To MAKCU...")
        time.sleep(1)
    
        # Connect To The MAKCU. Using The Default Baud Rate.   
        MakcuConn = Connect_Makcu(115200, ComPort)
        
        # Send the needed bytes to change the baud rate to 4m.
        Erase_Print(f"Sending Bytes To Change Baud Rate...")
        time.sleep(3)
        
        MakcuConn.write(bytearray([0xDE, 0xAD, 0x05, 0x00, 0xA5, 0x00, 0x09, 0x3D, 0x00]))
        MakcuConn.close()           
        time.sleep(0.1)
        
        # Connect Back To The MAKCU With The New Baud Rate.
        MakcuConn = Connect_Makcu(4000000, ComPort)
        MakcuConn.flush()
        
        # Try To Send and Receive Data From The MAKCU To Ensure Baud Rate Was Changed Correctly.
        Erase_Print(f"Trying To Communicate With New Baud Rate...")
        time.sleep(2)
        
        MakcuConn.write(b"km.version()\r")
        data = MakcuConn.readline()
        
        # Check If We Got The Expected Response From The MAKCU. On The New Baud Rate.
        if "km.MAKCU" in data.decode("utf-8"):
            Erase_Print(f"Successfully Changed Baud Rate To 4000000!\r\nNote: This is NOT permanent! You will need to re run this everytime your MAKCU is turned off and back on.")
        else:
            Erase_Print("Failed To Change Baud Rate!")
        
        # Close The Connection To The MAKCU.
        MakcuConn.close()
            
    except Exception as error:
        Erase_Print(f"There was an Error! {error}")

if __name__ == "__main__":
    main()
    time.sleep(10)
