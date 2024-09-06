# 2D dictionary.
# Data structures like Lists, Dicts, etc do not need only numbers or strings inside. You can chain them together to create multi dimensional objects
# In this case, every key in the books_dict dictionary is itself a dictionary with genre, page count and cover art
books_dict = {
    "Dune": { "genre": "sci-fi", "page_count": 250, "cover_art": "desert scene"},
    "Lord Of The Rings": { "genre": "fantasy", "page_count": 300, "cover_art": "middle earth"},
    "Neuromancer": { "genre": "cyberpunk", "page_count": 150, "cover_art": "futuristic city"},
}

# In the function Parameters we use Annotations in front of each parameter.
# Parameter names are completely optional and don't influence the function call. The names given are used as variables inside the function only
# This does not enforce the types when the function is called BUT it shows on the code editor, serving as guidance to the programmer
# To add a default value, aka a value that if ommited in the function call will default to this value, use the syntax some_parameter="default value"
def edit_or_add_book(name_in: str, genre_in: str, page_count_in: int, cover_art_in: str="N/D"):
    books_dict[name_in.capitalize().strip()] = {
        "genre": genre_in,
        "page_count": page_count_in,
        "cover_art": cover_art_in
    }

# This function uses a Return Annotation that is written as a "-> datatype" at the end of a function declaration.
# Again, it doesn't enforce anything but provides guidance to the programmer so they know what data type the function should return.
def remove_book(name_in: str) -> bool:
    try:
        books_dict.pop(name_in.capitalize())
        return True
    except KeyError:
        return False

# This function runs through the main dictionary, gets its keys (str) and values (dict) and runs  through those too, printing to terminal
# A visual example to help understand:
# outer_dict = {
#     "outer_key1": {
#         "inner_key1": "inner_value1",
#         "inner_key2": "inner_value2",
#     }
# }
# 
# The only thing that isn't shown here is outer_value1 and inner_dict which are equivalent. 
# The value to the key "outer_key1" is the inner dictionary itself.
def display_books():
    for d1_key, d1_value in books_dict.items():
        print(d1_key)
        for d2_key, d2_value in d1_value.items():
            print(f"  {d2_key}: {d2_value}")

# Put a breakpoint at the start of the loop and go line by line with F11 while looking at the stack on the sidebar
# You will see the first for loop touching each key-value-pair (kvp) of the outer_dict which are given by the .items() function.
# You will then see the second for loop going into each of those kvp and going through each kvp inside it.
# Go slow, and use the debugger to see step by step