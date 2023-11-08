import sys
import book_dao

menu_options = {
    1: 'Add a Publisher',
    2: 'Add a Book',
    3: 'Edit a Book',
    4: 'Delete a Book',
    5: 'Search Books',
    6: 'Exit',
}

search_menu_options = {
    1: 'Search all books',
    2: 'Search by title',
    3: 'Search by ISBN',
    4: 'Searched by publisher',
    5: 'Search by price range',
    6: 'Search by year',
    7: 'Search by title and publisher'
}

#function for checking the input when adding a publisher
def isPublisherDataValid(name, phone, city):
    if len(name) > 25:
        print("Name is too long. The Name can be up to 25 characters long")
        return False
    if len(phone) != 10:
        print("Phone numbers must be 10 characters long")
        return False
    try:
        int(phone)
    except ValueError:
        print("Phone numbers must consists of integers")
        return False
    if len(city) > 20:
        print("City name is too long. City names can be up to 20 characters long")
        return False
    return True

#function for checking the input when adding a book
def isBookDataValid(ISBN, title, year, published_by, previous_edition, price):
    if ISBN != None and len(ISBN) != 10:
        print("ISBN must be 10 characters long")
        return False
    if title != None and len(title) > 50:
        print("Title can't be longer than 50 characters")
        return False
    if(year != None):
        try:
            int(year)
        except ValueError:
            print('Year must be an integer')
            return False
    if published_by != None and len(published_by) > 25:
        print("Published name can't be longer than 25 characters")
        return False
    if previous_edition != None and len(previous_edition) > 10:
        print("Previous edition can't be longer than 10 characters")
        return False
    if price != None:
        try:
            float(price)
        except ValueError:
            print('Price must be a floating point value')
            return False
    return True

def search_all_books():
    # Use a data access object (DAO) to 
    # abstract the retrieval of data from 
    # a data resource such as a database.
    results = book_dao.findAll()

    # Display results
    print("The following are the ISBNs and titles of all books.")
    for item in results:
        print(item[0], item[1])
    print("The end of books.")


def search_by_title():
    print()
    title = input('Enter the title of books you want to find: ')
    print("The following are the ISBNs and titles of all books with title '" + title + "'")
    results = book_dao.findByTitle(title)
    for item in results:
        print(item[0], item[1])
    print('End of search')

def print_menu():
    print()
    print("Please make a selection")
    for key in menu_options.keys():
        print (str(key)+'.', menu_options[key], end = "  ")
    print()
    print("The end of top-level options")
    print()

def print_search_menu():
    print()
    print("Select a search option")
    for key in search_menu_options.keys():
        print(str(key) + '.', search_menu_options[key], end = ' ')
    print()
    print()


def option1():
    #output instructions for the user
    print('-----------ADD A PUBLISHER-----------')
    print('To add a publisher, write the data in the following format: [name], [phoneNo], [city]')
    print('To cancel the entry, type NULL')
    #take user input
    publisherData = input("Enter the publisher data here: ")
    #check if entry is NULL and return if needed
    if publisherData == None:
        print("Entry canceled")
        return
    #parse the input into words
    data = publisherData.split(',')
    #pass the words into variables
    try:
        name, phone, city = data
    except ValueError:
        print("Error: Entry is incomplete")
        return
    #check if input is valid and can be used in the query. return otherwise
    if not isPublisherDataValid(name, phone, city):
        return
    #call the function in book_dao
    result = book_dao.addAPublisher(name, phone, city)
    #print the result
    print(result)


def option2():
    #output instructions for the user
    print('-----------ADD A BOOK-----------')
    print('To add a book, input the data in the following format:')
    print('[ISBN], [title], [year], [published_by], [previous_edition], [price]')
    print("If the book doesn't have a previous edition, input null instead")
    print('To cancel the entry, type NULL')
    #take user input
    bookData = input("Enter the book data here: ")
    #check if input is NULL and return if needed
    if bookData == None:
        print("Entry cancelled")
        return
    #parse the input into words
    data = bookData.split(', ')
    #pass the words into variables
    try:
        ISBN, title, year, published_by, previous_edition, price = data
    except ValueError:
        print("Error: the entry is incomplete")
        return
    #check if input is valid and can be used in the query. return otherwise
    if not isBookDataValid(ISBN, title, year, published_by, previous_edition, price):
        return
    #call the function in book_dao
    result = book_dao.addABook(ISBN, title, year, published_by, previous_edition, price)
    #print the result
    print(result)

def option3():
    print('-----------EDIT A BOOK-----------')
    ISBN = input('Enter the ISBN of the book you want to edit: ')
    print('Input new values for each field. Press enter if you want to leave the field unchanged')
    title = input('Input new title or press Enter: ')
    year = input('Input new year or press Enter: ')
    published_by = input('Input new published or press Enter: ')
    previous_edition = input('Input new previous edition or press Enter: ')
    price = input('Input new price or press Enter: ')

    if len(title) < 1: title = None
    if len(year) < 1: year = None 
    if len(published_by) < 1: published_by = None 
    if len(previous_edition) < 1: previous_edition = None
    if len(price) < 1: price = None 

    if not isBookDataValid(ISBN, title, year, published_by, previous_edition, price):
        return
    result = book_dao.editABook(ISBN, title, year, published_by, previous_edition, price)
    print(result)

def option4():
    print('-----------DELETE A BOOK-----------')
    print('WARNING: AFTER DELETION THE ENTRY WILL BE PERMANENTLY LOST')
    ISBN = input('Enter the ISBN of the book you want to delete: ')
    
    if len(ISBN) != 10: 
        print('Error: ISBN must be 10 characters long')
        return 
    result = book_dao.deleteABook(ISBN)
    print(result)

def option5():
    print_search_menu()

    option = ''
    try:
        option = int(input('Enter your choice: '))
    except KeyboardInterrupt:
        print('Interrupted')
        return
    except:
        print('Wrong input. Please enter a number')
    
    if option == 1:
        print("Search Option 1: all books were chosen.")
        search_all_books()
    elif option == 2:
        print("Search Option 2: search by title was chosen")
        search_by_title()
    else:
        print('Invalid option. Please enter a number betwee 1 and 7')

    # Assume the option: search all books was chosen
    



if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        except:
            print('Wrong input. Please enter a number ...')

        # Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            print('Thanks your for using our database services! Bye')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 6.')

