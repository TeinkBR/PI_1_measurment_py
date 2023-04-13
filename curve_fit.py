import numpy as np
from scipy.optimize import curve_fit


import numpy as np
from scipy.optimize import curve_fit


def fit_curve(data):
    """
    Fits a curve to the given data using a simple polynomial model.

    Args:
        data: A 2D array where the first column is x values and the second column is y values.

    Returns:
        A 1D array of the polynomial coefficients.
    """
    x = data[:, 0]
    y = data[:, 1]

    def model_func(x, a, b, c):
        return a * x ** 2 + b * x + c

    popt, _ = curve_fit(model_func, x, y)
    return popt
