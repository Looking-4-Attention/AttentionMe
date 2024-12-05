import cv2
import numpy as np
from .segmentation import segment_person
import cv2
import numpy as np
from .segmentation import segment_person


def enlargement(image_path, output_path="enlarged_image.png", scale=2):
    # Load image and segmentation mask
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    person_mask, _ = segment_person(image_path)

    # Ensure mask is binary (0 or 255)
    person_mask = (person_mask > 0.5).astype(np.uint8) * 255

    # Find coordinates of the object in the mask
    coords = cv2.findNonZero(person_mask)
    x, y, w, h = cv2.boundingRect(coords)

    # Crop the object using the mask
    roi = cv2.bitwise_and(image, image, mask=person_mask)
    cropped_roi = roi[y:y+h, x:x+w]
    cropped_mask = person_mask[y:y+h, x:x+w]

    # Enlarge the cropped ROI and the mask
    enlarged_roi = cv2.resize(cropped_roi, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    enlarged_mask = cv2.resize(cropped_mask, None, fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)

    # Create a blank canvas for the output image
    canvas = np.zeros_like(image)
    mask_canvas = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)

    # Calculate placement for enlarged ROI
    roi_height, roi_width = enlarged_roi.shape[:2]
    center_x = x + w // 2
    center_y = y + h // 2
    new_x = center_x - roi_width // 2
    new_y = center_y - roi_height // 2

    # Calculate the valid region within the image boundaries
    start_x = max(0, new_x)
    start_y = max(0, new_y)
    end_x = min(image.shape[1], new_x + roi_width)
    end_y = min(image.shape[0], new_y + roi_height)

    # Calculate the corresponding region in the enlarged ROI
    roi_start_x = max(0, -new_x)
    roi_start_y = max(0, -new_y)
    roi_end_x = roi_start_x + (end_x - start_x)
    roi_end_y = roi_start_y + (end_y - start_y)

    # Place the enlarged ROI and mask within the valid region
    canvas[start_y:end_y, start_x:end_x] = enlarged_roi[roi_start_y:roi_end_y, roi_start_x:roi_end_x]
    mask_canvas[start_y:end_y, start_x:end_x] = enlarged_mask[roi_start_y:roi_end_y, roi_start_x:roi_end_x]

    # Blend the original image with the enlarged object
    inverse_mask = cv2.bitwise_not(mask_canvas)
    background = cv2.bitwise_and(image, image, mask=inverse_mask)
    result = cv2.add(background, canvas)

    # Save the result
    cv2.imwrite(output_path, result)
    print(f"Enlarged image saved to {output_path}")
