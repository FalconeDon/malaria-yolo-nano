
---

### 4. **[coco2yolo.py](ca://s?q=COCO_to_YOLO_conversion_script)**
```python
import json, os

coco_json = "nih_polys_coco.json"
labels_dir = "labels"
os.makedirs(labels_dir, exist_ok=True)

with open(coco_json, "r") as f:
    coco = json.load(f)

image_lookup = {img["id"]: img for img in coco["images"]}

for ann in coco["annotations"]:
    img_info = image_lookup[ann["image_id"]]
    img_w, img_h = img_info["width"], img_info["height"]
    x_min, y_min, w, h = ann["bbox"]

    x_center = (x_min + w/2) / img_w
    y_center = (y_min + h/2) / img_h
    w_norm, h_norm = w/img_w, h/img_h
    class_id = ann["category_id"] - 1

    label_file = os.path.join(labels_dir, os.path.splitext(img_info["file_name"])[0] + ".txt")
    with open(label_file, "a") as lf:
        lf.write(f"{class_id} {x_center:.6f} {y_center:.6f} {w_norm:.6f} {h_norm:.6f}\n")

print("Conversion complete! YOLO labels saved in:", labels_dir)
