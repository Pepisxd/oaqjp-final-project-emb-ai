"""Packaging configuration for the EmotionDetection library."""

from setuptools import find_packages, setup

setup(
    name='EmotionDetection',
    version='1.0',
    description='Emotion detection powered by the Watson NLP library',
    packages=find_packages(include=['EmotionDetection']),
    install_requires=['requests'],
)
