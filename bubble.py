import time


def bubble_sort(data, draw, tick):
    n = len(data)
    for _ in range(n-1):
        for j in range(n-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                draw(data, ["yellow" if x == j or x == j+1 else "red" for x in range(n)])
                time.sleep(tick)
            else:
                draw(data, ["green" if x == j or x == j + 1 else "red" for x in range(n)])
                time.sleep(tick)
