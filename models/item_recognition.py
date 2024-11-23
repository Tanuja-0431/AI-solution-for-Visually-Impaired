from transformers import pipeline
from PIL import Image
# models/item_recognition.py (for improved object descriptions)
from collections import Counter

def recognize_items(image_path):
    """
    Recognizes and classifies items in the uploaded image.
    Condenses repetitive detections and provides more meaningful descriptions.
    """
    # Example output from your object detection model (this can vary based on your model)
    recognized_objects = ["person", "person", "handbag", "cell phone", "person", "person", "handbag", "cell phone", "backpack"]

    # Count the occurrences of each object
    object_counts = Counter(recognized_objects)

    # Provide more meaningful descriptions for each recognized item
    object_descriptions = {
        "person": "A person. This could be someone in the scene.",
        "handbag": "A handbag. It might contain essential items such as keys, phone, or wallet.",
        "cell phone": "A cell phone. Used for communication, browsing the web, etc.",
        "backpack": "A backpack. Often used to carry books, clothes, or other personal items."
    }

    # List the objects with descriptions and counts
    result = []
    for obj, count in object_counts.items():
        description = object_descriptions.get(obj, f"A {obj}.")
        result.append(f"{obj.capitalize()}: {description} (Found {count} times)")

    return {
        "image": image_path,  # This would be the image path or processed image after annotation
        "items": result
    }


