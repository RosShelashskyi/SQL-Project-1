from mysql_connector import connection
import mysql.connector

def findAll():
    cursor = connection.cursor()
    query = "select * from bookmanager.Book"
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results
    

# def findByTitle(title):
#     to be added

#function to add a publisher to the database
def addAPublisher(name, phone, city):
    #create a connection
    cursor = connection.cursor()
    #construct the query
    query = "insert into Publisher(name, phone, city) values (%s, %s, %s)"
    data = (name, phone, city)
    #try to execute the query
    try:
        cursor.execute(query, data)
        connection.commit()
    except mysql.connector.errors.IntegrityError:
        #close the connection if the entry is duplicate and return the error message
        cursor.close()
        return "Duplicate entry: publisher <" + name + "> already exists"
    #close the connection and return the successful result
    cursor.close()
    return "Publisher <" + name + "> added successfully"

#function to add a book to the database
def addABook(ISBN, title, year, published_by, previous_edition, price):
    #create a connection
    cursor = connection.cursor()
    #construct the query
    query = "insert into Book(ISBN, title, year, published_by, previous_edition, price) values (%s, %s, %s, %s, %s, %s)"
    data = (ISBN, title, year, published_by, previous_edition, price)
    #try to execute the query
    try:
        cursor.execute(query, data)
        connection.commit()
    except mysql.connector.errors.IntegrityError:
        #close the connection if the entry is duplicate and return the error message
        cursor.close()
        return "Duplicate entry: book <" + title + "> already exists"
    #close the connection and return the successful result
    cursor.close()
    return "Book <" + title + "> added successfully"