from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Speicher für Nachrichten (maximal 3 zuletzt gepostete Nachrichten)
messages = []

@app.route('/')
def input_page():
    return render_template('input.html')

@app.route('/output')
def output_page():
    return render_template('output.html')

@app.route('/post_message', methods=['POST'])
def post_message():
    global messages
    data = request.json
    if 'message' in data:
        messages.append(data['message'])
        # Nur die letzten 3 Nachrichten speichern
        messages = messages[-8:]
        return jsonify({'status': 'success'}), 200
    return jsonify({'status': 'error', 'message': 'No message provided'}), 400

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

if __name__ == '__main__':
    app.run(debug=True)
