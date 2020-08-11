no_of_army = int(input())

if no_of_army < 1:
    print("no army")
elif 1 <= no_of_army <= 9:
    print("few")
elif 10 <= no_of_army <= 49:
    print("pack")
elif 50 <= no_of_army <= 499:
    print("horde")
elif 500 <= no_of_army <= 999:
    print("swarm")
elif no_of_army >= 1000:
    print(" legion")
