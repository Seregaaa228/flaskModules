import pydantic
from flask import Blueprint, jsonify, request
from pydantic import BaseModel
from typing import Optional


class ValidationClass(BaseModel):
    login: str
    password: str
    userList: Optional[list]


page_user = Blueprint('page_user', __name__,
                      url_prefix="/api")


@page_user.route("/validation", methods=['POST'])
def validation_user_page():
    try:
        validation = ValidationClass(**request.json)
    except pydantic.error_wrappers.ValidationError as err:
        return jsonify(str(err)), 415
    return jsonify(str(validation)), 200


@page_user.route("/user")
def user_page():
    return jsonify("user page"), 200
