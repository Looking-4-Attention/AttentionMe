Usage
=====

Here’s a simple example to get started with the background removal feature.  
For your information, there is a **Sample Usage Repository** in this organization.

### Example Code

```python
from attentionme import *
import cv2

# Path to the input image
image_path = 'sample_images/group1.jpg'

# Read and save the original image
image = cv2.imread(image_path)
cv2.imwrite('image_outputs/original_image.png', image)

# Perform background removal
remove_background(image_path, 'image_outputs/removed_background_image.png')