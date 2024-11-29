from setuptools import setup, find_packages

setup(
    name="attentionme",
    version="0.1.0",
    description="A library for person-focused image processing",
    author="Aenoc Woo, Dami Lee, Namhoon Cho, Hyunsoo Kim",
    packages=find_packages(),
    install_requires=[
        "torch",
        "torchvision",
        "opencv-python",
        "numpy"
    ],
)