# dev
# 📨 Simple Email Inbox API

A lightweight Flask-based email inbox system that accepts inbound emails via webhook and provides a JSON API to access messages.

## Features

- **Inbound Email Webhook**: Accepts POST requests with email data
- **JSON Storage**: Persists emails in a simple JSON file
- **REST API**: Provides endpoints to retrieve stored emails
- **Basic Web Interface**: Simple HTML view to display inbox contents

## Tech Stack

- **Backend**: Python + Flask
- **Storage**: JSON file (`inbox.json`)
- **Frontend**: Basic HTML/CSS (via Jinja template)

## Getting Started

### Prerequisites
- Python 3.7+
- Flask

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/flask-email-inbox.git
cd flask-email-inbox
```

2. Install dependencies:
```bash
pip install flask
```

3. Run the application:
```bash
python app.py
```

The server will start at `http://localhost:8000`

## API Documentation

### POST `/inbound`
Accepts email data in JSON format

**Example Request:**
```json
{
    "From": "sender@example.com",
    "Subject": "Test Message",
    "TextBody": "Hello World!"
}
```

**Response:**
- HTTP 200 (Empty response)

### GET `/api/inbox`
Retrieve all stored emails

**Example Response:**
```json
[
    {
        "from": "sender@example.com",
        "subject": "Test Message",
        "body": "Hello World!",
        "receivedAt": "2023-11-05T12:34:56.789Z"
    }
]
```

## Project Structure
```
.
├── app.py            # Main application code
├── inbox.json        # Email storage (auto-created)
├── templates/
│   └── index.html    # Basic inbox view
└── README.md
```

## Deployment

1. **Local Testing**:
   - Use ngrok to expose your local server:
   ```bash
   ngrok http 8000
   ```
   - Configure your email service provider to send webhooks to your ngrok URL

2. **Production**:
   - Consider using:
   - Gunicorn/WSGI server
   - PostgreSQL/MongoDB for production storage
   - Environment variables for configuration
   - Docker containerization

## Security Considerations

1. Add authentication for the `/inbound` endpoint
2. Implement request validation
3. Use HTTPS in production
4. Add rate limiting
5. Consider replacing JSON file storage with a proper database

## Example Usage

View inbox in browser:
```bash
open http://localhost:8000
```

Query inbox via CLI:
```bash
curl http://localhost:8000/api/inbox
```

## Troubleshooting

**Common Issues:**
- `inbox.json` not created: Ensure write permissions in project directory
- CORS errors: Add proper CORS headers if using a frontend
- Missing fields: Ensure POST requests include `From` and `Subject` fields

## License
MIT License

---

**Next Steps**:
1. Add authentication middleware
2. Implement email filtering/sorting
3. Add pagination to API
4. Support HTML email content
5. Add attachment handling

To contribute, please fork the repository and submit a pull request.
