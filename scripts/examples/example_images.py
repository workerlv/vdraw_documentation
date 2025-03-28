import numpy as np
import cv2


def draw_3_predefined_figures():
    mask = np.zeros((1000, 1000), dtype=np.uint8)  # empty mask

    # figure 1
    points_raw_1 = np.array(
        [[100, 100], [400, 200], [600, 300], [300, 400], [200, 350]]
    )
    points_1 = points_raw_1.reshape((-1, 1, 2))
    cv2.fillPoly(mask, [points_1], color=(255, 255, 255))

    # figure 2
    points_raw_2 = np.array([[500, 150], [700, 250], [600, 150]])
    points_2 = points_raw_2.reshape((-1, 1, 2))
    cv2.fillPoly(mask, [points_2], color=(250, 250, 250))

    # figure 3
    points_raw_3 = np.array([[500, 500], [700, 600], [400, 900], [300, 850]])
    points_3 = points_raw_3.reshape((-1, 1, 2))
    cv2.fillPoly(mask, [points_3], color=(250, 250, 250))

    return mask
