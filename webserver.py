from flask import Flask, request, Response
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import sqlite3
import os.path

# Events table
#  table

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        handle_requst(request.form)
        return Response('', 204)

def handle_requst(request_data):
    for key, value in request_data.items():
        print(key, value)

def initializeDatabase():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE events
    (key INTEGER PRIMARY KEY, title TEXT, date TEXT, cap INTEGER, creator TEXT, details TEXT)''')

    c.execute('''CREATE TABLE attendee
    (key INTEGER PRIMARY KEY, name TEXT, phone TEXT, eventID INTEGER, status TEXT)''')


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    if not os.path.isfile('database.db'):
        initializeDatabase()