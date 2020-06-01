# Pose Estimation and Matching

## Team Members
Matthew Avallone, Siddharth Choudhary, and Kshitija Patel

## Overview
The goal of this project is to perform human pose estimation and matching. Given two images, a reference image and a test image, human poses would be detected using keypoints and compared to determine the similarity between them. These key points can be plotted as a 2D stick-figure. The reference image would be overlayed on the test image to find the similarity between the poses which are depicted in both of the images. 

![alt text](https://github.com/mattavallone/pose-matching/blob/master/pose-match.png "Sample Pose Matching")

For further details, please refer to the [project report](https://github.com/mattavallone/pose-matching/blob/master/report/CV%20Project%20Report.pdf).

## Libraries Used
* OpenCV
* Numpy
* Matplotlib
* Pandas

## Links to the prototxt and pre-trained model of the MPII Pose dataset:

* [Prototxt](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/models/pose/mpi/pose_deploy_linevec_faster_4_stages.prototxt)

* [Caffe Model](http://posefs1.perception.cs.cmu.edu/OpenPose/models/pose/mpi/pose_iter_160000.caffemodel)
