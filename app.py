from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
import os
import requests

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./static"
basedir = os.path.abspath(os.path.dirname(__file__))


SECRET_KEY = 'SPARTA'

client = MongoClient('mongodb+srv://test:sparta@cluster0.zosuv.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def main():
    # token_receive = request.cookies.get('mytoken')
    # payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    # user_info = db.users.find_one({"username": payload["id"]})
    return render_template('index.html')#, user_info=user_info)


@app.route('/register')
def register_page():
    return render_template("write.html")


@app.route('/register/save', methods=['POST'])
def register():
    token_receive = request.cookies.get('mytoken')
    try:
        # payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        # # 포스팅하기
        # user_info = db.users.find_one({"username": payload["id"]})
        mountain_receive = request.form["mountain_give"]
        route_receive = request.form["route_give"]
        location_receive = request.form["location_give"]
        facilities_receive = request.form["facilities_give"]
        facilities_receive = [int(val) for val in facilities_receive.split(',')]
        description_receive = request.form["description_give"]

        doc = {
                "mountain": mountain_receive,
                "route": route_receive,
                "location": location_receive,
                "fa": facilities_receive,
                "desc": description_receive
        }
        if 'file_give' in request.files:
            file = request.files["file_give"]
            filename = secure_filename(file.filename).split('.')[0]
            print(filename)
            extension = secure_filename(file.filename).split('.')[-1]
            today = datetime.now()
            my_time = today.strftime('%Y%m%d%H%M%s')
            file_name = f'{filename}-{my_time}.{extension}'
            file_path = f"./static/{file_name}.{extension}"
            file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], file_name))
            doc["pic"] = file_name

        db.mountain_info.insert_one(doc)
        print(doc)
        return jsonify({"result": "success", 'msg': '포스팅 성공'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("main"))


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)