import logging
import populate_db
from sqlalchemy import create_engine
from db_manager import setupdb, init_session
from flask import current_app, Flask, redirect, url_for

db_engine = None

def create_app(config, debug=False, testing=False, config_overrides=None):
    app = Flask(__name__)
    app.config.from_object(config)

    app.debug = debug
    app.testing = testing

    db_name = app.config["SQLALCHEMY_DATABASE"]
    db_engine = create_engine(db_name)
    setupdb(db_engine)
    session_token = init_session(db_engine)
    populate_db.add_restaurants(app, session_token)
    populate_db.add_reviews(app,session_token)

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
