from flask import Blueprint, Response, abort, request

from ..utils.crypto import encrypt_data

import bleach

auth_service_bp = Blueprint("auth_service", __name__, url_prefix="/service")


@auth_service_bp.route("/encrypt_data", methods=["POST"])
def return_encrypted_data():
    try:
        data = request.data.decode()
    except UnicodeDecodeError:
        abort(400, description="Invalid input")

    sanitized = bleach.clean(data)
    
    if sanitized == "":
        abort(400, description="Invalid input")

    encrypted_data = encrypt_data(sanitized.encode())

    return Response(encrypted_data, mimetype="application/octet-stream")