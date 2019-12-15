import traceback

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'OK!'


if __name__ == '__main__':
    try:
        print('u')
        app.run()
    except:
        traceback.print_exc()
