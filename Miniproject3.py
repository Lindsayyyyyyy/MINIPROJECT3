from flask import Flask, render_template, request
import sqlite3
import pandas as pd
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def __function1__():
    # function for the home page

    # triggered when you press 'submit' on the entry form
    with sqlite3.connect("productdata.db") as con:
        if (request.method == "POST"):
            input1 = request.form["input"]
            input2 = request.form["input2"]
            input3 = request.form["input3"]
            input4 = request.form["input4"]
            con.execute("CREATE TABLE IF NOT EXISTS product(category TEXT, productDescription TEXT, price NUMERIC, productCode TEXT)")
            con.execute("INSERT INTO product(category, productDescription,price,productCode) VALUES(?,?,?,?)", [input1, input2, input3, input4])
            con.commit()
    return render_template("homepage.html")
    

@app.route("/productdata", methods=['GET','POST'])
def __function2__():
    # page for entering data
    if (request.method == "GET"):
        return render_template("productdata.html")


@app.route("/retrievedata", methods=['GET'])
def __function3__():

    # page for viewing data
    # normal way of accessing
    if request.method == "GET":
        return render_template("retrievedata.html", title = "Product Data Entry")

@app.route('/retrievedata', methods = ['POST'])
def list():
    cats= request.form["category"].strip()

    with sqlite3.connect("productdata.db") as con:
        if cats != "":
            df = pd.read_sql("SELECT * FROM product WHERE category =?", con, params = (cats,))
        else:
            df = pd.read_sql("SELECT * FROM product", con)
    return render_template("requesteddata.html", df=df, title = "Retrieval from Database")

    
app.run(debug=True)
    