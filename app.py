from flask import Flask, render_template, url_for, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')         # hovedside
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])         # funksjon som sjekker login
def login():
    un = request.form['un']         # leser brukernavn fra skjema
    pwd = request.form['pwd']         # leser passord fra skjema
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM login WHERE username=? AND pwd=?", (un, pwd))         # leter etter brukeren i DB
        records = cur.fetchall()
    if len(records) >= 1:         # fant brukeren
        msg = "Welcome " + un
    else:         # fant ikke brukeren
        msg = "Wrong username or password"
    return render_template("result.html", msg=msg)

@app.route('/enternew')         # siden hvor du lager ny bruker
def new_student():
    return render_template('student.html')

@app.route('/addrec', methods=['POST'])           # funksjon som legger ny bruker i DB
def addrec():
    if request.method == 'POST':
        try:
            un = request.form['un']         # leser skjemafelt
            pwd = request.form['pwd']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO login (username, pwd) VALUES (?,?)", (un, pwd))         # legger til brukeren i DB
                con.commit()
                msg = "Record sucessfully added"
        except:
             msg = "error in insert operation"
        finally:
            return render_template("result.html", msg=msg)
            con.close()

@app.route('/list')         # siden hvor du ser tabellen med alle brukerne fra DB
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from login")           # lese alle brukerne
    rows = cur.fetchall()
    return render_template('list.html', rows=rows)

if __name__ == "__main__":
    app.run(debug=True)