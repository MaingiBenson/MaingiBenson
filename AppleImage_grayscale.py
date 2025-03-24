import cv2
import numpy as np
import os

def convert_to_grayscale(image_path):
    """Converts an image to grayscale and displays it."""
    try:
        # Load the image from the specified path
        image = cv2.imread(image_path)

        if image is None:
            print(f"Error: Could not load image from {image_path}. Please check the file path.")
            return

        # Convert to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply a simple threshold (you can adjust this)
        _, thresholded = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

        # Display the grayscale and thresholded images
        cv2.imshow('Original Image', image)
        cv2.imshow('Grayscale Image', gray_image)
        cv2.imshow('Thresholded Image', thresholded)
        print("Threshold value used: 127")

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"An error occurred: {e}")

image_path = "C:\\Users\\CARSON\\OneDrive\\Desktop\\school\\3.2\\Computer Graphics\\Images_Graphics\\Green_Apple.jpeg"

#check if the file exists before attempting to open it.
if os.path.exists(image_path):
    convert_to_grayscale(image_path)
else:
    print(f"Error: The file '{image_path}' does not exist.")