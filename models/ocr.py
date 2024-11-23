# models/ocr.py

import pytesseract
from PIL import Image,ImageFilter, ImageEnhance 
import pyttsx3


# Set Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(image_path):
    """
    Extracts text from an image using OCR (Tesseract) with preprocessing.
    """
    try:
        # Open the image
        image = Image.open(image_path)
        
        # Preprocess the image
        image = image.convert("L")  # Convert to grayscale
        image = image.filter(ImageFilter.SHARPEN)  # Sharpen the image
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2)  # Enhance contrast
        
        # Use Tesseract to extract text
        text = pytesseract.image_to_string(image)
        text = text.strip()  # Remove unnecessary whitespace
        
        # Validate the extracted text
        if not text or text.isspace():
            return "No readable text found in the image."
        
        return text
    except Exception as e:
        return f"Error in extracting text: {e}"

def text_to_speech(text):
    """
    Convert the given text to speech using pyttsx3.
    """
    try:
        # Initialize the pyttsx3 engine
        engine = pyttsx3.init()
        
        # Configure voice properties
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)  # Select voice (index 0 or 1 for male/female)
        engine.setProperty('rate', 150)  # Set speech rate (words per minute)
        engine.setProperty('volume', 1.0)  # Set volume (0.0 to 1.0)
        
        # Convert the text to speech
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in text-to-speech: {e}")
        return f"Error in text-to-speech: {e}"
