# flask --app app --debug run
import psycopg2
from flask import Flask, render_template

con = psycopg2.connect(
    host="localhost", 
    port="5432", 
    database="",
    user="postgres", 
    password=""  )  

# create the app
app = Flask(__name__)

@app.route("/")
def Index():
    cur =con.cursor() # cursor
    cur.execute("""select * from public.total""")
    list_books = cur.fetchall()
    return render_template('index.html', list_books=list_books)

#### cur.close()
#### con.close() # close the connection


@app.route("/limit")
def Limit():
    cur =con.cursor() # cursor
    cur.execute("""select * from public.total LIMIT 50""")
    list_books = cur.fetchall() 
    return render_template('limit.html', list_books=list_books)  