import json

from flask import Flask, render_template

from .authentication.routes import authentication_bp

brochure_app = Flask(__name__, static_folder="static", template_folder="template")
brochure_app.config.from_file("../settings.json", load=json.load)

# Blueprints
brochure_app.register_blueprint(authentication_bp)