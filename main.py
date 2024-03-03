from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager

from views import messeges
import models


import os
from flask import Flask
from flask_pymongo import PyMongo


login_manager = LoginManager()
login_manager.login_view = "accounts.login"


# @login_manager.unauthorized_handler
# def unauthorized():
#     # do stuff
#     # return "You don't have permission"
#     print("You don't have permission")
#     return redirect(url_for("accounts.login"))

app = Flask(__name__)


@login_manager.user_loader
def load_user(user_id):
    user = None
    return user


@app.route("/")
def index():
    return render_template("main/index.html")


if __name__ == "__main__":
    app.secret_key = "123456"  # import os // os.get_env['SECRET_KEY']
    login_manager.init_app(app)

    # app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///:memory"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getcwd()}/db/project.db"
    models.init_app(app)

    app.register_blueprint(messeges.bp)

    app.run(debug=True)
    # app.config["MONGO_URI"] = "mongodb://localhost:27017/lawai"
    # mongo = PyMongo(app)
