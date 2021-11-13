from flask import Flask
from api import page_init, items, user
from pages import page_html_init, main, other

app = Flask(__name__)

app.register_blueprint(page_init)
app.register_blueprint(items.page_items)
app.register_blueprint(user.page_user)

app.register_blueprint(page_html_init)
app.register_blueprint(main.page_html_main)
app.register_blueprint(other.page_html_other)



if __name__ == '__main__':
    app.run(debug=True)
