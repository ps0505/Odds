import pytesseract
import requests
import cv2
import time

start = time.perf_counter()
img = cv2.imread("espn1.png")
end = time.perf_counter()
print(f"Time to open image: {end - start}")
# img = img.point(lambda x: 0 if x < 150 else 255)
# img.show()
start = time.perf_counter()
text = pytesseract.image_to_string(img)
end = time.perf_counter()
print(f"Time to OCR image: {end - start}")
text = text.replace('#', '+')

print(text)


