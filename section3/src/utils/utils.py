"""
Various utility methods in this module
"""
import numpy as np

def med_reshape(image, new_shape):
    """
    This function reshapes 3D data to new dimension padding with zeros
    and leaving the content in the top-left corner

    Arguments:
        image {array} -- 3D array of pixel data
        new_shape {3-tuple} -- expected output shape

    Returns:
        3D array of desired shape, padded with zeroes
    """

    reshaped_image = np.zeros(new_shape)

    # TASK: write your original image into the reshaped image
    x_length, y_length, z_length = image.shape
    reshaped_image[:x_length, :y_length, :z_length] = image

    return reshaped_image