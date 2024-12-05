import numpy as np
import threading
import cv2
import torch
from torchvision import models
from torchvision.transforms import functional as F

# Load pretrained model for segmentation
model = models.detection.maskrcnn_resnet50_fpn(pretrained=True)
model.eval()


def segment_person(image_path):
    """
    Segments the image to isolate a specific person based on the provided index.

    Args:
        image_path (str): Path to the input image.

    Returns:
        person_mask (numpy.ndarray): Binary mask of the selected person.
        background_mask (numpy.ndarray): Binary mask of everything except the person.
    """

    # Load image
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convert to tensor for model input
    image_tensor = F.to_tensor(image_rgb).unsqueeze(0)

    with torch.no_grad():
        outputs = model(image_tensor)

    labels = outputs[0]['labels']
    scores = outputs[0]['scores']
    masks = outputs[0]['masks']
    person_boxes = [outputs[0]['boxes'][i].cpu().numpy() for i in range(len(labels)) if labels[i] == 1 and scores[i] > 0.7]
    person_masks = [masks[i, 0].cpu().numpy() for i in range(len(labels)) if labels[i] == 1 and scores[i] > 0.7]

    if not person_masks:
        raise ValueError("No persons detected in the image.")

    # Draw bounding boxes and labels on the image
    image_with_boxes = image.copy()
    for i, box in enumerate(person_boxes):
        x1, y1, x2, y2 = map(int, box)
        # Draw rectangle for each detected person
        cv2.rectangle(image_with_boxes, (x1, y1), (x2, y2), (127, 255, 127), 2)
        # Put person index text
        cv2.putText(
            image_with_boxes,
            f"Person {i}",
            (x1, y1 + 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (127, 255, 127),
            2
        )

    # Function to capture console input
    def show_image():
        nonlocal person_index
        nonlocal image_with_boxes

        # Display the image with bounding boxes
        cv2.imshow("Detected Persons", image_with_boxes)

        # Event loop to display the image and handle window close
        while True:
            key = cv2.waitKey(1) & 0xFF  # Non-blocking wait

            # Break if input is received
            if person_index is not None:
                break

        cv2.destroyAllWindows()

    # Start input thread
    person_index = None
    show_image_thread = threading.Thread(target=show_image)
    show_image_thread.start()

    # Ask the user to select a person
    print("\n=== Detected Persons ===")
    for i, box in enumerate(person_boxes):
        x1, y1, x2, y2 = map(int, box)
        print(f"Person {i}: Bounding Box [x1={x1}, y1={y1}, x2={x2}, y2={y2}]")

    person_index = int(input("Enter the number of the person you want to process: "))

    # Validate the input
    if not (0 <= person_index < len(person_masks)):
        raise ValueError(f"Invalid person index: {person_index}. Please select between 0 and {len(person_masks) - 1}.")

    # Select the specified person
    selected_mask = person_masks[person_index]
    person_mask = (selected_mask > 0.5).astype(np.uint8)
    background_mask = 1 - person_mask

    return person_mask, background_mask
