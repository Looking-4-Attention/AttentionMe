import cv2
import numpy as np
from .segmentation import segment_person

def adjustBrightness(image_path, output_path="adjustBrightness_image.png", brightness_factor=0.6):
    _, background_mask = segment_person(image_path)
    image = cv2.imread(image_path)

    #Adjust background brightness
    background_mask = background_mask[:,:, np.newaxis]
    adjusted_background = image * background_mask * brightness_factor

    #merge background
    result=image*(1-background_mask)+adjusted_background

    #Save the Brightness adjusted image
    cv2.imwrite(output_path, result)
    print(f"Adjusted background saved to {output_path}")
