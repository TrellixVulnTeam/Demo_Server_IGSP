from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    print('this is master branch')
    app.debug = True
    print('this is test branch')
    app.run()
