import app
import config
import json

app = app.create_app(config)

raw_data = None
with open ("mega.json", "r") as mega:
   raw_data = json.load(mega)

# This is only used when running locally. When running live, gunicorn runs
# the application.
if __name__ == '__main__':
    app.run(debug=True)
