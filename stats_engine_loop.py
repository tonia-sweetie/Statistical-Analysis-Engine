import numpy as np
summ = 0

def mean(arr):
    sum(arr) / len(arr)
    return arr

def median(arr):
    arr = np.sort(arr)
    n = len(arr) -1
    
    if n%2 != 0:
        return arr[n // 2]
    else:
        return (arr[n - 1 // 2] + arr[n // 2]) / 2
    
    
    
def variance(arr):
    for i in arr:
        variance = (i - mean) ** 2
        summ += variance
    return summ

def standard_deviation(arr):
    for i in arr:
        variance = (i - mean) ** 2
        summ += variance
    return summ * 0.5
    
def minimum (arr):
    for i in arr:
        if i < summ:
            summ = i
    return summ

def maximum (arr):
    for i in arr:
        if i > summ:
            summ = i
    return summ