import numpy as np


def convert_data(data):
    """
    Converts the given data by taking the square root of the second column.

    Args:
        data: A 2D array where the first column is x values and the second column is y values.

    Returns:
        None
    """
    data[:, 1] = np.sqrt(data[:, 1])
    np.savetxt("converted_data.txt", data)
