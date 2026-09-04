# References (links only - no PDFs redistributed)

## Datasets & challenges
* SPEED - Sharma et al., "SPEED: Next-Generation Dataset for Spacecraft Pose Estimation across Domain Gap" - https://arxiv.org/abs/1908.04227
* SPEED+ - Park et al., "SPEED+: Next-Generation Dataset for Spacecraft Pose Estimation across Domain Gap" - https://arxiv.org/abs/2110.03101
* Kelvin Pose Estimation Challenge (ECCV) - https://kelvins.esa.int/

## Baselines implemented here
* SPN - Sharma & D'Amico, "Pose Estimation for Non-Cooperative Rendezvous Using Neural Networks" - https://arxiv.org/abs/1906.09868
* PVNet - Peng et al., "PVNet: Pixel-wise Voting Network for 6DoF Pose Estimation" - https://arxiv.org/abs/1812.11788
* Bo Chen et al., "Satellite Pose Estimation with Deep Landmark Regression and Nonlinear Pose Refinement" - https://arxiv.org/abs/1908.11542 (`hrnet/`)
* YOLO - Ultralytics YOLOv11/v12 docs - https://docs.ultralytics.com/
* FastPose-ViT - Ancey et al., "FastPose-ViT: A Vision Transformer for Real-Time Spacecraft Pose Estimation" - https://arxiv.org/abs/2512.09792 (`fastpose/`)

## Backbones / helpers
* HRNet - Sun et al., "Deep High-Resolution Representation Learning" - https://arxiv.org/abs/1908.07919
* ViT - Dosovitskiy et al. - https://arxiv.org/abs/2010.11929
* Swin Transformer - Liu et al. - https://arxiv.org/abs/2103.14030
* SAM - Kirillov et al., "Segment Anything" - https://arxiv.org/abs/2304.02643 (used in `pvnet/segmentor.ipynb` to synthesize SPEED masks)
* EPnP - Lepetit et al. - classic PnP reference; OpenCV `solvePnP` used for final pose.

## Upstream code (referenced, not vendored)
* `zju3dv/pvnet` - https://github.com/zju3dv/pvnet
* `zju3dv/clean-pvnet` - https://github.com/zju3dv/clean-pvnet
* `PierreAncey/FastPose-ViT` - https://github.com/PierreAncey/FastPose-ViT/

## Slides
* `Presentation.pdf` in this folder - sanitized project summary (28 slides).
