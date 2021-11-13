from flask import Blueprint, render_template

page_html_init = Blueprint('page_html_init', __name__,
                           url_prefix="/")


@page_html_init.route("init")
def init_page():
    return render_template("init.html"), 200


@page_html_init.route("init2")
def second_init_page():
    return render_template("init2.html"), 200
