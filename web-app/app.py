from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3

app = Flask(__name__)

def db_connect():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    conn = db_connect()
    inventory =  conn.execute('SELECT * FROM inventory').fetchall()
    conn.close()
    return render_template('index.html', inventory=inventory)

@app.route('/add_item')
def add_item():
    return render_template('add_item.html')

@app.route('/remove_item')
def remove_item():
    return render_template('remove_item.html')



@app.route('/add_stock', methods=['POST'])    
def add_stock():
    model = request.form['model']
    serial_num = request.form['serial_num']
    condition_notes = request.form['condition_notes']

    conn = db_connect()
    conn.execute('INSERT INTO inventory (model, serial_num, condition) VALUES (?, ?, ?)', (model, serial_num, condition_notes))
    conn.commit()
    conn.close()
    return f"<h3>Item Added Successfully!</h3> <br> Model: {model} <br> Serial Number: {serial_num} <br> Condition and Notes: {condition_notes} <br> <form action=\"{url_for('home')}\" method=\"GET\"><button type=\"submit\">Go Back!</button></form>"   
    
@app.route('/remove_stock', methods=['POST']) 
def remove_stock():
    id_num = request.form['id_num']
    model = request.form['model']
    serial_num = request.form['serial_num']

    conn = db_connect()
    if id_num:
        conn.execute("DELETE FROM inventory WHERE id =?", (int(id_num),))
    elif model and serial_num:
        conn.execute("DELETE FROM inventory WHERE model = ? AND serial_num = ?",(model, serial_num))
    else:
        conn.close()
        flash("Enter an ID, OR Both a Model and Serial Number!")
        return redirect(url_for("remove_item"))

    conn.commit()
    conn.close()

    return redirect(url_for("home"))
if __name__ == "__main__":
    app.run(debug=True)