# YOLO Implementation files description

These Python Jupyter Notebooks are the implementation of the YOLO (You Only Look Once) object detection algorithm, specifically designed for satellite imagery. The notebooks cover various aspects of the model, including data preparation, training, and evaluation.

## [creatingdatasetforyolo.ipynb](creatingdatasetforyolo.ipynb)
This notebook contains the implementation of the data preparation pipeline for the YOLO model, including data augmentation and annotation generation.

## [yolospeed.ipynb](yolospeed.ipynb)
This notebook trains the YOLO model on the prepared dataset and evaluates its performance on a validation set. It includes steps for model configuration, training, and inference.

The training metrics and some visualisations of the model's prediction can be found in [training_metrics](training_metrics/runs/detect/train) folder. See also [results_preview](training_metrics/results_preview) for example predictions.

## [yolospeedtest.ipynb](yolospeedtest.ipynb)
This notebook is used for testing the trained YOLO model on new images. It includes the IoU (Intersection over Union) calculation to evaluate the model's predictions against ground truth annotations.

Results Summary:
| Metric           | SPEED synthetic test-set | SPEED real test-set |
|------------------|--------------------------|---------------------|
| Mean IoU (-)     | 0.9509                   | 0.9118              |
| Median IoU (-)   | 0.9648                   | 0.9104              |

## [yoloextend.ipynb](yoloextend.ipynb)
This notebook uses the YOLO detection model to predict the bounding boxes for satellite and then crop the image and then pass into Resnet50 backbone and some convolutional layers to predict keypoints.

## [yoloextendtest.ipynb](yoloextendtest.ipynb)
This notebook is used for testing the model of `yoloextend.ipynb`. It evaluates the performance of the model and calculates orientation error, translation error and IoU.

Results Summary:
| Metric               | SPEED synthetic test-set | SPEED real test-set |
|-----------------------|--------------------------|---------------------|
| Mean ET (m)           | [-0.006 0.093 6.007]     | [-0.282 0.035 4.846]|
| Mean ET mag (m)       | 6.0073                   | 4.8544              |
| Median ET mag (m)     | 0.868                    | 7.034               |
| Mean ER (deg)         | 43.8142                  | 130.8098            |
| Median ER (deg)       | 9.5766                   | 156.8809            |
