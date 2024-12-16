import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/pushbutton', methods=['GET'])
def pushbutton():
    # print(request.json['id'])
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)

