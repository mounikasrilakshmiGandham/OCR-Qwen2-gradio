---
title: OCR
emoji: 🏃
colorFrom: red
colorTo: green
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
short_description: OCR Text Extraction on images
---

# Qwen-2 2B OCR - Text Extraction and Keyword Search

This repository provides instructions on running the **Qwen-2 2B OCR** model for extracting text from images and performing keyword search on the extracted text. The application is designed to run locally using Gradio for quick testing and can also be deployed to Hugging Face for broader usage.

## Table of Contents
- [Environment Setup](#environment-setup)
- [Running the Application Locally with Gradio](#running-the-application-locally-with-gradio)
- [Deployment Process on Hugging Face](#deployment-process-on-hugging-face)

## Environment Setup

Follow these steps to set up your environment to run the application:

### Prerequisites

- Python 3.8 or higher
- Git
- Hugging Face Account (for deployment)
- A GPU-enabled environment (for faster inference, optional but recommended)

### Installation Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/jahnavi-andey/OCR-Qwen2-gradio
    cd OCR-Qwen2-gradio/OCR
    ```

2. Set up a virtual environment (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Install Hugging Face Transformers and Gradio:

    ```bash
    pip install transformers gradio
    ```

### Model Download

Make sure to download the **Qwen-2 2B OCR** model checkpoint from Hugging Face:

### Deployment

1. Create a hugging face space

    ```bash
      git init
      git add .
      git commit -m "Initial commit"
      git push
    ```

2. Access the Deployed App

    ```bash
    https://huggingface.co/spaces/jahnaviandey/OCR
  ```
