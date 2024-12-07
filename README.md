# AttentionMe: Effects Library for Attention Seekers(부제 부분)

[![standard-readme compliant](https://img.shields.io/badge/python%20library-Open%20Source-skyblue.svg?style=flat-square)](https://github.com/Looking-4-Attention/AttentionMe)

AttentionMe is a Python library designed to enhance video and image processing by focusing on people segmentation and attention-grabbing features. It’s developed as a final team project for *Fundamentals of Open Source Software* (Fall semester, Hanyang University, ERICA Campus, 2024).

Whether you're looking to highlight yourself in a video or create a professional presentation, **AttentionMe** provides all the tools you need to make your content stand out.

[한국어 README](#attentionme-관종을-위한-효과-라이브러리)

---

## Table of Contents

- [Background](#background)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Modules Overview](#modules-overview)
- [Maintainer](#maintainer)
- [Contributing](#contributing)
- [License](#license)

---

## Background

Have you ever felt the urge to be the center of attention? Just like the lyrics from *Hype Boy* by New Jeans,
> "You got me looking for attention."

With AttentionMe, you can make that a reality. The library focuses on preprocessing videos and images to enhance the user’s presence. It provides tools for:

- People segmentation
- Background removal
- Dynamic zooming
- Highlighting specific subjects

Keep that in mind, this project was developed to promote teamwork and deepen our understanding of **open source software** development practices by the undergraduate students.

---

## Features

- **People Segmentation**: Accurately segment individuals in videos or images.
- **Background Removal**: Isolate subjects by removing unwanted backgrounds.
- **Zoom In**: Automatically zoom in on key areas for emphasis.
- **Brightness Adjustment for Background**: Fine-tune brightness to enhance visibility.
- **Target Pointing**: Draw attention to specific points with pointing and cropping functionalities.
- **Customizable Workflow**: Modular design allows easy integration and extension.

---

## Installation

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- Required libraries like `Pillow`, `NumPy`, and `OpenCV`

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Looking-4-Attention/AttentionMe.git
   cd AttentionMe

2. Install the repository:
   ```bash
   git clone https://github.com/Looking-4-Attention/AttentionMe.git
   cd AttentionMe
3. Clone the repository:
   ```bash
   git clone https://github.com/Looking-4-Attention/AttentionMe.git
   cd AttentionMe
   ```

---

## Usage

Here’s a simple example to get started with the segmentation feature. For your inforamtion, there is a Sample Usage repository in this organization.:
```bash
from attentionme.segmentation import segment_people
from attentionme.remove_background import remove_background

# Load an input image
input_file = "example.jpg"

# Segment people from the image
segmented_image = segment_people(input_file)

# Remove the background for a cleaner look
final_image = remove_background(segmented_image)

# Save the result
final_image.save("output.jpg")
```

---

## Modules Overview

-   **`segmentation.py`**: Provides functionality to detect and segment people in images and videos.
-   **`remove_background.py`**: A background removal tool that allows focusing solely on people, commonly known as the "cut-out" feature.
-   **`zoom_in.py`**: A zoom-in feature that emphasizes areas with people to highlight them.
-   **`crop.py`**: Easily crop images to your desired size or focus area.
-   **`adjust_brightness.py`**: Adjusts brightness to improve visual clarity by enhancing the background's visibility.
-   **`pointing.py`**: Adds arrows or markers next to individuals in images or videos for highliting.
-   **`enlargement.py`**: Allows users to zoom into specific parts of an image to examine fine details.

  --

## Maintainer

This project is maintained by the leader of the team _Looking 4 Attention_:

-   [Aenok Woo](https://github.com/wwwwje2008)

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

---

# AttentionMe: 관종을 위한 효과 라이브러리

AttentionMe는 2024년 2학기 한양대학교 에리카캠퍼스의 오픈소스 소프트웨어 기초 수업을 위한 기말고사 대체 팀 프로젝트로서 제작된 오픈소스 파이썬 라이브러리입니다.

이 프로젝트는 영상 및 이미지에서 사람을 인식하고 배경 제거, 줌, 강조 등의 다양한 기능을 제공합니다. 한국어 버전 문서를 통해 프로젝트와 기능을 이해할 수 있습니다.
사진 속에서에서 자신을 돋보이게 하고 싶다면, AttentionMe는 콘텐츠 속의 당신을 눈에 띄게 만드는 데 필요한 모든 도구를 제공합니다.

---

## 배경

마치 *Hype Boy*의 가사처럼, 관심의 중심에 서고 싶다는 '관종' 욕구를 느껴본 적 있으신가요?
> "You got me looking for attention."

**AttentionMe**와 함께라면 그 소망이 현실이 될 수 있습니다. 이 라이브러리는 영상과 이미지의 사전 처리(preprocessing)를 통해 사용자의 존재감을 극대화합니다. 제공하는 주요 기능은 다음과 같습니다:

- 사람 분리 (People segmentation)  
- 배경 제거 (Background removal)  
- 줌 인 (Dynamic zooming)  
- 대상 강조  

기억하실 사항: 이 프로젝트는 팀워크를 증진하고 **오픈 소스 소프트웨어** 개발 실습과 협업 경험을 쌓기 위해 대학생들에 의해 개발되었습니다.

---

## 기능

- **사람 분리 (People Segmentation)**: 영상이나 이미지에서 사람을 정확히 인식 및 분리합니다.  
- **배경 제거 (Background Removal)**: 원치 않는 배경을 제거하여 주제를 깔끔하게 분리합니다.  
- **줌 인 (Zoom In)**: 중요 영역을 자동으로 확대해 강조합니다.  
- **배경 밝기 조정 (Brightness Adjustment for Background)**: 원하는 가시성을 위해 이미지의 밝기를 미세 조정할 수 있습니다.  
- **대상 강조 (Target Pointing)**: 특정 영역이나 포인트에 집중하기 위해 포인트 및 크롭 기능을 제공합니다.  
- **맞춤형 워크플로우 (Customizable Workflow)**: 모듈형 설계로 통합 및 확장 작업이 용이합니다.

---

## 설치

작업을 시작하기 전에 다음 사항이 설치되어 있어야 합니다:  
- Python 3.8 이상  
- `Pillow`, `NumPy`, `OpenCV`와 같은 필수 라이브러리  

### 설치 단계

1. 저장소 클론하기:
   ```bash
   git clone https://github.com/Looking-4-Attention/AttentionMe.git
   cd AttentionMe
   ```
   
 2. 저장소 설치하기:
   ```bash
   pip install .
   ```
   
   ---

## 사용법

아래는 간단한 예제입니다. 더 자세한 사항은 저희 Organization 내 Sample Usage repository를 참고하시기 바랍니다. 아래는 사람 분리 기능을 시작하는 코드입니다:
```bash
from attentionme.segmentation import segment_people
from attentionme.remove_background import remove_background

# 입력 이미지 로드
input_file = "example.jpg"

# 사람 분리
segmented_image = segment_people(input_file)

# 배경 제거
final_image = remove_background(segmented_image)

# 결과 저장
final_image.save("output.jpg")
```

   ---

## 모듈 개요

-   **`segmentation.py`**: 이미지 및 영상에서 사람을 인식하고 분리하는 기능을 제공합니다.
-   **`remove_background.py`**: 배경 제거 기능으로 사람에 집중할 수 있습니다. 소위 말하는 '누끼' 기능.
-   **`zoom_in.py`**: 주요 영역인 사람이 있는 곳을 강조하기 위해 줌 인 하는 기능입니다.
-   **`crop.py`**: 원하는 크기 및 포커스 영역으로 쉽게 이미지를 자를 수 있습니다.
-   **`adjust_brightness.py`**: 배경의 밝기 조정을 통해 시각적 명확성을 높입니다.
-   **`pointing.py`**: 이미지나 영상에서 사람 옆에 화살표를 붙여 강조합니다.
-   **`enlargement.py`**: 이미지의 특정 부분을 확대하여 세부 사항을 확인할 수 있습니다.

   ---

## 유지보수자

이 프로젝트는 _Looking 4 Attention_ 팀장에 의해 유지보수되고 있습니다:

-   [Aenok Woo](https://github.com/wwwwje2008)

궁금한 점이나 의견이 있다면 언제든지 연락해 주세요.

   ---

## 기여

_Looking 4 Attention_의 팀원이자 메인 Contributor들:

-   [Namhoon Cho](https://github.com/Namhoon-Cho)
-   [Dami Lee](https://github.com/iamdami)
-   [Hyunsoo Kim](https://github.com/hyun1227)

저희 팀원이 아니어도, 아래 절차를 통해 프로젝트에 기여할 수 있습니다. 여러분의 기여를 환영합니다.:

1.  저장소를 포크합니다.
2.  새 브랜치를 만듭니다: `git checkout -b feature/your-feature-name`.
3.  변경 사항을 커밋합니다: `git commit -m 'Add feature'`.
4.  브랜치를 푸시합니다: `git push origin feature/your-feature-name`.
5.  풀 리퀘스트를 제출합니다.

   ---

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 세부 사항은 LICENSE 파일을 확인하세요.
