# Lab Report — Lab 01: Efficient Separable Gaussian Convolution

*Fill in each section below. Be specific — name the actual methods/parameters you used, since
your report is graded alongside your code.*

## Overview

_1 sentence: What was the goal of this lab?_

The goal of this assignmnet is to apply two 1D convolution passes instead one full 2d convolution.

## Implementation

_1-2 sentences: Briefly describe the steps you performed to implment efficient convolution._
I generated normalized gaussian kernel of size (6*sigma +1) and reshaped it as a column vector. Then applied 1d convolution vertically with axis 0 and then horizontally (axis 1). Then converted the data type to uint8.
## Results

_1-2 sentences: How well did your method perform vs the baseline in the pytests? ._
The implementation passed all 10 tests. Convolution time was 0.0458 seconds, which was less than the threshold of 0.5123 seconds. Two separate 1D convolutions were faster than performing one direct 2D convolution.