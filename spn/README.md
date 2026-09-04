# Satellite Pose Estimation (SPN) Implementation files description

These Python Jupyter Notebooks are the implementation of Satellite Pose Estimation(SPN): "Pose Estimation for Non-Cooperative Rendezvous Using Neural Networks" by Sumant Sharma, Simone D'Amico. Paper available at https://arxiv.org/abs/1906.09868


## [spnrpn.ipynb](spnrpn.ipynb)
Object detection model for obtaining the bounding box of the satellite in the image. This model combines a classic AlexNet‐style convolutional backbone with a two‐stage object-detection head (RPN + Fast R-CNN) to predict tight bounding‐boxes around projected 3D keypoints.

# One Pass

## SPNV100
### [spnv100classes.ipynb](spnv100classes.ipynb)
SPN model implementation for obtaining the pose of a satellite in an image. The SPN model wraps a classic AlexNet‐style feature extractor, a RegionProposalNetwork, and ROI heads, then applies additional convolutional layers and parallel fully connected branches for classification (fc6–fc8) and regression (fc9–fc11). 

### [spnv100test.ipynb](spnv100test.ipynb)
Notebook for testing the spnv100classes.ipynb implementation. It calculates the orientation error, translation error, and the IoU of the predicted bounding box with respect to the ground truth.

Results Summary:

| Metric             | SPEED synthetic test-set     | SPEED real test-set          |
|--------------------|------------------------------|------------------------------|
| Mean IoU (-)       | 0.7813                       | 0.7024                       |
| Median IoU (-)     | 0.8419                       | 0.7301                       |
| Mean ET (m)        | [19.853, 11.423, -57.605]    | [5.661, 3.450, -16.131]      |
| Mean ET mag (m)    | 61.9918                      | 17.4402                      |
| Median ET mag (m)  | 53.908                       | 17.617                       |
| Mean ER (deg)      | 57.5221                      | 146.0217                     |
| Median ER (deg)    | 19.5200                      | 147.9434                     |

## Tpark 
### [tparkspn.ipynb](tparkspn.ipynb)
Implementation of SPN as done by Tpark(author of SPEED Plus baseline paper). This doesn't contain the object detection model, as the images are direclty cropped using the ground truth bounding boxes. 

### [tparktest.ipynb](tparktest.ipynb)
Notebook for testing the tparkspn.ipynb implementation. It calculates the orientation error, translation error, and the IoU of the predicted bounding box with respect to the ground truth.

Results Summary:

| Metric               | SPEED synthetic test-set     | SPEED real test-set          |
|----------------------|------------------------------|------------------------------|
| Mean IoU (-)         | 1.0000                       | 1.0000                       |
| Median IoU (-)       | 1.0000                       | 1.0000                       |
| Mean ET (m)          | [0.002 -0.002 1.004]         | [-0.035 0.082 0.582]         |
| Mean ET mag (m)      | 1.0037                       | 0.5892                       |
| Median ET mag (m)    | 0.864                        | 0.404                        |
| Mean ER (deg)        | 5.8606                       | 58.0922                      |
| Median ER (deg)      | 5.0405                       | 16.6590                      |

## SPNV200
### [spnv200classes.ipynb](spnv200classes.ipynb)
Same as spnv100classes.ipynb, but loads the convolution weights from the TPark trained model(from above) and some slight changes in hyperparameters.

### [spnv200test.ipynb](spnv200test.ipynb)
Jupyter Notebook for testing the spnv200classes.ipynb implementation. It calculates the orientation error, translation error, and the IoU of the predicted bounding box with respect to the ground truth.

Results Summary:

| Metric               | SPEED synthetic test-set     | SPEED real test-set          |
|----------------------|------------------------------|------------------------------|
| Mean IoU (-)         | 0.7658                       | 0.7039                       |
| Median IoU (-)       | 0.8328                       | 0.7437                       |
| Mean ET (m)          | [19.849 11.422 -57.580]      | [5.726 3.553 -16.359]        |
| Mean ET mag (m)      | 61.9666                      | 17.6921                      |
| Median ET mag (m)    | 54.466                       | 18.291                       |
| Mean ER (deg)        | 61.3299                      | 153.4373                     |
| Median ER (deg)      | 27.0932                      | 174.7363                     |

