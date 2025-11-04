"""
YOLO_AquaLite Fine-Tuning Script 
Description:
    This script fine-tunes a YOLO_AquaLite model on a custom dataset.
    It supports multiple model sizes and uses the Ultralytics YOLO interface.

Usage:
    1. Place your pretrained weights in the folder (the default folder from the repository):
       "Weights files (trained on COCO dataset)/"
    2. Update the 'data_file' variable with the path to your dataset YAML.
    3. Run the script: python fine_tune_yolo.py
"""

import os
from ultralytics import YOLO

# -------------------------------
# User-defined Configuration
# -------------------------------

# Choose model size: options are "nano", "small", "medium", "large", "xlarge"
model_type = "nano"

# Path to your dataset YAML file
data_file = "path/to/fish_dataset.yaml"

# Directory where training results will be saved
project = "Yolo_AquaLite_fine_tune"

# Training hyperparameters
epochs = 200
patience = 200
image_size = 640
batch = 64
optimizer = 'SGD'  # Options: 'SGD', 'Adam', 'AdamW'

# -------------------------------
# Model Setup
# -------------------------------

# Mapping model types to pretrained weight filenames
model_file_map = {
    "nano": "YOLO_AquaLite_COCO_n.pt",
    "small": "YOLO_AquaLite_COCO_s.pt",
    "medium": "YOLO_AquaLite_COCO_m.pt",
    "large": "YOLO_AquaLite_COCO_l.pt",
    "xlarge": "YOLO_AquaLite_COCO_x.pt"
}

# Validate model_type
if model_type not in model_file_map:
    raise ValueError(f"Invalid model_type '{model_type}'. Choose from: {list(model_file_map.keys())}")

# Construct full path to the model weights
model_filename = model_file_map[model_type]
weights_dir = "Weights files (trained on COCO dataset)"
model_path = os.path.abspath(os.path.join(weights_dir, model_filename))

# Load the model
model = YOLO(model_path)

# -------------------------------
# Training
# -------------------------------

# Construct experiment name
experiment_name = f"fine_tune_{model_type}"

# Start training
model.train(
    data=data_file,
    epochs=epochs,
    patience=patience,
    imgsz=image_size,
    batch=batch,
    optimizer=optimizer,
    project=project,
    name=experiment_name
)
