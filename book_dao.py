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
        print("Duplicate entry: publisher <" + name + "> already exists")
    cursor.close()
    return "Publisher <" + name + "> added successfully"