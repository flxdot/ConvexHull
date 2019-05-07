import numpy as np

def findHull(x, y):
    """Call to find the the data points representing the vertex of the enclosing convex hull.

    :param x: (mandatory, numpy.array or list) The x positions of the data
    :param y: (mandatroy, numpy.array or list) The y positions of the data
    :return: (numpy.array, numpy.array) tuple (x,y) of numpy arrays holding the coordinates
    """

    if isinstance(x, list):
        x = np.array(x)
    elif not isinstance(x, np.ndarray):
        raise TypeError('Coordinates have to be provided as list or numpy.ndarray')
    if isinstance(y, list):
        y = np.array(y)
    elif not isinstance(y, np.ndarray):
        raise TypeError('Coordinates have to be provided as list or numpy.ndarray')

    # init the data of the hull
    x_hull = np.array([np.min(x), np.max(x)])
    y_hull = np.array([np.min(y), np.max(y)])

    # get the max and min values and draw the first line
    p1 = np.array([x_hull[0], y_hull[0]])
    p2 = np.array([x_hull[1], y_hull[1]])

    #
    idx = get_max_dist(p1, p2, x, y)
    x_hull = np.append(x_hull, x[idx])
    y_hull = np.append(y_hull, y[idx])

    # return the found points
    return np.array(x_hull), np.array(y_hull)

def get_max_dist(p1, p2, x, y):
    """Returns the index of the x and y coordinates which have the greatest distance from the line spanned by
    the point p1 and p2

    :param p1: (mandatory, numpy.ndarray)
    :param p2: (mandatory, numpy.ndarray)
    :param x: (mandatory, numpy.ndarray)
    :param y: (mandatory, numpy.ndarray)
    :return: (int) index of the point with the greatest distance
    """

    rtn_idx = 0
    dist = np.zeros_like(x)
    for idx in range(len(x)):
        p0 = np.array([x[idx], y[idx]])

        # calculate the current distance
        dist[idx] = np.linalg.norm(np.cross((p0 - p1), (p0 - p2))) / np.linalg.norm(p1 - p2)

    return np.argmax(dist)
