# CS6643 Computer Vision Final Project
# Matthew Avallone, Siddharth Choudhary, Kshitija Patel

import numpy as np
import math

# Cosine Distance Metric
# Input: L2 normized pose vectors
# Output: Cosine distance between the two vectors
def cosine_distance(pose1, pose2):
	# Find the cosine similarity
	cossim = pose1.dot(np.transpose(pose2)) / (np.linalg.norm(pose1) * np.linalg.norm(pose2))

	# Find the cosine distance
	cosdist = (1 - cossim)

	return cosdist

# Weighted Distance Metric
# Input: L2 normized pose vectors, and confidence scores for each point in pose 1
# Output: Weighted distance between the two vectors
def weight_distance(pose1, pose2, conf1):
	# D(U,V) = (1 / sum(conf1)) * sum(conf1 * ||pose1 - pose2||)
	#		 = sum1 * sum2

	# Compute first summation
	sum1 = 1 / np.sum(conf1)

	# Compute second summation
	sum2 = 0
	for i in range(len(pose1)):
		conf_ind = math.floor(i / 2) # each index i has x and y that share same confidence score
		sum2 += conf1[conf_ind] * abs(pose1[i] - pose2[i])

	weighted_dist = sum1 * sum2

	return weighted_dist