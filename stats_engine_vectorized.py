import numpy as np
summ = 0

def mean(arr):
    return np.mean(arr)

def median(arr):
    return np.median(arr, axis = 1)

def variance(arr):
    return summ + ((arr[arr - arr.mean()]) ** 2)

def standard_deviation(arr):
    return (summ + ((arr[arr - arr.mean()]) ** 2)) ** 0.5
    
def minimum (arr):
    return arr[arr < summ]

def maximum (arr):
    return  arr[arr > summ]