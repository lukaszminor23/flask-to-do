from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    text = StringField("To-do text", validators=[DataRequired()])
    due_date = DateField("Due date", validators=[DataRequired()])
    submit = SubmitField("Add to-do")
