# The import command looks through the project folder (where main.py is and any subfolders).
# And looks for a file with this name to import as a MODULE, in this case books.py. It takes all its functions and makes them available in this file
# import books -> imports all the functions
# import books as b -> same as above, but it changes the name to b. Instead of books.function() you use b.function(). Can have any name you want
# from books import remove_book -> imports only a specific function. Used to save memory (dont worry about it for small projects like this)
import books 

def main():
    # Using functions from a module is as easy as modulename.function(arguments).
    # Check books.py for more info but hovering your mouse over the function call here should give plenty information
    books.edit_or_add_book("harry potter ", "fantasy", "20", "hogwarts")

    # The following line works because books.remove_book returns a value that we can print.
    # This is where the concept of the Stack comes into play. As this line runs, the following happens
    # print() tries to print to screen what's inside the (); but inside is a function call that wants to run too.
    # And so the program adds things to the Stack that run in sequence and only when all are resolved will print actually print the result
    # print() -> books.remove_book() runs -> books.remove_book() ends and returns value -> print()
    print(books.remove_book("harry potter"))


if __name__ == "__main__":
    main()