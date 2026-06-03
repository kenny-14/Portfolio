import base64
import os

# Tracks your main folder
script_dir = os.path.dirname(os.path.abspath(__file__))

# Looking directly in Kenny Codes, exactly where your file is!
image_path = os.path.join(script_dir, "web.photo.jpeg")

if os.path.exists(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    print("\n--- COPY EVERYTHING BELOW THIS LINE ---")
    print(encoded_string)
    print("--- END OF CODE ---")
else:
    print("\nERROR: Still cannot find the image file.")
    print(f"Looked here: {image_path}")