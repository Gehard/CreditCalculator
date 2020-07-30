foods = {
    'pizza': 'Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy',
    'salad': 'Caesar salad, Green salad, Tuna salad, Fruit salad',
    'soup': 'Chicken soup, Ramen, Tomato soup, Mushroom cream soup'
}
food = input()
if food not in foods:
    print("Sorry, we don't have it in the menu")
else:
    print(foods[food])
