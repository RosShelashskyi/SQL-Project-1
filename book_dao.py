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

def addAPublisher(name, phone, city):
    cursor = connection.cursor()
    query = "insert into Publisher(name, phone, city) values (%s, %s, %s)"
    data = (name, phone, city)
    try:
        cursor.execute(query, data)
        connection.commit()
    except mysql.connector.errors.IntegrityError:
        cursor.close()
        return "Duplicate entry: publisher <" + name + "> already exists"
    cursor.close()
    return "Publisher <" + name + "> added successfully"

def addABook(ISBN, title, year, published_by, previous_edition, price):
    cursor = connection.cursor()
    query = "insert into Book(ISBN, title, year, published_by, previous_edition, price) values (%s, %s, %s, %s, %s, %s)"
    data = (ISBN, title, year, published_by, previous_edition, price)
    try:
        cursor.execute(query, data)
        connection.commit()
    except mysql.connector.errors.IntegrityError:
        cursor.close()
        return "Duplicate entry: book <" + title + "> already exists"
    cursor.close()
    return "Book <" + title + "> added successfully"