import cv2
import numpy as np
from .segmentation import segment_person

def add_pointed_person(image_path, output_path="pointed_image_path.png", arrow_thickness=3, arrow_color=(0, 0, 255)):
    person_mask, _ = segment_person(image_path)
    image = cv2.imread(image_path)

    coords = cv2.findNonZero(person_mask)
    x, y, w, h = cv2.boundingRect(coords)

    center_x = x + w // 2
    center_y = y + h // 2

    arrow_start = (x + w, center_y)
    arrow_end = (center_x, center_y)

    cv2.arrowedLine(image, arrow_start, arrow_end, arrow_color, arrow_thickness, tipLength=0.05)

    cv2.imwrite(output_path, image)
    print(f"Pointed image saved as {output_path}")

if __name__ == "__main__":
    image_path = "image_path.png"
    add_pointed_person(image_path, arrow_thickness=5, arrow_color=(0, 255, 0))
