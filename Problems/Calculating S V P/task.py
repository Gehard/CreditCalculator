# put your python code here
length = int(input())
width = int(input())
height = int(input())


def sum_calculations(a, b, c):
    # Sum of lengths of all edges
    return 4 * (a + b + c)


def surface_area(a, b, c):
    return 2 * ((a * b) + (b * c) + (a * c))


def volume(a, b, c):
    return a * b * c


print(sum_calculations(length, width, height))
print(surface_area(length, width, height))
print(volume(length, width, height))
