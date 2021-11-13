from flask import Blueprint,  render_template

page_html_other = Blueprint('page_html_other', __name__,
                            url_prefix="/")


@page_html_other.route("other")
def other_page():
    return render_template("other.html"), 200


@page_html_other.route("other2")
def second_other_page():
    return render_template("other2.html"), 200
