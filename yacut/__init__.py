import traceback
try:
    from dotenv import load_dotenv
    from flask import Flask
    from flask_migrate import Migrate
    from flask_sqlalchemy import SQLAlchemy

    from settings import Config

    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    from . import api_views, error_handlers, models, views  # nopep8
except Exception as e:
    print('При запуске приложения произошла ошибка:')
    traceback.print_exc()