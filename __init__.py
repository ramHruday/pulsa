import os
from flask import Flask


def create_app():
    try:
        app = Flask(__name__)
        app.config.from_mapping(
            SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key'
        )
        from . import main
        app.register_blueprint(main.bp)
        print('y')
        return app.run()
    except Exception as e:
        print(e)