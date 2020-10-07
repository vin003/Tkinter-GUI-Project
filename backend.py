import sqlite3
def connect():
     con=sqlite3.connect("books.db")
     cursor=con.cursor()
     cursor.execute("CREATE TABLE IF NOT EXISTS book (id integer PRIMARY KEY,title text, author text,year integer,isbn integer)")
     con.commit()
     con.close()

def insert(title,author,year,isbn):
     con=sqlite3.connect("books.db")
     cursor=con.cursor()
     cursor.execute("INSERT INTO  book VALUES (null,?,?,?,?)",(title,author,year,isbn))
     con.commit()
     con.close()

def view():
    con=sqlite3.connect("books.db")
    cursor=con.cursor()
    cursor.execute("SELECT * from book")
    rows=cursor.fetchall()
    con.close()
    return rows


def update(id,title,author,year,isbn):
    con=sqlite3.connect("books.db")
    cursor=con.cursor()
    cursor.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
    con.commit()
    con.close()


def search(title="",author="",year="",isbn=""):
    con=sqlite3.connect("books.db")
    cursor=con.cursor()  
    cursor.execute("SELECT * from book WHERE  title=? OR author=? OR year=? OR isbn=? ",(title,author,year,isbn))    
    rows=cursor.fetchall()
    con.close()
    return rows


def delete(id):
    con=sqlite3.    connect("books.db")
    cursor=con.cursor()
    cursor.execute("DELETE from  book  WHERE id=?",(id,))
    con.commit()
    con.close()


connect()
# print(search(author="George Wash"))
# insert("The sea","George Wash",1912,12345)
# insert("The Earth","Henry Wash",1916,12345)
# insert("The Water","Oregeon Wash",1919,12345)
# print(view())