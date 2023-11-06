from mysql_connector import connection

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
    cursor.execute(query, data)
    connection.commit()
    connection.close()