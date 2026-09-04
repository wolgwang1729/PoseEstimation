# Spacecraft Pose Estimation (SPEED / SPEED+)

6-DoF pose estimation for the Tango spacecraft from single monocular images.
Course project **23CS250** - experiments with classical + learning baselines on the
[SPEED](https://arxiv.org/abs/1908.04227) and
[SPEED+](https://arxiv.org/abs/2110.03101) datasets (synthetic + real / domain-gap splits).

> This repo contains only original experiment code (Jupyter notebooks), training curves,
> and small YOLO weights. No partner / agency branding. No dataset images are committed -
> see [`data/README.md`](data/README.md).

## Methods explored

| Folder | What | Key result (see sub-README) |
|---|---|---|
| [`spn/`](spn/) | SPN (Sharma & D'Amico) - AlexNet/ResNet-50 + RPN + pose head, 1-pass and 2-pass (full-res crop), TPark baseline | 2-pass + ResNet-50 RPN: Mean IoU 0.84 synth / 0.77 real; ET-mag ~0.87 m synth |
| [`pvnet/`](pvnet/) | PVNet pixel-wise voting + `solvePnP` - ResNet/AlexNet, ViT, Swin backbones, 8 vs 11 keypoints, SPEED→SPEED+ fine-tune; SAM ViT-H mask generation (`segmentor.ipynb`) | 11-kpt ResNet + SPEED pretrain + SPEED+ fine-tune: Mean ER 7.5° real (best PVNet) |
| [`yolo/`](yolo/) | YOLO detection (YOLOv11n, 640px, 120 epochs) + YOLO→crop→ResNet-50 keypoint extension | Detector Mean IoU 0.951 synth / 0.912 real |
| [`fastpose/`](fastpose/) | FastPose direct-regression ViT (no PnP) + DETR-style variant, last model explored | See `fastpose/README.md` + implementation notes PDF |
| [`hrnet/`](hrnet/) | Deep landmark regression + nonlinear refinement (Bo Chen et al., HRNet-style) | See `training.logs` |
| [`docs/`](docs/) | Sanitized project presentation + paper links (no PDFs vendored) | - |

Each subfolder has its own `README.md` with per-notebook results tables
(ET = translation error, ER = rotation error, IoU = detection IoU).

## Repo layout

```text
PoseEstimation/
  README.md
  requirements.txt / environment.yml
  docs/
    Presentation.pdf   # sanitized, retitled "Satellite Pose Estimation"
    references.md              # papers + datasets + upstream repos (links only)
  data/
    README.md                  # SPEED/SPEED+ download + expected layout (no images in git)
    custom_dataset.yaml -> ../yolo/training_metrics/custom_dataset.yaml
  src/common/
    metrics.py                 # ET / ER / IoU helpers shared across notebooks
  hrnet/  spn/  pvnet/  yolo/  fastpose/  # notebooks + per-folder READMEs
  yolo/training_metrics/       # YOLO weights (*.pt), runs/detect/train curves + CSVs, results_preview/
  weights/README.md            # weight provenance + LFS note
```

Upstream vendor clones (`clean-pvnet`, `pvnet` originals) are **not** vendored;
see `docs/references.md` for links. Only SPEED-adapted experiment notebooks are kept.

## Quickstart

```bash
# 1. Clone
git clone <your-fork-url> PoseEstimation
cd PoseEstimation

# 2. Env (pick one)
pip install -r requirements.txt
# or
conda env create -f environment.yml
conda activate pose-est

# 3. Data (not in git - ~10 GB)
# Follow data/README.md to download SPEED + SPEED+,
# then arrange as data/speed/{images,labels} and data/yolo_dataset/{images,labels}
# YOLO config: yolo/training_metrics/custom_dataset.yaml (edit `path:` to your local root)

# 4. Open notebooks, e.g.
jupyter lab spn/tparkspn.ipynb
jupyter lab pvnet/pvnetonspeed11.ipynb
jupyter lab yolo/yolospeed.ipynb
jupyter lab hrnet/bochenkeypoint.ipynb
jupyter lab fastpose/fastpose.ipynb
```

Kaggle note: original runs used `/kaggle/input/...` paths and 2×GPU.
`custom_dataset.yaml` now defaults to `../../data/yolo_dataset` - override `path:` as needed.
All Kaggle datasets + notebooks linked in [`docs/kaggle.md`](docs/kaggle.md).

## Data

See [`data/README.md`](data/README.md). Expected:

```text
data/
  speed/images/{train,test_synthetic,test_real}  # 1920x1200 mono JPEGs
  speed/labels/*.json                            # quaternions + translations + camera
  yolo_dataset/{images,labels}/{train,val}
```

## Weights

* `yolo/training_metrics/yolo11n.pt` - pretrained detector init.
* `yolo/training_metrics/runs/detect/train/weights/{best,last}.pt` (~5 MB each) - trained YOLO runs.
* Committed directly (each < 100 MB GitHub limit). If they grow, enable Git LFS:
  `git lfs track "*.pt" "*.pth"` - see `weights/README.md` and `.gitattributes`.

## Metrics

Standard SPEED metrics, see `src/common/metrics.py`:

* `ET` / `ET-mag` (m), `ER` (deg) from predicted vs GT `t`/`q`,
* `IoU` for detection boxes.
* Pose via `cv2.solvePnP` (iterative / Levenberg–Marquardt) on voted keypoints.

## Docs

* [`docs/Presentation.pdf`](docs/Presentation.pdf) - 28-slide summary (metadata sanitized).
* [`docs/references.md`](docs/references.md) - SPEED, SPEED+, SPN, PVNet, HRNet/BoChen, ViT, Swin, YOLO, EPnP, SAM.

## Provenance

* Author: Mayank Yadav (23CS250).
* Source notebooks ran on Kaggle GPUs (2025). Desktop submission copy used as canonical source;
  HDD extras (vendor clones, admin/proposal PDFs, large slide decks, lectures)
  intentionally excluded from this public repo.
* No third-party PDFs are redistributed (copyright); only links.

## License

MIT - see [LICENSE](LICENSE).
