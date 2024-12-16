import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/pushbutton', methods=['POST'])
def pushbutton():
    print(request.json['id'])
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