## SPNV300
### [spnv300classes.ipynb](spnv300classes.ipynb)
Similar to spnv200classes.ipynb, but the RPN model is also trained along with the classification and regression heads `loss = loss_class + 10.0*loss_regress + rpn_loss + roi_loss` and some hyperparameters are changed. 

### [spnv300test.ipynb](spnv300test.ipynb)
Jupyter Notebook for testing the spnv300classes.ipynb implementation. It calculates the orientation error, translation error, and the IoU of the predicted bounding box with respect to the ground truth.

Results Summary:

| Metric               | SPEED synthetic test-set     | SPEED real test-set          |
|----------------------|------------------------------|------------------------------|
| Mean IoU (-)         | 0.7238                       | 0.7042                       |
| Median IoU (-)       | 0.7734                       | 0.7068                       |
| Mean ET (m)          | [19.742 11.363 -57.231]      | [5.899 3.588 -16.906]        |
| Mean ET mag (m)      | 61.5972                      | 18.2612                      |
| Median ET mag (m)    | 53.810                       | 19.603                       |
| Mean ER (deg)        | 45.2899                      | 128.9108                     |
| Median ER (deg)      | 11.3803                      | 165.2983                     |

# 2 Pass

## SPNV400
### [spnv400classes.ipynb](spnv400classes.ipynb)
In this file, after obtaining the bounding box of the satellite in the image using the RPN model, the original (1920x1200) image is cropped and then again passed thrugh the SPN model. All the previous versions were directly cropping the initial transformed image (224x224) using the bounding box, which resulted in a loss of information. This version aims to retain more information by cropping the original image.

### [spnv400test.ipynb](spnv400test.ipynb)
Jupyter Notebook for testing the spnv400classes.ipynb implementation. It calculates the orientation error, translation error, and the IoU of the predicted bounding box with respect to the ground truth.

Results Summary:

| Metric               | SPEED synthetic test-set     | SPEED real test-set          |
|----------------------|------------------------------|------------------------------|
| Mean IoU (-)         | 0.7658                       | 0.7039                       |
| Median IoU (-)       | 0.8328                       | 0.7437                       |
| Mean ET (m)          | [-0.001 0.001 0.963]         | [0.082 0.151 0.554]          |
| Mean ET mag (m)      | 0.9628                       | 0.5796                       |
| Median ET mag (m)    | 0.838                        | 0.461                        |
| Mean ER (deg)        | 20.5574                      | 88.6952                      |
| Median ER (deg)      | 6.2255                       | 112.7025                     |

## SPN Advanced
### [spnrpnadvanced.ipynb](spnrpnadvanced.ipynb)
This is the improved version of the `spnrpn.ipynb`. In this resnt50 backbone is used instead of the AlexNet backbone. 

### [spnrpnadvancedtestfull.ipynb](spnrpnadvancedtestfull.ipynb)
This is the testing notebook for the model which uses the SPN advanced RPN and the same SPN model as in the `spnv400classes.ipynb`. It calculates the orientation error, translation error, and the IoU of the predicted bounding box with respect to the ground truth.

Results Summary:

| Metric               | SPEED synthetic test-set     | SPEED real test-set          |
|----------------------|------------------------------|------------------------------|
| Mean IoU (-)         | 0.8407                       | 0.7659                       |
| Median IoU (-)       | 0.8734                       | 0.8000                       |
| Mean ET (m)          | [0.005 -0.004 0.867]         | [0.011 0.109 0.592]          |
| Mean ET mag (m)      | 0.8668                       | 0.6019                       |
| Median ET mag (m)    | 0.809                        | 0.551                        |
| Mean ER (deg)        | 14.7462                      | 78.8189                      |
| Median ER (deg)      | 6.0831                       | 68.2189                      |