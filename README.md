# AI Vision Project by Adity

This project demonstrates basic image processing using Python, OpenCV, and NumPy. The script loads an image, converts it to grayscale, and adds a white border around it.

## Prerequisites

Before running the script, ensure you have the following installed:
- Python (3.7 or newer)
- Required Python packages:
  - `opencv-python`
  - `numpy`

You can install the required packages using `pip`:
```bash
pip install opencv-python numpy
```

## Getting Started

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/bfouzder/Python-Ai-Vision-by-OpenCV-NumPy.git
   ```
2. Navigate to the project folder:
   ```bash
   cd ai-vision
   ```

3. Ensure the following files are present:
   - `ai_vision.py` (the main script)
   - `sample_image.png` (an image file to process)
   - `ai_vision_circle.py` (the main script)
   - `sample_image2.png` (an image file to process)

4. Run the script:
   ```bash
   python ai_vision.py
   ```

## How It Works

1. **Image Loading**:
   - The script loads `sample_image.png`, `sample_image2.png` from the current directory.
   - If the image is not found, it will display an error and exit.

2. **Grayscale Conversion**:
   - The loaded image is converted to grayscale to simplify the color channels.

3. **Add Border**:
   - A white border (10 pixels wide) is added to the image using NumPy.

4. **Display the Image**:
   - The final bordered image is displayed in a pop-up window.

## Sample Output

When the script runs successfully, you should see a pop-up window with the bordered image.

## Troubleshooting

- If you encounter an error related to `cv2.imshow`, ensure you have the full `opencv-python` package installed (not the headless version):
  ```bash
  pip uninstall opencv-python-headless
  pip install opencv-python
  ```

- Ensure the file `sample_image.png` exists in the same directory/images as the script.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributions

Feel free to fork the repository and submit pull requests to enhance the project!

