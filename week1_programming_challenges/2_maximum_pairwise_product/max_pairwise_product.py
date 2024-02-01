# python3


def max_pairwise_product(numbers):
    """
    Since we are only interested in the maximum pairwise product and all numbers are positive,
    we just need to get the top 2 integers and multiply them to get the result.
    :param numbers:
    :return:
    """
    if numbers[0] > numbers[1]:
        small = numbers[1]
        large = numbers[0]
    else:
        large = numbers[1]
        small = numbers[0]
    for elem in numbers[2:]:
        if (elem > small) and (elem <= large):
            small = elem
        elif elem > large:
            small = large
            large = elem
    return small*large


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
