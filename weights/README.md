# Weights

* `../yolo/training_metrics/yolo11n.pt` (~5.4 MB) - pretrained detector initialization.
* `../yolo/training_metrics/runs/detect/train/weights/best.pt` + `last.pt` (~5.3 MB each) - trained YOLO runs (120 epochs, imgsz 640).

All files are under GitHub's 100 MB/file limit, so they are committed directly
(no Git LFS required). `.gitattributes` contains commented LFS rules if you add
larger checkpoints later:

```bash
git lfs install
git lfs track "*.pt" "*.pth" "*.onnx"
```
