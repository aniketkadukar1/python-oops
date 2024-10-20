"""Program to create fibonacci series"""

def fibonacci_series(num):
    series = [0, 1]
    for i in range(2, num):
        series.append(series[i-2] + series[i-1])
    return series

print(fibonacci_series(6))