from . import db


class Topic(db.Model):
    id = db.Column(
        db.BigInteger().with_variant(db.Integer, "sqlite"),
        primary_key=True,
        autoincrement=True,
    )
    name = db.Column(db.String)

    created_date = db.Column(db.DateTime)


# class Topic(me.Document):
#     meta = {"collection": "topics"}
#     name = me.StringField(required=True, max_length=256)
#     creted_by = me.StringField(required=True, max_length=256)
#     created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
