from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'your_mail_server'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/helpme', methods=['POST'])
def helpme():
    email = request.json.get('email')
    if not email:
        return jsonify({"error": "Missing email"}), 400

    msg = Message("Help Request", sender='your_email@example.com', recipients=[email])
    msg.html = "<h1>Help Request</h1><p>Your help request has been received.</p>"
    mail.send(msg)

    return jsonify({"message": "Email sent successfully to {}".format(email)}), 200
