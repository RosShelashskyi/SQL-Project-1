from mysql_connector import connection
import mysql.connector

#returns all books in the database
def findAll():
    cursor = connection.cursor()
    query = "select * from bookmanager.Book"
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results
    
#returns all books with title <title>
def findByTitle(title):
    cursor = connection.cursor()
    query = "select * from Book where title = '" + title + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results

#returns all books with ISBN <ISBN>
def findByISBN(ISBN):
    cursor = connection.cursor()
    query = "select * from Book where ISBN = '" + ISBN + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results

#returns all books with publisher <published_by>
def findByPublisher(published_by):
    cursor = connection.cursor()
    query = "select * from Book where published_by = '" + published_by + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results

#returns all books with price between <min> and <max>
def findByPrice(min, max):
    cursor = connection.cursor()
    query = "select * from Book where price between " + min + " and " + max
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results

#returns all books with year <year>
def findByYear(year):
    cursor = connection.cursor()
    query = "select * from Book where year = " + year
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results

#returns all books with title <title> and publisher <published_by>
def findByTitleAndPublisher(title, published_by):
    cursor = connection.cursor()
    query = "select * from Book where title = '" + title + "' and published_by = '" + published_by + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results

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
    if previous_edition == 'null' or len(previous_edition) < 1:
        previous_edition = None
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
        return "Duplicate entry: book <" + title + "> already exists or the input was incorrect"
    #close the connection and return the successful result
    cursor.close()
    return "Book <" + title + "> added successfully"

#function to edit a book
def editABook(ISBN, title, year, published_by, previous_edition, price):
    cursor = connection.cursor()
    query = 'update Book'
    #insert set statement into the query if the variables aren't null
    if title != None:
        query += " set title = '" + title + "',"
    if year != None:
        query += ' set year = ' + year + ','
    if published_by != None:
        query += " set published_by = '" + published_by + "',"
    if previous_edition != None:
        query += " set previous_edition = '" + previous_edition + "',"
    if price != None:
        query += 'set price = ' + price
    #remove the ',' from the last statement if there is ','
    if query[len(query) - 1] == ',':
        newquery = query[0:len(query) - 1]
    else:
        newquery = query 
    #execute the query
    newquery += " where ISBN = '" + ISBN + "'"
    cursor.execute(newquery)
    connection.commit()
    #close conection and return
    cursor.close()
    return "Book with ISBN: " + ISBN + " has been edited successfully"

#deletes a book with ISBN <ISBN>
def deleteABook(ISBN):
    cursor = connection.cursor()
    query = "delete from Book where ISBN = '" + ISBN + "'"
    cursor.execute(query)
    connection.commit()
    cursor.close()
    return "Book with ISBN " + ISBN + " sucessfully deleted"