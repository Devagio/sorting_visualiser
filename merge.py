import time


def merge_sort(data, draw, tick):
    merge_sort_alg(data, 0, len(data)-1, draw, tick)


def merge_sort_alg(data, left, right, draw, tick):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, draw, tick)
        merge_sort_alg(data, middle+1, right, draw, tick)
        merge(data, left, middle, right, draw, tick)


def merge(data, left, middle, right, draw, tick):
    n = len(data)
    draw(data, get_colour_array(n, left, middle, right))
    time.sleep(tick)

    left_part = data[left:middle+1]
    right_part = data[middle+1: right+1]

    left_index, right_index = 0, 0

    for data_index in range(left, right+1):
        if left_index < len(left_part) and right_index < len(right_part):
            if left_part[left_index] <= right_part[right_index]:
                data[data_index] = left_part[left_index]
                left_index = left_index + 1
            else:
                data[data_index] = right_part[right_index]
                right_index = right_index + 1
        elif left_index < len(left_part):
            data[data_index] = left_part[left_index]
            left_index = left_index + 1
        else:
            data[data_index] = right_part[right_index]
            right_index = right_index + 1

    draw(data, ["green" if left <= x <= right else "white" for x in range(n)])
    time.sleep(tick)


def get_colour_array(length, left, middle, right):
    colour_array = []

    for i in range(length):
        if left <= i <= right:
            if i <= middle:
                colour_array.append("yellow")
            else:
                colour_array.append("pink")
        else:
            colour_array.append("white")

    return colour_array
