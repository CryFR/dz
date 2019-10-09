import random
import numpy as np
fat_boi = np.random.randint(-100, 100, 1000)


def negative(array):
    array = tuple(array)
    smallest = list(array).index(min(array))
    biggest = list(array).index(max(array))
    if smallest < biggest:
        neg_nos = len([num for num in array[smallest:biggest + 1] if num < 0])
    else:
        neg_nos = len([num for num in array[biggest:smallest + 1] if num < 0])
    print(neg_nos)


negative(fat_boi)
