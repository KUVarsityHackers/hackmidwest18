from flask import Flask, request, Response
from twilio.rest import Client
import sqlite3

# Events table
# User table

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':
        print(request.form)
        return Response('Success', 200)


if __name__ == '__main__':
    app.run()