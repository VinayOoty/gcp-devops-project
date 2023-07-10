from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "<h1>Sample, Python Flask Application - v1.0</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
