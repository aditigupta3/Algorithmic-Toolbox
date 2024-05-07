# Uses python3
import sys

def get_search_array(starts, ends):
    """
    Function to get a sorted array for:
    point, the number of segments which contain the point
    """
    end_pts_array = sorted([(start, 1) for start in starts] + [(end + 0.1, -1) for end in ends])
    search_array = [[end_pts_array[0][0], end_pts_array[0][1]]]
    total = end_pts_array[0][1]
    for elem in end_pts_array[1:]:
        total += elem[1]
        if elem[0] == search_array[-1][0]:            
            search_array[-1][1] = total
        else:
            search_array.append([elem[0], total])
    return search_array

def get_num_segments(search_array, point):
    """
    Function to count the number of segments for each point using binary search in the search array
    """
    start = 0
    end = len(search_array)-1
    while start <= end:
        if point < search_array[start][0]:
            return search_array[start-1][1]
        elif point >= search_array[end][0]:
            return search_array[end][1]
        
        mid = (start + end)//2
        if point == search_array[mid][0]:
            return search_array[mid][1]
        elif point < search_array[mid][0]:
            end = mid - 1
        elif start == end:
            return search_array[start][1]
        else:
            start = mid + 1
    return search_array[start][1]

def fast_count_segments(starts, ends, points):
    search_array = [(-float('inf'), 0)] + get_search_array(starts, ends) + [(float('inf'), 0)]
    results = list()
    for point in points:
        results.append(get_num_segments(search_array, point))
    return results

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
