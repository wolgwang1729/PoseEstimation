"""Shared SPEED metrics: translation error (ET), rotation error (ER), IoU.

Pure-numpy helpers matching the definitions used across
spn/, pvnet/, yolo/ notebooks.
"""

import numpy as np


def translation_error(t_pred, t_gt):
    """Per-axis error vector and magnitude (meters).

    Args:
        t_pred, t_gt: (3,) array-likes in meters.
    Returns:
        (et_vec, et_mag)
    """
    t_pred = np.asarray(t_pred, dtype=float).reshape(3)
    t_gt = np.asarray(t_gt, dtype=float).reshape(3)
    et_vec = t_pred - t_gt
    return et_vec, float(np.linalg.norm(et_vec))


def quat_to_dcm(q):
    """Direction cosine matrix from scalar-first unit quaternion (w,x,y,z)."""
    q = np.asarray(q, dtype=float).reshape(4)
    q = q / np.linalg.norm(q)
    w, x, y, z = q
    return np.array([
        [1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
        [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
        [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)],
    ])


def rotation_error(q_pred, q_gt):
    """Angular error in degrees between two scalar-first quaternions."""
    r_pred = quat_to_dcm(q_pred)
    r_gt = quat_to_dcm(q_gt)
    r_rel = r_pred @ r_gt.T
    cos_angle = np.clip((np.trace(r_rel) - 1.0) / 2.0, -1.0, 1.0)
    return float(np.degrees(np.arccos(cos_angle)))


def iou_xyxy(box_a, box_b):
    """IoU for boxes in [x1, y1, x2, y2] format."""
    a = np.asarray(box_a, dtype=float).reshape(4)
    b = np.asarray(box_b, dtype=float).reshape(4)
    ix1, iy1 = max(a[0], b[0]), max(a[1], b[1])
    ix2, iy2 = min(a[2], b[2]), min(a[3], b[3])
    iw, ih = max(0.0, ix2 - ix1), max(0.0, iy2 - iy1)
    inter = iw * ih
    area_a = max(0.0, a[2] - a[0]) * max(0.0, a[3] - a[1])
    area_b = max(0.0, b[2] - b[0]) * max(0.0, b[3] - b[1])
    union = area_a + area_b - inter
    return float(inter / union) if union > 0 else 0.0
