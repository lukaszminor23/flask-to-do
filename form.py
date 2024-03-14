from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    text = StringField("To-do text", validators=[DataRequired()])
    due_date = StringField("Due date", validators=[DataRequired()], render_kw={"placeholder": "YYYY-MM-DD"})
    submit = SubmitField("Add to-do")
