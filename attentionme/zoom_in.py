import cv2
import numpy as np
from .segmentation import segment_person


def zoom_in(image_path, output_path="zoomed_image.png"):
    person_mask, _ = segment_person(image_path)
    image = cv2.imread(image_path)

    # Find bounding box of the person mask
    coords = cv2.findNonZero(person_mask)
    x, y, w, h = cv2.boundingRect(coords)

    # Calculate padding (12.5% of height and width)
    padding_h = int(h * 0.125)
    padding_w = int(w * 0.125)

    # Calculate zoomed region with padding
    top = max(0, y - padding_h)
    bottom = min(image.shape[0], y + h + padding_h)
    left = max(0, x - padding_w)
    right = min(image.shape[1], x + w + padding_w)

    # Zoom the region of interest (ROI)
    zoomed_image = image[top:bottom, left:right]

    # Save the cropped image
    cv2.imwrite(output_path, zoomed_image)
    print(f"Zoomed image saved to {output_path}")