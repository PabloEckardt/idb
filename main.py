import app
import config

app = app.create_app(config)

# This is only used when running locally. When running live, gunicorn runs
# the application.
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
