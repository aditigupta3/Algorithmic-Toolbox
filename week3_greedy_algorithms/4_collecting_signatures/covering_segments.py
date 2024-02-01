# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    """
    We first sort all segments by their start point.
    Then, for each segment, we check if they can be contained in one of the segments.
    :param segments:
    :return:
    """
    segments.sort(key=lambda x: x.start)
    all_points = [(segments[0].start, segments[0].end)]
    for seg in segments[1:]:
        # If there is some overlap between the old segment and the new one
        if seg.start <= all_points[-1][1]:
            # If the end point of the old segment is contained in the new segment
            if seg.end >= all_points[-1][1]:
                continue
            # If the new segment closes before the old one
            else:
                all_points[-1] = (all_points[-1][0], seg.end)
        # If there is no overlap between the old segment and the new one.
        else:
            all_points.append((seg.start, seg.end))
    return [seg[1] for seg in all_points]


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
