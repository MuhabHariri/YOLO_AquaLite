<h2 align="center">This repository accompanies the paper <br><em>"YOLO-AquaLite: A Lightweight Fish Detection Model for Real-Time Underwater Applications"</em></h2>

---


## 🛠 Setup, Configuration, and Training

<br>
<a href="https://www.ultralytics.com/" target="_blank"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

This project is built on top of the Ultralytics YOLO framework, specifically **YOLOv11**.  
For environment setup, dataset preparation, and general usage instructions, please refer to the official [Ultralytics YOLO Documentation](https://docs.ultralytics.com/).

---

## 🎯 Weight Files

- **Weights files (trained on COCO dataset):**  
  The folder `Weights files (trained on COCO dataset)` includes YOLO_AquaLite model variants (`nano`, `small`, `medium`, `large`, and `xlarge`) trained on the COCO dataset.


- **Weights files (Fine-tuned on Fish dataset):**  
  The folder `Weights files (Fine_tuned on Fish dataset)` contains YOLO_AquaLite model variants that have been fine-tuned on the fish dataset described in our paper.



---

## 🚀 Training YOLO_AquaLite

To train a YOLO_AquaLite model variant, use the following command:

```bash
yolo detect train data=Dataset.yaml model=ultralytics/cfg/models/11/YOLO_AquaLite_Variant.yaml epochs=500 batch=32 imgsz=640
```
Replace `Variant` with the desired model size: `n` (nano), `s` (small), `m` (medium), `l` (large), or `xl` (xlarge).


