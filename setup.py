from setuptools import setup, find_packages

setup(
    name="attentionme",
    version="0.1.1",
    author="Aenoc Woo, Dami Lee, Namhoon Cho, Hyunsoo Kim",
    description="A library for person-focused image processing",
    long_description=open("README.md", encoding="UTF-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Looking-4-Attention/AttentionMe",
    packages=find_packages(),
    install_requires=[
        "torch",
        "torchvision",
        "opencv-python",
        "numpy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)