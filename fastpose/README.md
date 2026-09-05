# FastPose implementation files description

Direct-regression Vision Transformer for 6DoF spacecraft pose estimation, without PnP solvers.
This was the last model explored in this project, motivated by the inference cost of
iterative PnP-based pipelines (SPN, PVNet). The network regresses pose parameters directly
from cropped satellite images for fast inference.

Upstream work: FastPose-ViT by Pierre Victor Ancey et al.
- Code: https://github.com/PierreAncey/FastPose-ViT/
- Paper: FastPose-ViT - A Vision Transformer for Real-Time Spacecraft Pose Estimation (arXiv:2512.09792)

Only original experiment notebooks are committed here. The upstream implementation itself
is not vendored - see the link above. Third-party helper code received during development
(`fastpose.py`, `muon.py`) is also not committed.

## Contents

### [fastpose.ipynb](fastpose.ipynb)
Training notebook for the FastPose model on the SPEED dataset (9600 train / 2400 val split
from the 12000 synthetic images, plus eval on real images). Uses `/kaggle/input/speedsplit`
images and `/kaggle/input/mat-file` camera intrinsics and keypoints.

### [fastposetest.ipynb](fastposetest.ipynb)
Testing notebook for `fastpose.ipynb`. Evaluates translation error and orientation error
on the validation split and real images.

### [fastposedetr.ipynb](fastposedetr.ipynb)
Training notebook for the DETR-style detection/front-end variant paired with FastPose
regression. Uses the same SPEED splits and camera files as above.

### [fastposedetrtest.ipynb](fastposedetrtest.ipynb)
Testing notebook for `fastposedetr.ipynb`.

### [FastPose-implementation-notes.pdf](FastPose-implementation-notes.pdf)
Implementation report (6 pages, Jan 2026): dataset adaptation, detection integration,
geometric pose parameterization, and SPEED results analysis.

## Note on cell outputs

These notebooks are committed with cell outputs (downloaded from Kaggle with outputs
preserved), so results tables and plots render directly on GitHub. The trained
checkpoint is available as a kernel output (`kaggle kernels output wolgwang/fastpose`,
about 660 MB, too large for git) - see the implementation notes PDF for the
results analysis. The Kaggle versions are linked in [`../docs/kaggle.md`](../docs/kaggle.md).

## Data

Same SPEED setup as the rest of the repo - see [`../data/README.md`](../data/README.md)
and [`../docs/kaggle.md`](../docs/kaggle.md) for `wolgwang/speedsplit` and
`wolgwang/mat-file`. No dataset images are committed.

## Credits

- Author: 23/CS/250 MAYANKYADAV <mayankyadav_23cs250@dtu.ac.in>
- Upstream FastPose-ViT: Pierre Victor Ancey et al. (see links above)
