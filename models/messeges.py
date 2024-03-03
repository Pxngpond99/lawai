from . import db


class Messege(db.Model):
    id = db.Column(
        db.BigInteger().with_variant(db.Integer, "sqlite"),
        primary_key=True,
        autoincrement=True,
    )
    description = db.Column(db.String)
    topic = db.Column(db.String)
    created_by = db.Column(db.String)

    created_date = db.Column(db.DateTime)


# class Messege(me.Document):
#     meta = {"collection": "messeges"}
#     description = me.StringField(required=True, max_length=256)
#     topic = me.ReferenceField("Topic", dbref=True)
#     created_by = me.StringField(required=True, max_length=256)

#     created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
