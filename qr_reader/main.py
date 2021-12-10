import cv2
import re

img=cv2.imread("qr_luis.png")
det=cv2.QRCodeDetector()
val, pts, st_code=det.detectAndDecode(img)
print(val)

