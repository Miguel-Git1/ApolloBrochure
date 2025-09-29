import json

from flask import Flask

from .authentication.routes import authentication_bp
from .dashboard.routes import dashboard_bp

brochure_app = Flask(__name__)
brochure_app.config.from_file("../settings.json", load=json.load)

# Blueprints
brochure_app.register_blueprint(authentication_bp)
brochure_app.register_blueprint(dashboard_bp)