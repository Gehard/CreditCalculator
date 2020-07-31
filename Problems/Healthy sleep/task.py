# recommended to sleep at least A hours per day
A = int(input())
# not sleep more than B hours.
B = int(input())
#  Ann sleeps H hours per day.
H = int(input())

if A <= B:
    if A <= H <= B:
        print("Normal")
    if H < A:
        print("Deficiency")
    elif H > B:
        print("Excess")