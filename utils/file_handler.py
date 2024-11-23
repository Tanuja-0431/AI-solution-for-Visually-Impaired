import os

def save_uploaded_file(uploaded_file):
    # Define the temp directory where you want to store the file
    temp_dir = "temp"
    
    # Check if the temp directory exists, and create it if it doesn't
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)  # Create the 'temp' directory
    
    # Generate the full file path where the uploaded file will be saved
    file_path = os.path.join(temp_dir, uploaded_file.name)
    
    # Write the file to the temp directory
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())  # Save the uploaded file
    
    return file_path  # Return the path of the saved file
