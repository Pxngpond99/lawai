from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    print(app.config["SQLALCHEMY_DATABASE_URI"])
    db.init_app(app)
    with app.app_context():
        db.create_all()


# MONGODB_DB = "lawdb"

# db = MongoEngine()


# def init_db(app):
#     db.init_app(app)


# def init_mongoengine(settings):
#     import mongoengine as me

#     dbname = settings.get("MONGODB_DB")
#     host = settings.get("MONGODB_HOST", "localhost")
#     port = int(settings.get("MONGODB_PORT", "27017"))
#     username = settings.get("MONGODB_USERNAME", "")
#     password = settings.get("MONGODB_PASSWORD", "")

#     me.connect(db=dbname, host=host, port=port, username=username, password=password)
