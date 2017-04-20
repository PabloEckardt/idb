import logging
from app import populate_db
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from app.db_manager import setupdb, init_session
from flask import current_app, Flask, redirect, url_for
from flask_cors import CORS

db_name = "sqlite:///app/db/food_close_to.db"
db_engine = create_engine(db_name)
setupdb(db_engine)
session_factory = init_session(db_engine)
Session = scoped_session(session_factory)


def create_app(config, debug=False, testing=False, config_overrides=None):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)

    app.debug = debug
    app.testing = testing

    populate_db.add_restaurants(app)
    populate_db.add_reviews(app)
    populate_db.add_food_types(app)
    populate_db.add_locations(app)

    if config_overrides:
        app.config.update(config_overrides)

    # Configure logging
    if not app.testing:
        logging.basicConfig(level=logging.INFO)

    # Register the Bookshelf VIEWS blueprint.
    from . views import views
    app.register_blueprint(views, url_prefix='')

    # Add a default root route.
    @app.route("/")
    def index():
        return redirect(url_for('views.index'))

    # Add an error handler. This is useful for debugging the live application,
    # however, you should disable the output of the exception for production
    # applications.
    @app.errorhandler(500)
    def server_error(e):
        return """
        An internal error occurred: <pre>{}</pre>
        See logs for full stacktrace.
        """.format(e), 500

    return app
