from flask import Blueprint,  render_template

page_html_main = Blueprint('page_html_main', __name__,
                           url_prefix="/")


@page_html_main.route("main")
def main_page():
    return render_template("main.html"), 200


@page_html_main.route("main2")
def second_main_page():
    return render_template("main2.html"), 200
