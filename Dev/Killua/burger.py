burger_menu = {
    "Recipe1": {'name': 'Cheese Burger' ,'price': '4$', 'ingredients': ['Ground Beef', 'Cheese', 'Beef Burger', 'Lettuce', 'Tomato', 'Onion', 'Pickles']},
    "Recipe2": {'name':'Bacon Burger','price': '3.5$', 'ingredient':['Ground Beef', 'Tomato', 'Onion','Lettuce','Pickle', 'Bacon']},
    "Recipe3" : {'name':'Chicken Burger', 'price':'2.5$', 'ingredient':['Ground Chicken', 'Lettuce', 'Tomato', 'Onion', 'Pickles']}
}

def customeOrder_or_order(name : str , ingredients : str):
    burger_menu[name.capitalize().strip()] = {'name':name,'ingredients': ingredients}


def cancel_order(name_in: str) -> bool:
    try:
        cancel_order.pop(name_in.capitalize())
        return True
    except KeyError:
        return False
    


def display_menu():
    for d1_key, d1_value in burger_menu.items():
        print(d1_key)
        for d2_key, d2_value in d1_value.items():
            print(f"  {d2_key}: {d2_value}")
