weather = [
    'Sunny',
    'Cloudy',
    'Rainy'
]

S = input()


def solve():
    index = weather.index(S)
    next_index = 0 if index == 2 else index + 1

    return weather[next_index]


print(solve())
