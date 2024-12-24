import cv2
import numpy as np

# Load an image from the current directory
# Make sure the file "sample_image.png" is present in the same folder as this script
image = cv2.imread("sample_image.png")

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not load image. Please ensure 'sample_image.png' exists in the same directory.")
    exit()

# Convert the image to grayscale
# This reduces the image to a single color channel (0-255 intensity values)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Add a white border around the grayscale image using NumPy's pad function
# The pad_width=10 adds a 10-pixel border, and constant_values=255 ensures the border is white
bordered_image = np.pad(gray_image, pad_width=10, mode='constant', constant_values=255)

# Display the resulting image with a border
# A window will pop up showing the bordered image
cv2.imshow("Bordered Image", bordered_image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
