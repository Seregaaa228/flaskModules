from flask import Blueprint, jsonify

page_init = Blueprint('page_init', __name__,
                      url_prefix="/api")


@page_init.route("/init")
def init_page():
    return jsonify("init page"), 200


@page_init.route("/init2")
def second_init_page():
    return jsonify("init 2 page"), 200
