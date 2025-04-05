from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Tworzenie bazy, jeśli nie istnieje
def init_db():
    with sqlite3.connect("baza.db") as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS produkty (id INTEGER PRIMARY KEY AUTOINCREMENT, nazwa TEXT)")

@app.route('/')
def index():
    with sqlite3.connect("baza.db") as conn:
        produkty = conn.execute("SELECT * FROM produkty").fetchall()
    return render_template("index.html", produkty=produkty)

@app.route('/dodaj', methods=['POST'])
def dodaj():
    nazwa = request.form.get('nazwa')
    if nazwa:
        with sqlite3.connect("baza.db") as conn:
            conn.execute("INSERT INTO produkty (nazwa) VALUES (?)", (nazwa,))
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

