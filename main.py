import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tessaract OCR\tesseract.exe"
img = Image.open("hh.JPG")
text = pytesseract.image_to_string(img)
print(text)
