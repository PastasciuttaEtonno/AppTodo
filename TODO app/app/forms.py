from binascii import Incomplete
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    text = StringField("Testo",validators=[DataRequired()],render_kw={"placeholder": "es. carote, mele, farina..."})
    title = StringField("Titolo",validators=[DataRequired()],render_kw={"placeholder": "es. spesa"})
    submit= SubmitField("Crea")



class ModifyForm(FlaskForm):
    text = StringField("Testo",validators=[DataRequired()],render_kw={"placeholder": ""})
    title = StringField("Titolo",validators=[DataRequired()],render_kw={"placeholder": ""})
    radio = RadioField(
        'Label', choices=[('option1', 'completato'), ('option2', 'incompleto')], default="option2", validators=[DataRequired()])
    #RadioField('Stato', choices=[("True",'Completato'),("False",'Incompleto')], default="False")
    submitModify= SubmitField("Modifica")
