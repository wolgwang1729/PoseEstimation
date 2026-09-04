# Pixel-wise Voting Network(PVNet) Implementation files description

These Python Jupyter Notebooks are the implementation of PVNet (Pixel-wise Voting Network) for 6DoF pose estimation as described in "PVNet: Pixel-wise Voting Network for 6DoF Pose Estimation" (https://arxiv.org/abs/1812.11788). This notebook trains the network to predict per-pixel voting fields for object keypoints and estimates the pose using PnP.

## Segmentor
### [segmentor.ipynb](segmentor.ipynb)
The PVnet model requires masks for training but the original SPEED dataset does not provide them. This notebook uses keypoints to generate masks for the SPEED dataset using Segment Anything Model (SAM) Vit-H model.

## PVNet8SPN
### [pvnet8spn.ipynb](pvnet8spn.ipynb)
This notebook implements the PVNet technique but uses Alexnet backbone instead of ResNet. It is designed to work with the SPEED dataset and trains the model to predict pixel-wise voting fields for object keypoints.

### [pvnet8spntest.ipynb](pvnet8spntest.ipynb)
Testing notebook for pvnet8spn.ipynb. It evaluates the performance of the PVNet model with Alexnet backbone on the SPEED dataset, measuring orientation error, translation error.

Results Summary:

| Metric             | SPEED synthetic test-set     | SPEED real test-set       |
|--------------------|------------------------------|---------------------------|
| Mean ET (m)        | [0.017 0.002 10.627]         | [-0.094 0.116 2.200]      |
| Mean ET mag (m)    | 10.6268                      | 2.2046                    |
| Median ET mag (m)  | 9.435                        | 3.617                     |
| Mean ER (deg)      | 112.2541                     | 110.4000                  |
| Median ER (deg)    | 126.4520                     | 112.4111                  |

## PVNet on SPEED8
### [pvnetonspeed8.ipynb](pvnetonspeed8.ipynb)
This notebook is similar to pvnet8spn.ipynb but uses a ResNet backbone. 


### [pvnetonspeed8test.ipynb](pvnetonspeed8test.ipynb)
Testing notebook for pvnetonspeed8.ipynb. It evaluates the performance of the PVNet model with ResNet backbone on the SPEED dataset, measuring orientation error, translation error.

Results Summary:

| Metric             | SPEED synthetic test-set     | SPEED real test-set       |
|--------------------|------------------------------|---------------------------|
| Mean ET (m)        | [0.013 -0.016 7.263]         | [-0.157 0.092 2.605]      |
| Mean ET mag (m)    | 7.2634                       | 2.6110                    |
| Median ET mag (m)  | 1.085                        | 3.037                     |
| Mean ER (deg)      | 65.9998                      | 123.1995                  |
| Median ER (deg)    | 16.1034                      | 148.0221                  |

## PVNet on SPEED11
### [pvnetonspeed11.ipynb](pvnetonspeed11.ipynb)
This notebook is similar to pvnetonspeed8.ipynb but uses 11 keypoints instead of 8. 

### [pvnetonspeed11test.ipynb](pvnetonspeed11test.ipynb)
Testing notebook for pvnetonspeed11.ipynb. It evaluates the performance of the PVNet model with ResNet backbone on the SPEED dataset with 11 keypoints, measuring orientation error, translation error.

Results Summary:

| Metric             | SPEED synthetic test-set     | SPEED real test-set       |
|--------------------|------------------------------|---------------------------|
| Mean ET (m)        | [0.071 -0.050 9.845]         | [-0.070 -0.128 0.956]     |
| Mean ET mag (m)    | 9.8451                       | 0.9675                    |
| Median ET mag (m)  | 8.647                        | 0.723                     |
| Mean ER (deg)      | 45.6121                      | 13.3741                   |
| Median ER (deg)    | 12.0449                      | 12.2134                   |

### [pvnetonspeed11speedplus.ipynb](pvnetonspeed11speedplus.ipynb)
This notebook is similar to pvnetonspeed11test.ipynb but the model is trained on SPEED+ dataset. 

Results Summary:

| Metric               | SPEED synthetic test-set     | SPEED real test-set          |
|----------------------|------------------------------|------------------------------|
| Mean ET (m)          | [0.060 -0.040 10.034]        | [-0.099 -0.029 2.202]        |
| Mean ET mag (m)      | 10.0344                      | 2.2044                       |
| Median ET mag (m)    | 8.790                        | 1.720                        |
| Mean ER (deg)        | 54.6117                      | 46.5790                      |
| Median ER (deg)      | 15.3201                      | 13.3476                      |

### [pvnetonspeed11trainedonspeedandfinetunedonspeedplus.ipynb](pvnetonspeed11trainedonspeedandfinetunedonspeedplus.ipynb)
This notebook is similar to pvnetonspeed11test.ipynb but the model is trained on SPEED dataset and then fine-tuned on SPEED+ dataset.

Results Summary:

| Metric               | SPEED synthetic test-set     | SPEED real test-set          |
|----------------------|------------------------------|------------------------------|
| Mean ET (m)          | [0.067 -0.069 9.418]         | [-0.150 -0.116 1.277]        |
| Mean ET mag (m)      | 9.4189                       | 1.2906                       |
| Median ET mag (m)    | 8.151                        | 1.461                        |
| Mean ER (deg)        | 30.9939                      | 7.4885                       |
| Median ER (deg)      | 10.7517                      | 7.9267                       |

## ViTPose

### [vitpose.ipynb](vitpose.ipynb)
This notebook uses the ViT as backbone for the PVNet model. 

### [vitposetest.ipynb](vitposetest.ipynb)
Testing notebook for vitpose.ipynb. It evaluates the performance of the PVNet model with ViT backbone on the SPEED dataset, measuring orientation error, translation error. The results are not good probably because ViT is not suitable for dense prediction tasks like segmentation.

Results Summary:
+----------------------+------------------------------+------------------------------+
| Metric               | SPEED synthetic test-set     | SPEED real test-set          |
+----------------------+------------------------------+------------------------------+
| Mean ET (m)          | [-0.004 -0.013 10.378]       | [-0.127 0.113 4.333]         |
| Mean ET mag (m)      | 10.3777                      | 4.3367                       |
| Median ET mag (m)    | 8.783                        | 4.150                        |
| Mean ER (deg)        | 117.0704                     | 148.1685                     |
| Median ER (deg)      | 124.6000                     | 142.4881                     |

## SWIN PVNet

### [swinpvnet.ipynb](swinpvnet.ipynb)
This notebook uses the Swin Transformer as backbone for the PVNet model.

### [swinpvnettest.ipynb](swinpvnettest.ipynb)
Testing notebook for swinpvnet.ipynb. It evaluates the performance of the PVNet model with Swin Transformer backbone on the SPEED dataset, measuring orientation error, translation error.

Results Summary:
| Metric               | SPEED synthetic test-set     | SPEED real test-set          |
|----------------------|------------------------------|------------------------------|
| Mean ET (m)          | [0.003 -0.003 10.851]        | [-0.306 0.060 3.730]         |
| Mean ET mag (m)      | 10.8510                      | 3.7427                       |
| Median ET mag (m)    | 9.669                        | 4.224                        |
| Mean ER (deg)        | 87.3644                      | 93.3250                      |
| Median ER (deg)      | 41.6233                      | 115.9585                     |

## SWIN Seg

### [swinseg.ipynb](swinseg.ipynb)
This notebook uses the Swin Transformer as backbone for the segmentation task and uses the original SWIN Segmentation decoder.

### [swinsegtest.ipynb](swinsegtest.ipynb)
Testing notebook for swinseg.ipynb. It evaluates the performance of the Swin Transformer segmentation model on the SPEED dataset, measuring orientation error, translation error.

Results Summary:
| Metric               | SPEED synthetic test-set     | SPEED real test-set          |
|----------------------|------------------------------|------------------------------|
| Mean ET (m)          | [0.011 -0.010 10.267]        | [-0.318 0.263 2.861]         |
| Mean ET mag (m)      | 10.2669                      | 2.8905                       |
| Median ET mag (m)    | 9.146                        | 3.062                        |
| Mean ER (deg)        | 68.0183                      | 136.6333                     |
| Median ER (deg)      | 24.7395                      | 122.0569                     |