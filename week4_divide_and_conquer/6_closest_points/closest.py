#Uses python3
import sys
import math

def distance(c1, c2):
    return (c1[0]-c2[0])**2 + (c1[1]-c2[1])**2

def mindist(coords):
    """
    Function used to get the minimum distance between any 2 points using
    divide and conquer technique.
    """
    if len(coords) == 1:
        return None
    elif len(coords) == 2:
        return distance(coords[0], coords[1])
    mid = len(coords)//2
    d1 = mindist(coords[:mid]) # Get the minimum distance in 1st half
    d2 = mindist(coords[mid:]) # Get the minimum distance in 2nd half
    d = None
    if d1 is not None:
        d = d1
    if d2 is not None:
        if d is None:
            d = d2
        elif d2 < d:
            d = d2
    # The strip in the middle may have even closer points.
    mid_val = (coords[mid-1][0] + coords[mid][0])/2
    strip = sorted([c for c in coords if (mid_val - d) <= c[0] <= (mid_val + d)], key=lambda x: (x[1], x[0]))
    for i in range(len(strip)):
        for j in range(i+1, min(i+8, len(strip))):
            d = min(d, distance(coords[i], coords[j]))
    return d

def minimum_distance(x, y):
    #write your code here
    coords = sorted([(xi, yi) for xi, yi in zip(x, y)])
    return math.sqrt(mindist(coords))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
