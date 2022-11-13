import time


def selection_sort(data, draw, tick):
    n = len(data)
    for i in range(n-1):
        min_val = data[i]
        min_index = i
        for j in range(i+1, n):
            draw(data, get_colour_array(n, i, j, min_index))
            time.sleep(tick)
            if data[j] < min_val:
                draw(data, get_colour_array(n, i, j, min_index, True))
                time.sleep(tick)
                min_val = data[j]
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]


def get_colour_array(data_len, i, j, min_index, is_swapping=False):
    colour_array = []
    for k in range(data_len):
        if k < i:
            colour_array.append("green")
        elif k == i:
            colour_array.append("yellow")
        elif k == min_index:
            colour_array.append("blue")
        elif k == j:
            colour_array.append("pink")
        else:
            colour_array.append("gray")

        if is_swapping:
            if k == j or k == min_index:
                colour_array[k] = "red"
    return colour_array
