from flask import Flask, request, Response
from twilio.rest import Client
import sqlite3

# Events table
# User table

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':
        handle_response(request.form)
        return Response('', 204)

def handle_requst(request_data):
    for key, value in request_data.items():
        print(key, value)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)