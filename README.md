# Milkgaurd-AI
An intelligent milk sample testing and AI based monitoring system

### Technical Introduction

The MilkGuard AI system uses a Raspberry Pi 3B+ integrated with a Raspberry Pi camera module to capture milk sample images for quality analysis. The camera is connected to the Raspberry Pi through a dedicated camera ribbon cable interface.

A 5V white LED light is positioned near the camera to provide sufficient and consistent illumination during image acquisition. The LED lighting helps reduce variations caused by surrounding light conditions and improves the visibility of the milk sample during image capture.

The LED light receives power from a suitable 5V supply, while the camera captures images inside the optical chamber. The Raspberry Pi stores the captured images on its microSD card and transmits them wirelessly to the Flutter-based mobile application through a Wi-Fi connection.

The mobile application performs image preprocessing, colour feature extraction and machine learning-based milk quality classification. This arrangement provides a compact and cost-effective image acquisition system for the MilkGuard AI project.
