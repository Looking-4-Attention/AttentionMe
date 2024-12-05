import cv2
import numpy as np
from .segmentation import segment_person


def crop(image_path, output_path="cropped_person.png"):
    person_mask, _ = segment_person(image_path)
    image = cv2.imread(image_path)

    # Find bounding box of the person mask
    coords = cv2.findNonZero(person_mask)
    x, y, w, h = cv2.boundingRect(coords)

    # Crop the region of interest (ROI)
    cropped_image = image[y:y+h, x:x+w]

    # Save the cropped image
    cv2.imwrite(output_path, cropped_image)
    print(f"Cropped image saved to {output_path}")
