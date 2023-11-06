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
    query = f"insert into Publisher(name, phone, city) values ('{name}', '{phone}', '{city}')"
    cursor.execute(query)