import torch
from transformers import DetrImageProcessor, DetrForObjectDetection
from PIL import Image
import requests
import numpy as np
import cv2

# Load a pre-trained object detection model from Hugging Face
model_name = "facebook/detr-resnet-50"  # You can use other models from Hugging Face as well
processor = DetrImageProcessor.from_pretrained(model_name)
model = DetrForObjectDetection.from_pretrained(model_name)

# Function for object detection
def detect_objects(image_path):
    # Open image and process it
    image = Image.open(image_path)

    # Preprocess the image for the model
    inputs = processor(images=image, return_tensors="pt")

    # Perform object detection
    outputs = model(**inputs)
    
    # Get results: The model outputs bounding boxes and labels
    target_sizes = torch.tensor([image.size[::-1]])  # Convert image size
    results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]
    
    # Convert the image to a numpy array for displaying
    image_np = np.array(image)
    
    # Create an image with bounding boxes around the detected objects
    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        box = [round(i, 2) for i in box.tolist()]
        cv2.rectangle(image_np, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (255, 0, 0), 3)
        cv2.putText(image_np, f'{label.item()}: {round(score.item(), 3)}', 
                    (int(box[0]), int(box[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    
    # Save the image with bounding boxes
    output_image_path = "output_image_with_bboxes.jpg"
    cv2.imwrite(output_image_path, image_np)
    
    # Extract object labels for the user
    object_labels = [f"{model.config.id2label[label.item()]}: {round(score.item(), 3)}"
                     for score, label in zip(results["scores"], results["labels"])]
    
    return {"image": output_image_path, "objects": object_labels}
