from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import validators
from wtforms import widgets


class MessegeForm(FlaskForm):

    description = StringField("พิมพ์ข้อความ", validators=[validators.DataRequired()])
