# -*- coding: utf-8 -*-
import numpy as np
import cv2
import os
import sys

# Allow helpers package to be found when this module is imported standalone
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from helpers.dataloader import load_image, get_data_path
from scipy.ndimage import convolve1d

SPHINX_IMAGE = "2560px-Great_Sphinx_of_Giza_-_20080716a.jpg"

def read_image():
    """Load and preprocess the Sphinx image: scale by 0.5 and convert to greyscale."""
    image_path = get_data_path(SPHINX_IMAGE)
    return load_image(image_path, scale_factor=2, as_gray=True)

# Skeleton Code will generate a 1D Gaussian Kernel for given sigma.
# You need to implement 2D convolution as efficiently as possible.
class GaussianFilt:
    def __init__(self, sigma):
        self.sigma = sigma

    def gauss_kernel(self):
        """Generate a normalised 1D Gaussian kernel of appropriate size for self.sigma.

        Returns:
            gauss_1d (ndarray): Shape (k_size, 1) — column vector kernel.
        """
        # Work out the necessary kernel size and range to generate the Gaussian over.
        '''raise NotImplementedError("Implement this method")'''
        k_size = int(6 * self.sigma + 1)
        half = k_size // 2
        x = np.arange(-half, half + 1)
        gauss_1d = (1.0 / (self.sigma * np.sqrt(2 * np.pi))) * np.exp(-(x ** 2) / (2 * self.sigma ** 2))
        gauss_1d = gauss_1d / gauss_1d.sum()
        gauss_1d = np.expand_dims(gauss_1d, axis=1)
        return gauss_1d
    
    def my_conv_method(self, image):
        """Perform separable 2D Gaussian convolution via two 1D matrix-multiply passes.

        Args:
            image (ndarray): 2D greyscale image (H, W), any numeric dtype.

        Returns:
            conv_img (ndarray): Blurred image of same shape, dtype uint8.
        """
        '''raise NotImplementedError("Implement this method")'''
        gauss_1d=self.gauss_kernel()
        kernel = gauss_1d.squeeze()
        vertical=convolve1d(image,kernel, axis=0, mode="reflect")
        horizontal = convolve1d(vertical, kernel, axis=1, mode="reflect")
        con_image = np.clip(horizontal, 0, 255).astype(np.uint8)
        return con_image
        
