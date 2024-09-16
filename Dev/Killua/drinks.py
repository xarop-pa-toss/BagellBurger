drinks_menu = {
    "Drink1": {'name': 'Coffee' ,'price': '2$', 'ingredients': ['Water', 'Coffee Beans']},
    "Drink2": {'name':'Tea' ,'price': '2.5$', 'ingredients': ['Water', 'Tea Leaves']},
    "Drink3": {'name':'Soda' ,'price': '1.5$', 'ingredients': ['Carbonated Water', 'Flavoring']}
}

def customeOrder_or_order(name : str , ingredients : str):
    drinks_menu[name.capitalize().strip()] = {'name':name,'ingredients': ingredients}


def cancel_order(name_in: str) -> bool:
    try:
        del drinks_menu[name_in.capitalize()]
        return True
    except KeyError:
        return False
    

def display_menu():
    for d1_key, d1_value in drinks_menu.items():
        print(d1_key)
        for d2_key, d2_value in d1_value.items():
            print(f"  {d2_key}: {d2_value}")