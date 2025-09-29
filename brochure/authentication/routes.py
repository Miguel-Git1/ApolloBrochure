from flask import Blueprint, Response

authentication_bp = Blueprint("authentication_bp", __name__, url_prefix="/auth")

@authentication_bp.route("login/")
def login():
    return Response("This is the login page.")