from flask import Flask, jsonify, redirect, url_for, request
import os
import pymysql

app = Flask(__name__)


@app.route('/')
def index():
    response = jsonify({"Choo Choo": "Welcome to your  Flask app 🚅"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/add', methods = ['POST', 'GET'])
def add():
    # connection = pymysql.connect( host='containers-us-west-32.railway.app', user='root', passwd='Jyfcd452Xe3tmMsFLYDY', port=5522, db='railway' )
    # with connection.cursor() as cursor:
    #     sql = "INSERT INTO table_name (name, ship, base) VALUES ('Name', 1, 0)"
    #     cursor.execute(sql)
    user = request.form['nm']
    response = jsonify({"data": user})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/insert', methods=['POST'])
def insert_row():
    name = request.form['name']
    ship = request.form['ship']
    base = request.form['base']

    query = "INSERT INTO marked_systems (name, ship, base) VALUES (%s, %s, %s)"
    values = (name, ship, base)

    connection = pymysql.connect( host='containers-us-west-32.railway.app', user='root', passwd='Jyfcd452Xe3tmMsFLYDY', port=5522, db='railway' )
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `marked_systems`"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

        cursor.execute(query, values)
        connection.commit()

    response = jsonify({'status': 'success'})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/data')
def get_data():
    connection = pymysql.connect( host='containers-us-west-32.railway.app', user='root', passwd='Jyfcd452Xe3tmMsFLYDY', port=5522, db='railway' )
    with connection.cursor() as cursor:
        
        sql = "SELECT * FROM `marked_systems`"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)



    response = jsonify({"data": result})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
