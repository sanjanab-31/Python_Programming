import pywhatkit
import pyqrcode
from pyqrcode import QRCode
class supermarket:
    def __init__(self):
        print("Welcome to the Supermarker")

    def sendmsg(self,mobile,info):
        pywhatkit.sendwhatmsg_instantly("+918610500527",info)
    def getQr(self):
        url=pyqrcode.create("Amount is: 1000")
        url.svg("about.svg",scale=8)
        print("Done")

s=supermarket()
s.getQr()
s.sendmsg("+918610500527","Hello, this is a test message.")

print("Done")
