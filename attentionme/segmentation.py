import cv2
import numpy as np
from torchvision import models
import torch
from torchvision.transforms import functional as F

# Load pretrained model for segmentation
model = models.detection.maskrcnn_resnet50_fpn(pretrained=True)
model.eval()


def segment_person(image_path):
    """
    Segments the image to isolate a specific person based on the provided index.

    Args:
        image_path (str): Path to the input image.
        person_index (int): Index of the person to isolate.

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
    masks = outputs[0]['masks']
    person_boxes = [outputs[0]['boxes'][i].cpu().numpy() for i in range(len(labels)) if labels[i] == 1]
    person_masks = [masks[i, 0].cpu().numpy() for i in range(len(labels)) if labels[i] == 1]

    if not person_masks:
        raise ValueError("No persons detected in the image.")

    print("\n=== Detected Persons ===")
    for i, box in enumerate(person_boxes):
        x1, y1, x2, y2 = map(int, box)
        print(f"Person {i}: Bounding Box [x1={x1}, y1={y1}, x2={x2}, y2={y2}]")

    person_index = int(input("Enter the number of the person you want to process: "))

    if person_index < 0 or person_index >= len(person_masks):
        raise ValueError(f"Invalid person index: {person_index}. Please select between 0 and {len(person_masks) - 1}.")

    # Select the specified person
    selected_mask = person_masks[person_index]
    person_mask = (selected_mask > 0.5).astype(np.uint8)
    background_mask = 1 - person_mask

    return person_mask, background_mask