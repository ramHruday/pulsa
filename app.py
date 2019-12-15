import traceback

from flask import Flask
from services import dialog_service

app = Flask(__name__)

app.register_blueprint(dialog_service.dialog)

if __name__ == '__main__':
    try:
        app.run()
    except:
        traceback.print_exc()
