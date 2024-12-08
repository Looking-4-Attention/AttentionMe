# AttentionMe: Effects Library for Attention Seekers

[![standard-readme compliant](https://img.shields.io/badge/python%20library-Open%20Source-skyblue.svg?style=flat-square)](https://github.com/Looking-4-Attention/AttentionMe)

AttentionMe is a Python library designed to enhance video and image processing by focusing on people segmentation and attention-grabbing features. It’s developed as a final team project for *Fundamentals of Open Source Software* (Fall semester, Hanyang University, ERICA Campus, 2024).

Whether you're looking to highlight yourself in a video or create a professional presentation, **AttentionMe** provides all the tools you need to make your content stand out.

[한국어 README](README_KO.md)

---

## Background

Have you ever felt the urge to be the center of attention? Just like the lyrics from *Hype Boy* by New Jeans,
> "You got me looking for attention."

With AttentionMe, you can make that a reality. The library focuses on preprocessing videos and images to enhance the user’s presence. It provides tools for:

- Background removal
- Zoom In
- etc.

Keep that in mind, this project was developed to promote teamwork and deepen our understanding of **open source software** development practices by the undergraduate students.

---

## Features

- **Background Removal**: Isolate subjects by removing unwanted backgrounds.
- **Zoom In**: Automatically zoom in on key areas for emphasis.
- **Brightness Adjustment for Background**: Fine-tune brightness to enhance visibility.
- **Target Pointing**: Draw attention to specific points with pointing and cropping functionalities.

---

## Installation

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- Required libraries like `PyTorch`, `NumPy`, and `OpenCV`

### Steps

You can install AttentionMe from PyPI:
   ```bash
   pip install attentionme
   ```

---

## Usage

Here’s a simple example to get started with the background removal feature. For your inforamtion, there is a Sample Usage repository in this organization.:
```python
from attentionme import *

image_path = 'sample_images/group1.jpg'
output_path = 'image_outputs/removed_background_image.png'

remove_background(image_path, output_path)
```

---

## Modules

-   **`segmentation.py`**: Provides functionality to detect and segment people in images and videos.
-   **`remove_background.py`**: A background removal tool that allows focusing solely on people, commonly known as the "cut-out" feature.
-   **`zoom_in.py`**: A zoom-in feature that emphasizes areas with people to highlight them.
-   **`crop.py`**: Easily crop images to your desired size or focus area.
-   **`adjust_brightness.py`**: Adjusts brightness to improve visual clarity by enhancing the background's visibility.
-   **`pointing.py`**: Adds arrows or markers next to individuals in images or videos for highliting.
-   **`enlargement.py`**: Allows users to zoom into specific parts of an image to examine fine details.

---

## Maintainer

This project is maintained by the leader of the team _Looking 4 Attention_:

-   [Aenoc Woo](https://github.com/wwwwje2008)

Feel free to reach out if you have questions or suggestions.

---

## Contributing

Main Contributors and the member of the team _Looking 4 Attention_:

-   [Namhoon Cho](https://github.com/Namhoon-Cho)
-   [Dami Lee](https://github.com/iamdami)
-   [Hyunsoo Kim](https://github.com/hyun1227)

We also welcome contributions! To get started:

1.  Fork the repository.
2.  Create a new branch: `git checkout -b feature/your-feature-name`.
3.  Commit your changes: `git commit -m 'Add feature'`.
4.  Push your branch: `git push origin feature/your-feature-name`.
5.  Submit a pull request for review.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
