<h2 align="center">This repository accompanies the paper <br><em>"YOLO-AquaLite: A Lightweight Fish Detection Model for Real-Time Underwater Applications"</em></h2>

---


## 🛠 Setup, Configuration, and Training

<br>
<a href="https://www.ultralytics.com/" target="_blank"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

This project is built on top of the Ultralytics YOLO framework, specifically **YOLOv11**.  
For environment setup, dataset preparation, and general usage instructions, please refer to the official [Ultralytics YOLO Documentation](https://docs.ultralytics.com/).

---
## 📌 What is YOLO_AquaLite?
<br>
YOLO_AquaLite is an object detection model based on the YOLOv11 architecture, designed with a focus on computational efficiency and lightweight deployment.
It introduces several architectural enhancements to optimize performance:

🔄 Replaces the initial backbone layers with a pre-trained encoder

🧱 Utilizes Dilated DeepResNet Blocks instead of traditional C3k2 blocks

🧭 Incorporates a Spatial-to-Channel Projection block into the pipeline

These improvements make YOLO_AquaLite significantly lighter than the original YOLOv11, with lower model size, reduced computational cost, and improved latency, while maintaining competitive detection accuracy.

---

## 🎯 Weight Files

- **Weights files (trained on COCO dataset):**  
  The folder `Weights files (trained on COCO dataset)` includes YOLO_AquaLite model variants ([nano](https://github.com/MuhabHariri/YOLO_AquaLite/raw/main/Weights%20files%20(trained%20on%20COCO%20dataset)/YOLO_AquaLite_COCO_n.pt), [small](https://github.com/MuhabHariri/YOLO_AquaLite/raw/main/Weights%20files%20(trained%20on%20COCO%20dataset)/YOLO_AquaLite_COCO_s.pt), [medium](https://github.com/MuhabHariri/YOLO_AquaLite/raw/main/Weights%20files%20(trained%20on%20COCO%20dataset)/YOLO_AquaLite_COCO_m.pt), [large](https://github.com/MuhabHariri/YOLO_AquaLite/raw/main/Weights%20files%20(trained%20on%20COCO%20dataset)/YOLO_AquaLite_COCO_l.pt), and [xlarge](https://github.com/MuhabHariri/YOLO_AquaLite/raw/main/Weights%20files%20(trained%20on%20COCO%20dataset)/YOLO_AquaLite_COCO_xl.pt)) trained on the COCO dataset.




- **Weights files (Fine-tuned on Fish dataset):**  
  The folder `Weights files (Fine_tuned on Fish dataset)` contains YOLO_AquaLite model variants ([nano](https://github.com/MuhabHariri/YOLO_AquaLite/raw/main/Weights%20files%20(Fine_tuned%20on%20Fish%20dataset)/YOLO_AquaLite_n.pt), [small](https://github.com/MuhabHariri/YOLO_AquaLite/raw/main/Weights%20files%20(Fine_tuned%20on%20Fish%20dataset)/YOLO_AquaLite_s.pt), [medium](https://github.com/MuhabHariri/YOLO_AquaLite/raw/main/Weights%20files%20(Fine_tuned%20on%20Fish%20dataset)/YOLO_AquaLite_m.pt), [large](https://github.com/MuhabHariri/YOLO_AquaLite/raw/main/Weights%20files%20(Fine_tuned%20on%20Fish%20dataset)/YOLO_AquaLite_l.pt), and [xlarge](https://github.com/MuhabHariri/YOLO_AquaLite/raw/main/Weights%20files%20(Fine_tuned%20on%20Fish%20dataset)/YOLO_AquaLite_xl.pt)) that have been fine-tuned on the fish dataset described in our paper.




---

## 🚀 Training YOLO_AquaLite

To train a YOLO_AquaLite model variant, use the following command:

```bash
yolo detect train data=Dataset.yaml model=ultralytics/cfg/models/11/YOLO_AquaLite_Variant.yaml epochs=500 batch=32 imgsz=640
```
Replace `Variant` with the desired model size: `n` (nano), `s` (small), `m` (medium), `l` (large), or `xl` (xlarge).


