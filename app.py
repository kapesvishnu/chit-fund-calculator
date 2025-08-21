import os
from flask import Flask, send_from_directory, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/src/advanced_chit_calculator.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)