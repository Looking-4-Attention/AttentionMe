import cv2
import numpy as np
from .segmentation import segment_person

def add_pointed_person(image_path, output_path="pointed_image_path.png"):
    person_mask, _ = segment_person(image_path)
    image = cv2.imread(image_path)

    coords = cv2.findNonZero(person_mask)
    x, y, w, h = cv2.boundingRect(coords)

    center_x = x + w // 2
    center_y = y + h // 2

    arrow_start = (x + w, center_y)
    arrow_end = (center_x, center_y)

    cv2.arrowedLine(image, arrow_start, arrow_end, (0, 0, 255), 3, tipLength=0.05)

    cv2.imwrite(output_path, image)
    print(f"이미지가 {output_path}에 저장되었습니다.")

if __name__ == "__main__":
    image_path = "image_path.png"
    add_pointed_person(image_path)
