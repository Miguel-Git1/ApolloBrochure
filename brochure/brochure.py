import json

from flask import Flask

from .authentication.routes import authentication_bp
from .services.auth_service import auth_service_bp

brochure_app = Flask(__name__)
brochure_app.config.from_file("../settings.json", load=json.load)

# Blueprints
brochure_app.register_blueprint(authentication_bp)
brochure_app.register_blueprint(auth_service_bp)