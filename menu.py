import sys
import book_dao

menu_options = {
    1: 'Add a Publisher',
    2: 'Add a Book',
    3: 'Edit a Book',
    # More options to be added
    5: 'Search Books',
    6: 'Exit',
}

search_menu_options = {
    # To be added
}

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


# def search_by_title():
#   To be added

def print_menu():
    print()
    print("Please make a selection")
    for key in menu_options.keys():
        print (str(key)+'.', menu_options[key], end = "  ")
    print()
    print("The end of top-level options")
    print()


def option1():
    print('-----------ADD A PUBLISHER-----------')
    print('To add a publisher, write the data in the following format: [name] [phoneNo] [city]')
    print('To cancel the entry, type NULL')
    publisherData = input("Enter the publisher data here:")
    if publisherData == "NULL":
        print("Entry canceled")
        return
    data = publisherData.split()
    name, phone, city = data
    if not isPublisherDataValid(name, phone, city):
        return
    result = book_dao.addAPublisher(name, phone, city)
    print(result)


def option2():
    print('-----------ADD A BOOK-----------')
    print('To add a book, input the data in the following format:')
    print('[ISBN], [title], [year], [published_by], [previous_edition], [price]')
    print('To cancel the entry, type NULL')
    bookData = input("Enter the book data here:")
    if bookData == 'NULL':
        print("Entry cancelled")
        return
    data = bookData.split(',')
    ISBN, title, year, published_by, previous_edition, price = data
    if isBookDataValid(ISBN, title, year, published_by, previous_edition, price):
        return
    result = book_dao.addABook(ISBN, title, year, published_by, previous_edition, price)
    print(result)

def option5():
    # A sub-menu shall be printed
    # and prompt user selection

    # print_search_menu

    # user selection of options and actions

    # Assume the option: search all books was chosen
    print("Search Option 1: all books were chosen.")
    search_all_books()



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
        # More options to be added
        elif option == 5:
            option5()
        elif option == 6:
            print('Thanks your for using our database services! Bye')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 6.')


def isPublisherDataValid(name, phone, city):
    if name == None or phone == None or city == None:
        print('Entry incomplete')
        return False
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

def isBookDataValid(ISBN, title, year, published_by, previous_edition, price):
    if ISBN == None or title == None or year == None or published_by == None or previous_edition == None or price == None:
        print('Entry incomplete')
        return False
    if len(ISBN) != 10:
        print("ISBN must be 10 characters long")
        return False
    if len(title) > 50:
        print("Title can't be longer than 50 characters")
        return False
    try:
        int(year)
    except ValueError:
        print('Year must be an integer')
        return False
    if len(published_by) > 25:
        print("Published name can't be longer than 25 characters")
        return False
    if len(previous_edition) > 10:
        print("Previous edition can't be longer than 10 characters")
        return False
    try:
        float(price)
    except ValueError:
        print('Price must be a floating point value')
        return False
    return True