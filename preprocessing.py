import cv2
import numpy as np

def preprocess_image(image_path, save_path="1p.png"):
    # Load image
    image = cv2.imread('1.png')

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Save processed image
    cv2.imwrite(save_path, edges)
    print(f"Preprocessed image saved as {save_path}")

if __name__ == "__main__":
    preprocess_image("2.png")  # Run preprocessing

