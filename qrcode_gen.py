import pyqrcode
import cv2
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.youtube.com/"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
#url.svg("myyoutube.svg", scale = 8)

#cv2.imshow("new Qr",url)

