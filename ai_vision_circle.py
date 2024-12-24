import cv2
import numpy as np

def identify_container(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load the image at {image_path}.")
        return

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect circular shapes (e.g., bottle caps)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50, param1=50, param2=30, minRadius=10, maxRadius=100)

    # Display results
    if circles is not None:
        circles = np.uint16(np.around(circles))
        print("Container(s) detected!")
        for circle in circles[0, :]:
            print(f"Circle found at (x: {circle[0]}, y: {circle[1]}) with radius: {circle[2]}")
            # Draw the circle and its center
            cv2.circle(image, (circle[0], circle[1]), circle[2], (0, 255, 0), 2)
            cv2.circle(image, (circle[0], circle[1]), 2, (0, 0, 255), 3)
    else:
        print("No container detected.")

    # Show the processed image with detected circles
    cv2.imshow("Detected Containers", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Use the sample image for testing
sample_image = "images/sample_image2.png"
identify_container(sample_image)