from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, login_user, logout_user

from werkzeug.security import generate_password_hash, check_password_hash

from forms import messeges as ms

import datetime
import models
from models.messeges import Messege
from models.topics import Topic

bp = Blueprint("messeges", __name__, url_prefix="/messeges")


def get_answer(text):

    messege = Messege()

    messege.description = "คำตอบของคำถาม"
    messege.created_by = "Ai"
    messege.created_date = datetime.datetime.now()
    models.db.session.add(messege)
    models.db.session.commit()


@bp.route(
    "/",
    methods=["GET", "POST"],
    defaults={"topic_name": None},
)
@bp.route("/<topic_name>/", methods=["GET", "POST"])
def index(topic_name):

    messeges = None
    messeges = models.db.session.query(Messege)
    if topic_name:
        messeges = models.db.session.query(Messege).filter_by(topic=topic_name)
    # if topic_name:
    #     messeges = Messege.objects(topic=topic_obj)

    # topics = Topic.objects()

    # print("------------>", topics)

    print("------------>", messeges)
    topics = models.db.session.query(Topic)

    form = ms.MessegeForm()
    if not form.validate_on_submit():
        print(form.errors)
        return render_template(
            "/messeges/index.html",
            form=form,
            messeges=messeges,
            topics=topics,
        )

    messege = Messege()
    form.populate_obj(messege)
    messege.created_by = "User"
    messege.created_date = datetime.datetime.now()

    if not topic_name:

        topic = Topic()
        topic.name = form.description.data

        topic.created_date = datetime.datetime.now()
        models.db.session.add(topic)
        models.db.session.commit()
        messege.topic = form.description.data
        topic_name = topic.name
    else:
        messege.topic = topic_name
        topic_name = topic_name

    models.db.session.add(messege)
    models.db.session.commit()
    if form.description.data:
        get_answer(form.description.data)
    messeges = models.db.session.query(Messege)
    if topic_name:
        messeges = models.db.session.query(Messege).filter_by(topic=topic_name)

    return redirect(url_for("messeges.index", topic_name=topic_name))
