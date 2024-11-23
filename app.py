import streamlit as st
import time
from models.scene import generate_caption
from models.ocr import extract_text, text_to_speech
from utils.file_handler import save_uploaded_file
from models.object_detection import detect_objects
from models.item_recognition import recognize_items

# Apply custom CSS for trendy vibes
with open("styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# App Title and Instructions
st.title("AI Assistance for Visually Impaired Individuals")

# Description and How it Works Section
st.markdown("""
    ## How it works:
    1. **Upload an image** of your surroundings or any document you'd like assistance with.
    2. **Select a functionality**:
        - **Real-Time Scene Understanding**: The app will analyze the image and provide a description of the scene to help you understand the environment.
        - **Text-to-Speech Conversion**: The app will extract any visible text from the image and convert it into audible speech, helping you access written content.
        - **Object and Obstacle Detection**: Detect objects and obstacles in the uploaded image for safe navigation.
        - **Personalized Assistance**: Recognize items and assist with descriptions for daily tasks.
    3. The app will process the image and provide the result to you, accompanied by real-time updates.
""")

# Upload Image
uploaded_image = st.file_uploader("Upload an Image 📷", type=["jpg", "png", "jpeg"])

if uploaded_image:
    # Save image to a temporary location
    file_path = save_uploaded_file(uploaded_image)
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    
    # Choose functionality
    option = st.radio("Select a functionality:", 
                      ("Real-Time Scene Understanding", 
                       "Text-to-Speech Conversion",
                       "Object and Obstacle Detection for Safe Navigation",
                       "Personalized Assistance for Daily Tasks"))

    if option == "Real-Time Scene Understanding":
        # Display a progress bar while generating the caption
        st.write("Generating Scene Description... Please wait.")
        progress = st.progress(0)  # Initialize the progress bar

        # Simulate processing time with a loop (this is just for demonstration)
        for i in range(100):
            time.sleep(0.05)  # Simulate some work being done (e.g., model inference)
            progress.progress(i + 1)  # Update the progress bar

        # Once progress bar is done, generate the caption
        caption = generate_caption(file_path)
        st.write("Scene Description 🖼️:")
        st.write(caption)
    
    elif option == "Text-to-Speech Conversion":
        # Display a progress bar while extracting text and converting to speech
        st.write("Extracting Text... Please wait.")
        progress = st.progress(0)

        # Simulate processing time with a loop
        for i in range(100):
            time.sleep(0.05)  # Simulate some work (OCR or text-to-speech)
            progress.progress(i + 1)  # Update the progress bar

        # Once progress bar is done, extract text and convert to speech
        text = extract_text(file_path)
        if text:
            st.write("Extracted Text 📝:")
            st.write(text)
            st.write("Playing the text as speech 🎤...")
            text_to_speech(text)
        else:
            st.write("No text found in the image.")

    elif option == "Object and Obstacle Detection for Safe Navigation":
        # Display a progress bar while detecting objects
        st.write("Detecting Objects... Please wait.")
        progress = st.progress(0)

        # Simulate processing time with a loop (adjust with actual processing time)
        for i in range(100):
            time.sleep(0.05)  # Simulate some work
            progress.progress(i + 1)

        # Once progress bar is done, detect objects in the uploaded image
        detected_objects = detect_objects(file_path)

        # Show the image with detected objects
        st.write("Objects Detected 🔍:")
        st.image(detected_objects["image"], caption="Image with Detected Objects", use_column_width=True)

        # Display detected object names and descriptions
        st.write("Detected Objects List 🏷️:")
        if detected_objects["objects"]:
            for obj in detected_objects["objects"]:
                st.write(f"- {obj}")
        else:
            st.write("No objects detected in the image.")

    elif option == "Personalized Assistance for Daily Tasks":
    # Display a progress bar while recognizing items
        st.write("Recognizing Items... Please wait.")
        progress = st.progress(0)

    # Simulate processing time with a loop (adjust with actual processing time)
        for i in range(100):
            time.sleep(0.05)  # Simulate some work
            progress.progress(i + 1)

    # Once progress bar is done, recognize items in the uploaded image
        recognized_items = recognize_items(file_path)

    # Debugging: Print the recognized_items structure to check its contents


    # Show the image with recognized items
        st.write("Recognized Items 🛍️:")
        if "image" in recognized_items:
            st.image(recognized_items["image"], caption="Image with Recognized Items", use_column_width=True)
    
    # Check if the 'items' key exists and it's a list
        if "items" in recognized_items and isinstance(recognized_items["items"], list):
            st.write("Item Descriptions 📜:")
            for item in recognized_items["items"]:
                if isinstance(item, dict) and "name" in item and "description" in item:
                   st.write(f"- {item['name']}: {item['description']}")
                else:
                   st.write(f"- {item} (Invalid item format)")
    else:
        st.write("No recognized items found or the items structure is invalid.")
