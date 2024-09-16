snacks_menu = {
    "Snack1": {'name': 'Chips' ,'price': '1.5$', 'ingredients': ['Potatoes', 'Oil', 'Salt']},
    "Snack2": {'name':'Popcorn' ,'price': '2$', 'ingredients': ['Corn', 'Oil', 'Salt']},
    "Snack3": {'name':'Cookies' ,'price': '3$', 'ingredients': ['Flour', 'Sugar', 'Eggs']}
}


def customeOrder_or_order(name : str , ingredients : str):
    snacks_menu[name.capitalize().strip()] = {'name':name,'ingredients': ingredients}



def cancel_order(name_in: str) -> bool:
    try:
        del snacks_menu[name_in.capitalize()]
        return True
    except KeyError:
        return False
    


def display_menu():
    for s1_key, s1_value in snacks_menu.items():
        print(s1_key)
        for s2_key, s2_value in s1_value.items():
            print(f"  {s2_key}: {s2_value}")