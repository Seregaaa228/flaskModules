from flask import Blueprint, jsonify

page_items = Blueprint('page_items', __name__,
                       url_prefix="/api")


@page_items.route("/items")
def items_page():
    return jsonify("items page"), 200


@page_items.route("/items2")
def second_items_page():
    return jsonify("items2 page"), 200
