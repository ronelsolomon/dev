from flask import Flask, request, jsonify, render_template
import json
import os
from datetime import datetime

app = Flask(__name__)
INBOX_FILE = 'inbox.json'

def load_inbox():
    if os.path.exists(INBOX_FILE):
        with open(INBOX_FILE, 'r') as f:
            return json.load(f)
    return []

def save_inbox(inbox):
    with open(INBOX_FILE, 'w') as f:
        json.dump(inbox, f, indent=2)

@app.route('/inbound', methods=['POST'])
def inbound():
    data = request.json
    if data and 'From' in data and 'Subject' in data:
        inbox = load_inbox()
        email = {
            'from': data['From'],
            'subject': data['Subject'],
            'body': data.get('TextBody', ''),
            'receivedAt': datetime.utcnow().isoformat()
        }
        inbox.insert(0, email)
        save_inbox(inbox)
        print(f"Received: {email['subject']}")
    return '', 200

@app.route('/api/inbox')
def api_inbox():
    inbox = load_inbox()
    return jsonify(inbox)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)

