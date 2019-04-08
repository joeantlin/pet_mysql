from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL      # import the function that will return an instance of a connection
app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL('pets_data')
    pets = mysql.query_db('SELECT * FROM pets;')
    print('*'*80)
    print(pets)
    return render_template("index.html", all_pets = pets)

@app.route("/add_data", methods=["POST"])
def add_data():
    mysql = connectToMySQL('pets_data')
    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES(%(pn)s, %(pt)s, NOW(), NOW());"
    data = {
        "pn": request.form["pname"],
        "pt": request.form["ptype"]
    }
    new_pet = mysql.query_db(query, data)
    print('*'*80)
    print(f'Pet Added')
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)