import json

from flask import Flask


app = Flask("main")

if __name__ == '__main__':
    app.config.from_file("settings.json", load=json.load)
    app.run(debug=True)