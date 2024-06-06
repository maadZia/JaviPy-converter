
from flask import Flask, request, jsonify, send_from_directory
import subprocess
import os
from main import main

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    java_code = data.get('java_code')
    if not java_code:
        return jsonify({'error': 'No code provided'}), 400

    with open('input.java', 'w') as f:
        f.write(java_code)

    try:
        main('input.java', 'output.py')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    try:
        with open('output.py', 'r') as f:
            python_code = f.read()
    except Exception as e:
        return jsonify({'error': 'Conversion failed or output file not found', 'details': str(e)}), 500

    return jsonify({'python_code': python_code})

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
