from flask import Flask

app = Flask(__name__)       # creating an app instance


@app.route('/')             # at the end point /
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':  # on running python app.py
    app.run(debug=True)               # run the flask app
