import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Test OCR
from PIL import Image
text = pytesseract.image_to_string(Image.open('istockphoto-1146968118-612x612.jpg'))  # Replace with your image
print(text)