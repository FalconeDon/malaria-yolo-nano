# malaria-yolo-nano
YOLO‑Nano training pipeline for malaria parasite detection using the NIH Thin Smear COCO dataset. Includes COCO → YOLO format conversion, dataset YAML configuration, and training scripts.
# Malaria Detection with YOLO-Nano

This repository provides a workflow to train YOLO-Nano on malaria thin blood smear images.
The dataset used is the NIH Thin Smear COCO dataset, which includes bounding box annotations
for parasitized and uninfected red blood cells, plus white blood cells.

## Features
- COCO → YOLO format conversion script
- Dataset YAML configuration for YOLO-Nano
- Training and evaluation pipeline
- Example results and metrics

## Dataset
Download NIH Thin Smear COCO dataset:
- Images (~965)
- Annotations (`nih_polys_coco.json`, `nih_points_coco.json`)

## Usage
1. Convert COCO annotations to YOLO format:
   ```bash
   python coco2yolo.py
