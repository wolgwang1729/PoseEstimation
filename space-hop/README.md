# SPACE-HOP implementation files description

Spacecraft 6-DoF pose estimation via masking-based embedding-predictive (JEPA)
pretraining of a ViT-B/16 encoder, then pose estimation as classification over a
Hopf-fibration SO(3) anchor grid with Lie-algebra offset refinement and a normalized
translation head. No PnP solvers - a single feedforward pass maps cropped satellite
images directly to pose parameters.

Upstream work: SPACE-HOP by Dutta et al., AI4Space Workshop @ CVPR 2026.
- Paper (open access): https://openaccess.thecvf.com/content/CVPR2026W/AI4Space/papers/Dutta_SPACE-HOP_Spacecraft_6-DoF_Pose_Estimation_using_Embedding-Predictive_Pretraining_and_Hopf_CVPRW_2026_paper.pdf
- Reviews/discussion: https://openreview.net/forum?id=t9LTeubtto
- Code: promised by the authors ("to be released soon", Apr 2026) - not vendored here.
Only original experiment notebooks are committed here; the paper itself is linked,
not vendored (per repo policy: no third-party PDFs).

## Contents

### [spacehop-pretrain.ipynb](spacehop-pretrain.ipynb)
Training notebook for the JEPA encoder on the SPEED dataset (7680 train / 1920 val
split from the 9600 trainval images, seed 42). Keypoint-anchored masking selects
target blocks around projected Tango keypoints; a context encoder, EMA target encoder
(0.996 -> 1.0), and predictor transformer are trained with Smooth-L1 loss in latent
space. Uses `/kaggle/input/speedsplit` images and `/kaggle/input/mat-file` camera
intrinsics and keypoints.

Final epoch (30/30): train Smooth-L1 0.1885, val Smooth-L1 0.1687.

### [spacehop-finetune.ipynb](spacehop-finetune.ipynb)
Training notebook for the SPACE-HOP pose heads on the same SPEED split, initialized
from the pretrained encoder (`jepa_best.pth` attached as input, auto-found). The `[CLS]`
token feeds three linear heads: normalized translation, 2048-way Hopf anchor classifier,
and Kx3 offset refinement (`Ltrans + Lcoarse + 10·Lfine`, 2 frozen warmup epochs).

Final epoch (30/30): loss 1.9842 (trans 0.0063, coarse 1.2056, fine 0.0772),
val ET 0.2734 m, ER 3.428 deg.

### [spacehop-test.ipynb](spacehop-test.ipynb)
Testing notebook for `spacehop-finetune.ipynb`. Loads `spacehop_best.pth` (auto-found),
rebuilds the anchor grid from the checkpoint, and evaluates translation error and
orientation error on the validation split and real images. Also saves error histograms
and best/median/worst GT-vs-predicted keypoint overlays.

Results Summary:

| Metric            | SPEED synthetic test-set | SPEED real test-set |
|-------------------|--------------------------|---------------------|
| Mean ET (m)       | [-0.001 -0.002 -0.028]   | [-0.043 -0.079 0.011] |
| Mean ET mag (m)   | 0.2734                   | 0.1586              |
| Median ET mag (m) | 0.1944                   | 0.1561              |
| Mean ER (deg)     | 3.4281                   | 8.0738              |
| Median ER (deg)   | 2.9924                   | 7.5561              |

Note: the real set in this mirror is only 5 images, so the real column is indicative
rather than statistically meaningful. The paper itself reports on SPEED+ (different
dataset), where SPACE-HOP-224 reaches ET 0.302 m / ER 9.015 deg on Lightbox.

## Note on cell outputs

These notebooks are committed with cell outputs (downloaded from Kaggle with outputs
preserved), so results tables and plots render directly on GitHub. The trained
checkpoints (`jepa_best.pth`, `spacehop_best.pth`, each several hundred MB, too large
for git) are available as kernel outputs - see the implementation notebooks for the
saving/attach procedure. The Kaggle versions are linked in [`../docs/kaggle.md`](../docs/kaggle.md).

## Data

Same SPEED setup as the rest of the repo - see [`../data/README.md`](../data/README.md)
and [`../docs/kaggle.md`](../docs/kaggle.md) for `wolgwang/speedsplit` and
`wolgwang/mat-file`. No dataset images are committed.

## Credits

- Author: Mayank Yadav
- Upstream SPACE-HOP paper: anonymous CVPR 2026 submission (see references in the PDF)
