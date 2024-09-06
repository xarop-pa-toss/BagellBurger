def dictionary_browser():
    spanish_dict = {
        'la casa': 'The house',
        'el coche': 'The car',
        'la playa': 'The beach',
        'el libro': 'The book',
        'la musica': 'The music'
    }
    list = ['la casa',
            'el coche',
            'la playa',
            'el libro',
            'la musica']
    while True:
        action = input("\nWhat would you like to do? ( Type 'Browse' to browse, and 'Quit' to exit program):  ").lower()
        if action == "browse":

            browse = input("\nWhat would you like to browse? ").lower()
            if browse in spanish_dict:
                print("\n")
                
                print(spanish_dict[browse])
                      
            else:
                Eroor = print(f"Error. Word does not exist in the dictionary, the words in dict are {list} ")

        elif action == "quit":
            print("It was nice seeing you today :)!")
            break

dictionary_browser()
