# Task 1 - Creating the menu items

## Explanation
There are many different data types but we are going to use Dictionaries here.

Dictionaries in Python work like real life ones. You have a word you want to look up the meaning of, so you look for the word (key) and get it's meaning (value).
Important characteristics:
- Keys must be unique, meaning you cannot have duplicate keys. You will never find the same exact word twice in the same IRL dictionary, same here.
- You can have the same value on different keys.
- Dictionary items/entries are always comprised of key-value-pairs, sometimes refered to as *kvp*. You can give a key a null/empty value, but it has to be there.

They are similar in syntax to Lists, but instead of using [ ] you use { }. Since you must use key-value-pairs, the syntax is _key: value_
The advantage over lists is that you can use the keys directly to find their values. With Lists you have to run through the whole List object and look around for something, usually with a _if x in y_ loop which is inneficient and you have no way of binding things together.
With Dictionaries you can just ask it "Give me your color/type/price/etc if you have it."

```python
# Creating a new Dictionary compared to a List.
# Remember, Dictionaries are created with { }, but you access their contents with [ ].
list = [
    "item 1",
    45,
    some_variable,
    this_function_returns_some_value() ]

dict = {
    "type": "garden hose",
    "color": item_color,
    "cost": 500
    "weight": calculate_weight_from_length_meters(13)
    "material": None }

# Getting a value from a known key.
if dict["color"] is not None:
    # This would write whatever the value of item_color is if it has a value (aka is not None).
    print(f"The color for the item {dict["type"]} is dict["color"]) 
else:
    # If the item_color variable is empty (it's value is None) then we tell that to the user.
    print(f"The color is not defined for the item {dict["type"]}")
```

### Useful default Dictionary functions
Like most other data structures you can add, remove and change the kvp's inside the Dictionary, but you can also loop through the keys and values.
```python
dict = {
    "key1": "value1"
    "key2": "value2"
}

# Changing a value - access its key and change the value directly
dict["key1"] = "value100"
dict["key2"] = None
# Adding a kvp - like changing a value, but you access a key that doesnt exist yet
dict["key50"] = "value50"
# Removing a kvp - you use the .pop() function.
dict.pop("key1")

# Getting keys and values
# .keys() and .values() will return all keys and values into a list you can run through. .items() does the same for both at the same time.
# Using the unchanged dictionary as an example
for k in dict.keys():
    print(k)
for v in dict.values():
    print(v)
for k, v in dict.items():
    print(k)
    print(v)
```

## Specification
The app needs to have items of all kinds for the user to select. But we also want to allow a degree of customization, not everyone wants onions on their burger!
- Create and use a file in your folder with the corresponding name:
   Bagell - desserts.py
   Killua - hamburguers.py
   Insanity - drinks.py
   Pluto - extras.py
- Do not include a main function, as this file will be imported as a module onto another file later on.

Your program __must__:
1 - Have at least one Dictionary that contains relevant food items. The Dictionary can have any keys you find relevant to the category that was assigned to you, but the following must exist: "name" and "price".
2 - Have functions that allow __creating and deleting items__ (kvp's) as well as __editing individual keys and values__ in that Dictionary.
    These functions must return True if successful, or False if unsuccessful. We will learn proper error handling later.

The objective is to create a module (your .py file) that will be used by the larger application to control the items on the BagellBurger menu.
You are free to include whatever you want and use whichever technique you like, as long as you meet the requirements above.
I recommend looking into the bonus section below as well.

# GOOD LUCK 😁


### BONUS - Multi-dimensional Dictionaries
```python
#The Values don't have to be strings or ints. You can actually have Lists or other Dictionaries as the value in a kvp.
items_dict = {
    "gardening_hose": {"color": "green", "length": 30, "price": 25.99},
    "chain_fence": {"color": "silver", "length": 100, "price": 120.50},
}
#To access these inner dictionaries you have do what is called a "nested" loop. One for the outer dictionary, and another for the inner dictionaries.
for item, details in items_dict.items():
    print(f"Item: {item}")
    for key, value in details.items():
        print(f"  {key}: {value})

#This prints the following
Item: gardening_hose
  color: green
  length: 30
  price: 25.99
Item: chain_fence
  color: silver
  length: 100
  price: 120.5

# Breakdown:
On line 1, we do a for loop that will run through each kvp in the items_dict dictionary. For each iteration (run of the loop), the Key will be called "item", and it's Value will be called "details". Remember, the Value being returned is in itself a dictionary (with color, length and price). It's called "details" to match the theme and purpose.
On line 2, we print the current "item" (key of the outer dictionary the loop is currently at).
On lines 3 and 4, we loop through the "details" (or Value) of the "key" (or Item) the outer loop is currently at and print all keys and values.
```