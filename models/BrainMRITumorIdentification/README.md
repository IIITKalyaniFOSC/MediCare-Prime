# Brain MRI Tumor Identification

## Overview
The goal of the model is to identify Tumors in Brain MRI scan images. Every year more than 1 Million people are diagnosed with Brain Tumor around the globe. Early identification of tumor increases the survival rate in patients.

## Dataset
The training data contains 3929 Brain MRI Scan Images. <br>
2556 images belong to non Tumor Category. <br>
1373 images belog to Tumor Category. <br>
Dataset can be downloaded from - https://www.kaggle.com/mateuszbuda/lgg-mri-segmentation <br>
The dataset is split into Train and Test sets. The test set consists of 576 (15%) images.

## Training the Model
Instead of training the model from Scratch, I have utilized the power of Transfer Learning. <br>
The infamous ResNet50 (Imagenet) model is taken as a basemodel and the weights are freezed. <br>
The output from the ResNet50 model is flattened and passed over to two Dense layers with 256 neurons. <br>
The final layer (output layer) consists of 2 neurons (1 each for Tumor and Non Tumor). <br>
15% images from training set are taken for Validation and the model that performs best on Validation set is saved for future predictions. 

## Result on Test Set
The model performs exceedingly well and is able to identify Tumors with an accuracy of 95% with a good balance between Precision and Recall.