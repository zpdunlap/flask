from flask import Flask, jsonify, redirect, url_for, request
import os
import pymysql

app = Flask(__name__)


@app.route('/')
def index():
    response = jsonify({"Choo Choo": "Welcome to your  Flask app 🚅"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/add')
def index():
    user = request.form['nm']
    response = jsonify({"data": user})
    response.headers.add("Access-Control-Allow-Origin", "*")


@app.route('/data')
def get_data():
    connection = pymysql.connect( host='containers-us-west-32.railway.app', user='root', passwd='Jyfcd452Xe3tmMsFLYDY', port=5522, db='railway' )
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `name` FROM `marked_systems` WHERE `id`=%s"
        cursor.execute(sql, ('1',))
        result = cursor.fetchone()
        print(result)



    response = jsonify({"data": result})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
