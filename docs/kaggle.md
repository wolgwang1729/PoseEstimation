# Kaggle links - datasets & notebooks

Kaggle profile: https://www.kaggle.com/wolgwang

> Datasets are **not** in git. Use these links for download / repro.
> In-notebook `/kaggle/input/<slug>` maps to `https://www.kaggle.com/datasets/wolgwang/<slug>`
> (or kernel outputs for trained weights - same slug under `/code/`).

## Datasets (`wolgwang/<slug>` → `kaggle.com/datasets/wolgwang/<slug>`)

| Dataset | Size / note | Used by |
|---|---|---|
| [speed](https://www.kaggle.com/datasets/wolgwang/speed) | 17.0 GB, SPEED+ | all - main SPEED+ source |
| [speedv1](https://www.kaggle.com/datasets/wolgwang/speedv1) | 4.9 GB, SPEEDv1 | early SPEED runs |
| [speedsplit](https://www.kaggle.com/datasets/wolgwang/speedsplit) | 3.9 GB, train/val/real splits + `train.json/val.json/real.json` | all notebooks (`speedsplit/speed/images/trainval`, `.../real`) |
| [mat-file](https://www.kaggle.com/datasets/wolgwang/mat-file) | `camera.json`, `tangoPoints.mat`, `attitudeClasses.mat` | all - intrinsics + 3D keypoints + attitude classes |
| [bvlc-alexnet-zeiler-and-fergus](https://www.kaggle.com/datasets/wolgwang/bvlc-alexnet-zeiler-and-fergus) | `bvlc_alexnet.npy` pretrained | `spn/`, `pvnet/` AlexNet backbones |
| [speeddatasetforyolo](https://www.kaggle.com/datasets/wolgwang/speeddatasetforyolo) | 187 MB, `yolo_dataset/{images,labels}` | `yolo/yolospeed.ipynb` (`/kaggle/input/speeddatasetforyolo/yolo_dataset`) |
| [yolo12n](https://www.kaggle.com/datasets/wolgwang/yolo12n) | 5 MB, `yolo12n.pt` init | `yolo/` training |
| [yolov12nspeed](https://www.kaggle.com/datasets/wolgwang/yolov12nspeed) | 18.5 MB, trained YOLO on SPEED | `yolo/yoloextend*.ipynb` (`yolospeed/runs/detect/train/weights/best.pt`) |
| [samfacebook](https://www.kaggle.com/datasets/wolgwang/samfacebook) | 2.4 GB, `sam_vit_h_4b8939.pth` | `pvnet/segmentor.ipynb` mask synthesis |
| [samvit-b](https://www.kaggle.com/datasets/wolgwang/samvit-b) | 347 MB, SAM ViT-B | mask ablations |
| [speedmasks](https://www.kaggle.com/datasets/wolgwang/speedmasks) / [speedsammasks](https://www.kaggle.com/datasets/wolgwang/speedsammasks) | SAM-generated SPEED masks | `pvnet/` training (`mask_dir`) |
| [masksspeedplus](https://www.kaggle.com/datasets/wolgwang/masksspeedplus) + [masksspeedplus1](https://www.kaggle.com/datasets/wolgwang/masksspeedplus1) [2](https://www.kaggle.com/datasets/wolgwang/masksspeedplus2) [3](https://www.kaggle.com/datasets/wolgwang/masksspeedplus3) [4](https://www.kaggle.com/datasets/wolgwang/masksspeedplus4) | SPEED+ masks splits | `pvnetonspeed11speedplus`, fine-tune notebook |
| [bochenjsons](https://www.kaggle.com/datasets/wolgwang/bochenjsons) / [mergebochenjsons](https://www.kaggle.com/code/wolgwang/mergebochenjsons) (`merged.json`) | BoChen JSON labels | `hrnet/bochenkeypoint.ipynb` |
| [trained-hrrnet](https://www.kaggle.com/datasets/wolgwang/trained-hrrnet) | 315 MB, trained HRNet | `hrnet/` eval |
| [speedresnet50feats](https://www.kaggle.com/datasets/wolgwang/speedresnet50feats) | 252 MB, ResNet-50 feats | `myapproachresnet50` |
| [maesmakk](https://www.kaggle.com/datasets/wolgwang/maesmakk) / [maepretrainedbase](https://www.kaggle.com/datasets/wolgwang/maepretrainedbase) | MAE pretrained | ViT/Swin ablations |
| [ransacsrc](https://www.kaggle.com/datasets/wolgwang/ransacsrc) | RANSAC/PnP src | `pvnet/` pose head |
| [linemod-pre-processed](https://www.kaggle.com/datasets/wolgwang/linemod-pre-processed) | 9 GB, Linemod (non-SPEED) | reference only, not used here |

Full list: `kaggle datasets list --mine` (34 datasets; FER/dog-vs-cat/shakespeare etc. omitted here as unrelated).

## Notebooks (`wolgwang/<slug>` → `kaggle.com/code/wolgwang/<slug>`)

### `hrnet/` ↔
* [bochenkeypoint](https://www.kaggle.com/code/wolgwang/bochenkeypoint) ↔ `hrnet/bochenkeypoint.ipynb`
* [bochenkeypointtest](https://www.kaggle.com/code/wolgwang/bochenkeypointtest), [fixbochenkeypoint](https://www.kaggle.com/code/wolgwang/fixbochenkeypoint), [where-is-the-issue-bochen](https://www.kaggle.com/code/wolgwang/where-is-the-issue-bochen), [mergebochenjsons](https://www.kaggle.com/code/wolgwang/mergebochenjsons), [myapproachresnet50](https://www.kaggle.com/code/wolgwang/myapproachresnet50) (+`test`), [creatingfeatsresnet50](https://www.kaggle.com/code/wolgwang/creatingfeatsresnet50)

### `spn/` ↔
* [tparkspn](https://www.kaggle.com/code/wolgwang/tparkspn) ↔ `spn/tparkspn.ipynb`, [tparktest](https://www.kaggle.com/code/wolgwang/tparktest) ↔ `spn/tparktest.ipynb`
* Train/test pairs in repo map 1:1 to similarly named kernels where published; early iterations: [spnmodel](https://www.kaggle.com/code/wolgwang/spnmodel), [spnv6rpn](https://www.kaggle.com/code/wolgwang/spnv6rpn), [spnv6classes](https://www.kaggle.com/code/wolgwang/spnv6classes), [spntest](https://www.kaggle.com/code/wolgwang/spntest), [spntestv100](https://www.kaggle.com/code/wolgwang/spntestv100), [spnrpnv100](https://www.kaggle.com/code/wolgwang/spnrpnv100), [rpnv01](https://www.kaggle.com/code/wolgwang/rpnv01), [rpnv02](https://www.kaggle.com/code/wolgwang/rpnv02), [speedv02](https://www.kaggle.com/code/wolgwang/speedv02), [speedtestv02](https://www.kaggle.com/code/wolgwang/speedtestv02), [demospnpreprocess](https://www.kaggle.com/code/wolgwang/demospnpreprocess)

### `pvnet/` ↔
* [pvnetv00](https://www.kaggle.com/code/wolgwang/pvnetv00), [pvnetv01](https://www.kaggle.com/code/wolgwang/pvnetv01) (early)
* [pvnetonspeed8](https://www.kaggle.com/code/wolgwang/pvnetonspeed8) ↔ `pvnet/pvnet8spn*.ipynb` family, [pvnetonspeed8test](https://www.kaggle.com/code/wolgwang/pvnetonspeed8test)
* [pvnetonspeed11](https://www.kaggle.com/code/wolgwang/pvnetonspeed11) ↔ `pvnet/pvnetonspeed11.ipynb`, [pvnetonspeed11test](https://www.kaggle.com/code/wolgwang/pvnetonspeed11test)
* [pvnetonspeed11speedplus](https://www.kaggle.com/code/wolgwang/pvnetonspeed11speedplus), [pvnetonspeed11trainedonspeedandfinetunedonspeedplu](https://www.kaggle.com/code/wolgwang/pvnetonspeed11trainedonspeedandfinetunedonspeedplu)
* [vitposes](https://www.kaggle.com/code/wolgwang/vitposes) / [vitpose-b](https://www.kaggle.com/code/wolgwang/vitpose-b) / [vitpose-test](https://www.kaggle.com/code/wolgwang/vitpose-test) ↔ `pvnet/vitpose*.ipynb`
* [swinpvnet](https://www.kaggle.com/code/wolgwang/swinpvnet) / [swinpvnettest](https://www.kaggle.com/code/wolgwang/swinpvnettest) ↔ `pvnet/swinpvnet*.ipynb`
* [swinseg](https://www.kaggle.com/code/wolgwang/swinseg) / [swinsegtest](https://www.kaggle.com/code/wolgwang/swinsegtest) ↔ `pvnet/swinseg*.ipynb`
* [segmentor](https://www.kaggle.com/code/wolgwang/segmentor) ↔ `pvnet/segmentor.ipynb`, plus [segmentornaive](https://www.kaggle.com/code/wolgwang/segmentornaive), [segmentorspeedplus3](https://www.kaggle.com/code/wolgwang/segmentorspeedplus3), [segmentorspeedplus4](https://www.kaggle.com/code/wolgwang/segmentorspeedplus4), [joinspeedplusmask](https://www.kaggle.com/code/wolgwang/joinspeedplusmask), [speedsegmentation](https://www.kaggle.com/code/wolgwang/speedsegmentation), [demopvnetpreprocess](https://www.kaggle.com/code/wolgwang/demopvnetpreprocess)

### `yolo/` ↔
* [creatingdatasetforyolo](https://www.kaggle.com/code/wolgwang/creatingdatasetforyolo) ↔ `yolo/creatingdatasetforyolo.ipynb`
* [yolospeed](https://www.kaggle.com/code/wolgwang/yolospeed) ↔ `yolo/yolospeed.ipynb`, [yolospeedtest](https://www.kaggle.com/code/wolgwang/yolospeedtest)
* [yoloextend](https://www.kaggle.com/code/wolgwang/yoloextend) ↔ `yolo/yoloextend.ipynb`, [yoloextendtest](https://www.kaggle.com/code/wolgwang/yoloextendtest)

### `fastpose/` ↔
* [fastpose](https://www.kaggle.com/code/wolgwang/fastpose) ↔ `fastpose/fastpose.ipynb`
* [fastposetest](https://www.kaggle.com/code/wolgwang/fastposetest) ↔ `fastpose/fastposetest.ipynb`
* [fastposedetr](https://www.kaggle.com/code/wolgwang/fastposedetr) ↔ `fastpose/fastposedetr.ipynb`
* [fastposedetrtest](https://www.kaggle.com/code/wolgwang/fastposedetrtest) ↔ `fastpose/fastposedetrtest.ipynb`

### Other (not in this repo, for context)
* [mtfnet](https://www.kaggle.com/code/wolgwang/mtfnet) - excluded from public repo (external snippet).

## How to use

```bash
# CLI (kaggle.json already configured on this machine)
kaggle datasets download wolgwang/speedsplit -p data/ --unzip
kaggle datasets download wolgwang/mat-file -p data/ --unzip
kaggle kernels pull wolgwang/yolospeed -p /tmp/yolospeed
```

To add a new link here, paste the Kaggle URL - slug pattern is stable:
`https://www.kaggle.com/datasets/wolgwang/<dataset>` and `https://www.kaggle.com/code/wolgwang/<notebook>`.
