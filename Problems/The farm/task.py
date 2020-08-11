price_of_chicken = 23
price_of_goat = 678
price_of_pig = 1296
price_of_cow = 3848
price_of_sheep = 6769

cash = abs(int(input()))

if cash < 23:
    print("None")

elif price_of_chicken <= cash < price_of_goat:
    print("1 chicken" if cash // price_of_chicken == 1 else f"{cash // price_of_chicken} chickens")

elif price_of_goat <= cash < price_of_pig:
    print("1 goat" if cash // price_of_goat == 1 else f"{cash // price_of_goat} goats")

elif price_of_pig <= cash < price_of_cow:
    print("1 pig" if cash // price_of_pig == 1 else f"{cash // price_of_pig} pigs")

elif price_of_cow <= cash < price_of_sheep:
    print("1 cow" if cash // price_of_cow == 1 else f"{cash // price_of_cow} cows")

elif cash >= price_of_sheep:
    print("1 sheep" if cash // price_of_sheep == 1 else f"{cash // price_of_sheep} sheep")

"""
ALTERNATIVELY

def find_animal(money):
    animal = {'Sheep': 6769, 'Cow': 3848, 'Pig': 1296, 'Goat': 678, 'Chicken': 23}
    for k, v in animal.items():
        if v <= money:
            if int(money / v) > 1 and k != 'Sheep': 
                suffix = 's'
            else: 
                suffix = ''
            return f'{int(money/v)} {k.lower()+suffix}'
    return None
mo = int(input())        
print(find_animal(mo))

"""