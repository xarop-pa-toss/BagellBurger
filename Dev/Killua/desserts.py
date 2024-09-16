dessert_menu = {
    "Recipe1": {'name': 'Chocolate Cake', 'price': '5$', 'ingredients': ['Flour', 'Sugar', 'Eggs', 'Cocoa Powder', 'Milk']},
    "Recipe2": {'name': 'Strawberry Cheesecake', 'price': '6$', 'ingredients': ['Graham Cracker', 'Cream Cheese', 'Sugar', 'Eggs', 'Strawberries']},
    "Recipe3": {'name': 'Vanilla Ice Cream', 'price': '3$', 'ingredients': ['Cream', 'Sugar', 'Vanilla Extract']}
}

def custom_order_or_order(name: str, ingredients: str):
    dessert_menu[name.capitalize().strip()] = {'name': name, 'ingredients': ingredients}

def cancel_order(name_in: str) -> bool:
    try:
        dessert_menu.pop(name_in.capitalize())
        return True
    except KeyError:
        return False

def display_menu():
    for d1_key, d1_value in dessert_menu.items():
        print(d1_key)
        for d2_key, d2_value in d1_value.items():
            print(f"  {d2_key}: {d2_value}")