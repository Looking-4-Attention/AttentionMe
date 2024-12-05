import cv2
import numpy as np
from segmentation import segment_person

def remove_background(image_path, output_path="output_no_background.png"):
    """
    Removes the background of the image, keeping only the selected person visible,
    and saves the result with a transparent background.
    
    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the resulting image with no background.
    """
    # Perform segmentation
    person_mask, _ = segment_person(image_path)

    # Load the original image
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    
    # Ensure the image has 3 channels (RGB)
    if image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

    # Set the alpha channel (transparency) based on the person mask
    alpha_channel = (person_mask > 0.5).astype(np.uint8) * 255
    image[:, :, 3] = alpha_channel  # Replace the existing alpha channel with the mask

    # Save the resulting image as a PNG with transparency
    cv2.imwrite(output_path, image)
    print(f"Image with removed background saved as {output_path}")

if __name__ == "__main__":
    image_path = "input.jpg"  # Replace with your input image path
    output_path = "output_no_background.png"  # Replace with your desired output path

    try:
        remove_background(image_path, output_path)
    except ValueError as e:
        print(f"Error: {e}")
