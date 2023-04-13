import numpy as np
from curve_fit import fit_curve

class MockMeasurement:
    def get_feedback(self, current):
        feedback = np.sin(2 * np.pi * current) + np.random.normal(0, 0.1, size=len(current))
        return feedback
