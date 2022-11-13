import time


def partition(data, head, tail, draw, tick):
    border = head
    pivot = data[tail]
    n = len(data)

    draw(data, get_colour_array(n, head, tail, border, border))
    time.sleep(tick)

    for j in range(head, tail):
        if data[j] < pivot:
            draw(data, get_colour_array(n, head, tail, border, j, True))
            time.sleep(tick)

            data[border], data[j] = data[j], data[border]
            border = border + 1

        draw(data, get_colour_array(n, head, tail, border, j))
        time.sleep(tick)

    draw(data, get_colour_array(n, head, tail, border, tail, True))
    time.sleep(tick)

    data[border], data[tail] = data[tail], data[border]
    return border


def quick_sort(data, head, tail, draw, tick):
    if head < tail:
        partition_index = partition(data, head, tail, draw, tick)
        quick_sort(data, head, partition_index-1, draw, tick)
        quick_sort(data, partition_index+1, tail, draw, tick)


def get_colour_array(data_len, head, tail, border, current_index, is_swapping=False):
    colour_array = []
    for i in range(data_len):
        if head <= i <= tail:
            colour_array.append("gray")
        else:
            colour_array.append("white")

        if i == tail:
            colour_array[i] = "blue"
        elif i == border:
            colour_array[i] = "red"
        elif i == current_index:
            colour_array[i] = "green"

        if is_swapping:
            if i == border or i == current_index:
                colour_array[i] = "yellow"

    return colour_array
