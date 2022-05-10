from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient

import requests

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)